#!/usr/bin/env python3
"""
DEPLOY AUTÔNOMO — CLAUDE COWORKING JURISPERITUS
Mecanismo: git push → GitHub → Netlify CI/CD deploy automático
"""

import os, subprocess, datetime, sys

BASE      = "/home/claude/jurisperitus"
GH_USER   = "jurisperitusescolaonline-crypto"
GH_TOKEN  = "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"
REPO      = "jurisperitus-coworking"
REMOTE    = f"https://{GH_USER}:{GH_TOKEN}@github.com/{GH_USER}/{REPO}.git"
LOG_DIR   = f"{BASE}/relatorios"
os.makedirs(LOG_DIR, exist_ok=True)

def run(cmd, cwd=BASE):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    return r.returncode == 0, r.stdout.strip(), r.stderr.strip()

def deploy(mensagem: str = None):
    ts  = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    msg = mensagem or f"deploy: atualização automática Claude Coworking — {ts}"

    print(f"\n🚀 DEPLOY AUTÔNOMO — {ts}")
    print("=" * 55)

    # 1. Garantir remote com token
    ok, _, _ = run(["git", "remote", "set-url", "origin", REMOTE])

    # 2. Stage tudo
    ok, out, err = run(["git", "add", "-A"])
    print(f"  stage:  {'✅' if ok else '❌'} {out or err or 'ok'}")

    # 3. Verificar se há algo para commitar
    ok2, status, _ = run(["git", "status", "--porcelain"])
    if not status:
        print("  commit: ⏭️  nada a commitar — já está atualizado")
    else:
        ok, out, err = run(["git", "commit", "-m", msg])
        print(f"  commit: {'✅' if ok else '❌'} {out.splitlines()[-1] if out else err}")

    # 4. Push
    ok, out, err = run(["git", "push", "origin", "main"])
    resultado = "✅ Push OK — Netlify deployando" if ok else f"❌ Erro: {err}"
    print(f"  push:   {resultado}")

    # 5. Log
    log = f"{LOG_DIR}/deploy_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(log, "w") as f:
        f.write(f"Data: {ts}\nMensagem: {msg}\nStatus: {'OK' if ok else 'ERRO'}\n{out}\n{err}")

    print(f"\n  Log: {log}")
    print("=" * 55)
    if ok:
        print("  ✅ Netlify irá deployar em ~30 segundos")
        print("  🌐 https://jurisperitus.com.br")
    return ok

if __name__ == "__main__":
    msg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    deploy(msg)
