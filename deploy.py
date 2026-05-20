#!/usr/bin/env python3
"""
DEPLOY AUTÔNOMO — CLAUDE COWORKING JURISPERITUS
Executa deploys no Netlify diretamente desta máquina.
Requer: NETLIFY_AUTH_TOKEN configurado em .env ou variável de ambiente.
"""

import os, subprocess, sys, datetime

# ── Configuração ──────────────────────────────────────────────
PROJETOS = {
    "jurisperitus-main": {
        "site_id": "77388af4-3a4f-4aa1-97be-f0405c14343c",
        "dir":     "/home/claude/jurisperitus/OS-ativas/netlify-deploy",
        "dominio": "jurisperitus.com.br",
    },
    # Adicionar demais projetos após obter site IDs:
    # "jurisperitus-tutor": {
    #     "site_id": "SEU_SITE_ID",
    #     "dir":     "/home/claude/jurisperitus/cursos/tutor",
    #     "dominio": "jurisperitus.com.br/tutor",
    # },
}

LOG = "/home/claude/jurisperitus/relatorios"
os.makedirs(LOG, exist_ok=True)

def deploy(projeto: str, producao: bool = True):
    cfg = PROJETOS.get(projeto)
    if not cfg:
        print(f"❌ Projeto '{projeto}' não encontrado.")
        return False

    token = os.environ.get("NETLIFY_AUTH_TOKEN")
    if not token:
        print("❌ NETLIFY_AUTH_TOKEN não configurado.")
        print("   Execute: export NETLIFY_AUTH_TOKEN=seu_token")
        print("   Gere o token em: app.netlify.com → User settings → Applications → Personal access tokens")
        return False

    flag = "--prod" if producao else ""
    cmd = [
        "netlify", "deploy",
        "--dir", cfg["dir"],
        "--site", cfg["site_id"],
        "--auth", token,
        "--message", f"Deploy automático Claude Coworking — {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}",
    ]
    if producao:
        cmd.append("--prod")

    print(f"\n🚀 Iniciando deploy: {projeto}")
    print(f"   Diretório: {cfg['dir']}")
    print(f"   Domínio:   {cfg['dominio']}")
    print(f"   Produção:  {'Sim' if producao else 'Preview'}\n")

    result = subprocess.run(cmd, capture_output=True, text=True)

    # Log
    log_file = f"{LOG}/deploy_{projeto}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(log_file, "w") as f:
        f.write(f"Projeto: {projeto}\n")
        f.write(f"Data: {datetime.datetime.now()}\n")
        f.write(f"Status: {'SUCESSO' if result.returncode == 0 else 'ERRO'}\n\n")
        f.write(result.stdout)
        if result.stderr:
            f.write("\nSTDERR:\n" + result.stderr)

    if result.returncode == 0:
        print(f"✅ Deploy concluído! Log: {log_file}")
        print(result.stdout)
        return True
    else:
        print(f"❌ Erro no deploy. Log: {log_file}")
        print(result.stderr)
        return False


if __name__ == "__main__":
    projeto = sys.argv[1] if len(sys.argv) > 1 else "jurisperitus-main"
    prod    = "--preview" not in sys.argv
    deploy(projeto, producao=prod)
