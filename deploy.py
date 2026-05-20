#!/usr/bin/env python3
"""
DEPLOY AUTÔNOMO — CLAUDE COWORKING JURISPERITUS
Mecanismo: git push → GitHub Pages (direto, sem serviço externo)
"""

import os, subprocess, datetime, sys, shutil

BASE     = "/home/claude/jurisperitus"
GH_USER  = "jurisperitusescolaonline-crypto"
GH_TOKEN = "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"
REPO     = "jurisperitus-coworking"
REMOTE   = f"https://{GH_USER}:{GH_TOKEN}@github.com/{GH_USER}/{REPO}.git"
LOG_DIR  = f"{BASE}/relatorios"
os.makedirs(LOG_DIR, exist_ok=True)

def run(cmd, cwd=BASE):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    return r.returncode == 0, r.stdout.strip(), r.stderr.strip()

def sincronizar_docs():
    """Copia arquivos atualizados para docs/ antes do push."""
    src = f"{BASE}/OS-ativas/netlify-deploy/index.html"
    dst = f"{BASE}/docs/index.html"
    if os.path.exists(src):
        shutil.copy2(src, dst)

def deploy(mensagem: str = None):
    ts  = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    msg = mensagem or f"deploy: atualização automática — {ts}"

    print(f"\n🚀 DEPLOY AUTÔNOMO — {ts}")
    print("=" * 55)

    sincronizar_docs()
    run(["git", "remote", "set-url", "origin", REMOTE])

    ok, _, _ = run(["git", "add", "-A"])
    print(f"  stage:  ✅")

    _, status, _ = run(["git", "status", "--porcelain"])
    if not status:
        print("  commit: ⏭️  já atualizado")
    else:
        ok, out, err = run(["git", "commit", "-m", msg])
        linha = out.splitlines()[-1] if out else err
        print(f"  commit: {'✅' if ok else '❌'} {linha}")

    ok, out, err = run(["git", "push", "origin", "main"])
    print(f"  push:   {'✅ Enviado para GitHub' if ok else '❌ ' + err}")

    log = f"{LOG_DIR}/deploy_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(log, "w") as f:
        f.write(f"Data: {ts}\nMensagem: {msg}\nStatus: {'OK' if ok else 'ERRO'}\n{out}\n{err}")

    print(f"\n  Log:  {log}")
    print(f"  URL:  https://jurisperitus.com.br")
    print("=" * 55)
    return ok

if __name__ == "__main__":
    msg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    deploy(msg)
