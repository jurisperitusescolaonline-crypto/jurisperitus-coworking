#!/usr/bin/env python3
"""
PUBLICADOR YOUTUBE — GITHUB ACTIONS
Jurisperitus Escola Online | Claude Coworking
Publica posts na comunidade e faz upload de vídeos no YouTube.
Variáveis: YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN
"""

import os, sys, datetime, json, requests

CLIENT_ID     = os.environ.get("YOUTUBE_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("YOUTUBE_CLIENT_SECRET", "")
REFRESH_TOKEN = os.environ.get("YOUTUBE_REFRESH_TOKEN", "")
PERIODO       = os.environ.get("PERIODO", "manha")

hoje     = datetime.date.today()
dia      = hoje.weekday()
nomes    = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
nome_dia = nomes[dia]

TEMAS = {
    0: "Gramática e Português",
    1: "Linguagem Jurídica",
    2: "IA e Tecnologia no Direito",
    3: "Oratória e Comunicação",
    4: "Mentalidade e Motivação",
    5: "Concursos OAB e Carreira",
    6: "Bastidores e Comunidade",
}

PRODUTOS = [
    ("Corretor de Redações IA", "R$ 19,90", "https://jurisperitus.com.br"),
    ("50 Prompts para Advogados", "R$ 37", "https://jurisperitus.com.br"),
    ("Cartilha OAB 1ª Fase", "R$ 47", "https://jurisperitus.com.br"),
    ("Analisador de TCC", "R$ 97", "https://jurisperitus.com.br"),
    ("Planner do Concurseiro", "R$ 47", "https://jurisperitus.com.br"),
    ("50 Prompts para Concurseiros", "R$ 37", "https://jurisperitus.com.br"),
    ("Cartilha de TCC", "R$ 37", "https://jurisperitus.com.br"),
]

tema    = TEMAS.get(dia, "Português Jurídico")
produto = PRODUTOS[dia % len(PRODUTOS)]

LOG = "resultado_youtube.txt"

def log(msg):
    print(msg)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def obter_access_token():
    """Obtém access token usando o refresh token."""
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type":    "refresh_token"
    })
    if r.status_code == 200:
        token = r.json().get("access_token")
        log("Access token obtido com sucesso")
        return token
    else:
        log(f"ERRO ao obter token: {r.status_code} — {r.text[:200]}")
        sys.exit(1)

def gerar_texto_comunidade():
    if PERIODO == "manha":
        return (f"📚 DICA DE {nome_dia.upper()} — {hoje.strftime('%d/%m/%Y')}\n\n"
                f"🎯 Tema: {tema}\n\n"
                f"Todo profissional do Direito que domina a língua portuguesa "
                f"tem uma vantagem decisiva — na advocacia, nos concursos e na vida.\n\n"
                f"🔗 Acesse nossos cursos: jurisperitus.com.br\n\n"
                f"#jurisperitus #linguagemjuridica #OAB #direito #portugues")
    elif PERIODO == "tarde":
        nome_prod, preco, link = produto
        return (f"💼 PRODUTO EM DESTAQUE\n\n"
                f"📌 {nome_prod}\n💰 {preco} — acesso imediato\n\n"
                f"Desenvolvido para advogados, concurseiros e estudantes de Direito.\n\n"
                f"👉 {link}\n\n"
                f"#jurisperitus #hotmart #cursonline #direito")
    else:
        ancora = ('⚔️ "Apenas dize uma palavra — e meu servo sarará." (Mt 8,8)\n\n'
                  if dia == 4 else "")
        return (f"🌙 REFLEXÃO DE {nome_dia.upper()}\n\n{ancora}"
                f"A excelência no Direito começa pela excelência na palavra.\n\n"
                f"Quem domina o Português domina o argumento.\n"
                f"Quem domina o argumento domina o tribunal. ⚖️\n\n"
                f"💬 Qual é sua maior dificuldade com a linguagem jurídica?\n\n"
                f"🔗 jurisperitus.com.br\n\n"
                f"#jurisperitus #motivacao #aprovacao #direito")

def publicar_comunidade(access_token, texto):
    """Publica post na comunidade do YouTube."""
    url = "https://www.googleapis.com/youtube/v3/communityPosts?part=snippet"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    body = {
        "snippet": {
            "type": "TEXT_ONLY",
            "textOriginal": texto
        }
    }
    r = requests.post(url, headers=headers, json=body)
    if r.status_code in [200, 201]:
        post_id = r.json().get("id", "")
        log(f"✅ POST COMUNIDADE PUBLICADO!")
        log(f"   Post ID: {post_id}")
        return True
    else:
        log(f"❌ ERRO ao publicar comunidade: {r.status_code} — {r.text[:300]}")
        return False

def agendar_video(access_token, titulo, descricao, arquivo_video, horario_publicacao=None):
    """Faz upload de vídeo para o YouTube."""
    if not os.path.exists(arquivo_video):
        log(f"AVISO: arquivo de vídeo não encontrado: {arquivo_video}")
        return False

    url = "https://www.googleapis.com/upload/youtube/v3/videos?part=snippet,status"
    headers = {"Authorization": f"Bearer {access_token}"}

    status_video = "public"
    publish_at = None
    if horario_publicacao:
        status_video = "private"
        publish_at = horario_publicacao

    metadata = {
        "snippet": {
            "title": titulo,
            "description": descricao,
            "tags": ["jurisperitus", "linguagem juridica", "OAB", "direito", "portugues"],
            "categoryId": "27"  # Educação
        },
        "status": {
            "privacyStatus": status_video,
            "publishAt": publish_at
        }
    }

    with open(arquivo_video, "rb") as f:
        files = {
            "metadata": (None, json.dumps(metadata), "application/json"),
            "video":    (os.path.basename(arquivo_video), f, "video/*")
        }
        r = requests.post(url, headers=headers, files=files)

    if r.status_code in [200, 201]:
        video_id = r.json().get("id", "")
        log(f"✅ VÍDEO ENVIADO!")
        log(f"   Video ID: {video_id}")
        log(f"   URL: https://youtube.com/watch?v={video_id}")
        return True
    else:
        log(f"❌ ERRO no upload: {r.status_code} — {r.text[:300]}")
        return False

if __name__ == "__main__":
    log(f"=== YouTube Action {hoje.strftime('%d/%m/%Y')} ({nome_dia}) ===")
    log(f"Período: {PERIODO} | Tema: {tema}")
    log("-" * 40)

    if not CLIENT_ID or not CLIENT_SECRET or not REFRESH_TOKEN:
        log("ERRO: Credenciais YouTube não definidas.")
        sys.exit(1)

    access_token = obter_access_token()
    texto        = gerar_texto_comunidade()

    log(f"Texto gerado ({len(texto)} chars)")
    log("Publicando post na comunidade...")

    sucesso = publicar_comunidade(access_token, texto)

    if sucesso:
        log("=== CONCLUÍDO COM SUCESSO ===")
    else:
        log("=== FALHA NA PUBLICAÇÃO ===")
        sys.exit(1)
