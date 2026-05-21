#!/usr/bin/env python3
"""
PUBLICADOR INSTAGRAM — GITHUB ACTIONS
Jurisperitus Escola Online | Claude Coworking
Publica posts de texto+imagem no Instagram via instagrapi.
Variáveis: IG_USUARIO, IG_SENHA, PERIODO
"""

import os, sys, datetime, json, textwrap
from pathlib import Path

USUARIO = os.environ.get("IG_USUARIO", "")
SENHA   = os.environ.get("IG_SENHA", "")
PERIODO = os.environ.get("PERIODO", "manha")
hoje    = datetime.date.today()

TEMAS = {
    0: "Gramática / Português",
    1: "Linguagem Jurídica",
    2: "IA & Tecnologia no Direito",
    3: "Oratória / Comunicação",
    4: "Mentalidade / Motivação",
    5: "Concursos / OAB / Carreira",
    6: "Bastidores / Comunidade",
}

PRODUTOS = [
    ("Corretor de Redações IA", "R$ 19,90"),
    ("50 Prompts para Advogados", "R$ 37"),
    ("Cartilha OAB 1ª Fase", "R$ 47"),
    ("Analisador de TCC", "R$ 97"),
    ("Planner do Concurseiro", "R$ 47"),
    ("50 Prompts para Concurseiros", "R$ 37"),
    ("Cartilha de TCC", "R$ 37"),
]

HASHTAGS = ("#jurisperitus #linguagemjuridica #OAB #concursopublico "
            "#direito #advogado #gramatica #aprovacao #professorfreire")

dia      = hoje.weekday()
tema     = TEMAS.get(dia, "Português Jurídico")
nomes    = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
nome_dia = nomes[dia]
produto  = PRODUTOS[dia % len(PRODUTOS)]


def gerar_legenda_manha():
    return (f"📚 DICA DE {nome_dia.upper()} — {hoje.strftime('%d/%m/%Y')}\n\n"
            f"🎯 Tema: {tema}\n\n"
            f"Todo profissional do Direito que domina a língua portuguesa "
            f"tem uma vantagem decisiva — na advocacia, nos concursos e na vida.\n\n"
            f"Salva esse post para consultar depois! 📌\n\n"
            f"🔗 Link na bio → jurisperitus.com.br\n\n"
            f"{HASHTAGS}")

def gerar_legenda_tarde():
    nome_prod, preco = produto
    return (f"💼 PRODUTO EM DESTAQUE\n\n"
            f"📌 {nome_prod}\n"
            f"💰 {preco} — acesso imediato\n\n"
            f"Desenvolvido para advogados, concurseiros e estudantes de Direito "
            f"que querem dominar a linguagem jurídica com excelência.\n\n"
            f"👉 Link na bio → jurisperitus.com.br\n\n"
            f"{HASHTAGS} #hotmart #cursonline")

def gerar_legenda_noite():
    ancora = ('\n⚔️ "Apenas dize uma palavra — e meu servo sarará." (Mt 8,8)\n'
              if dia == 4 else "")
    return (f"🌙 REFLEXÃO DE {nome_dia.upper()}{ancora}\n\n"
            f"A excelência no Direito começa pela excelência na palavra.\n\n"
            f"Quem domina o Português domina o argumento.\n"
            f"Quem domina o argumento domina o tribunal. ⚖️\n\n"
            f"💬 Qual é sua maior dificuldade com a linguagem jurídica?\n\n"
            f"🔗 jurisperitus.com.br\n\n"
            f"{HASHTAGS} #motivacao #aprovacao")


def gerar_imagem_card(texto_principal, periodo):
    """Gera imagem simples com Pillow nas cores da Jurisperitus."""
    try:
        from PIL import Image, ImageDraw, ImageFont
        import textwrap

        W, H   = 1080, 1080
        AZUL   = (0, 59, 131)       # #003B83
        DOURADO = (255, 180, 0)     # #FFB400
        BRANCO = (255, 255, 255)

        img  = Image.new("RGB", (W, H), AZUL)
        draw = ImageDraw.Draw(img)

        # Borda dourada
        draw.rectangle([20, 20, W-20, H-20], outline=DOURADO, width=6)

        # Topo — logo texto
        draw.rectangle([0, 0, W, 120], fill=DOURADO)
        try:
            font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
            font_body  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        except:
            font_title = ImageFont.load_default()
            font_body  = font_title
            font_small = font_title

        draw.text((W//2, 60), "JURISPERITUS", font=font_title, fill=AZUL, anchor="mm")

        # Tema
        draw.text((W//2, 200), tema.upper(), font=font_body, fill=DOURADO, anchor="mm")

        # Texto principal — quebrado em linhas
        linhas = textwrap.wrap(texto_principal, width=28)
        y = 320
        for linha in linhas[:8]:
            draw.text((W//2, y), linha, font=font_body, fill=BRANCO, anchor="mm")
            y += 60

        # Data
        draw.text((W//2, 900), hoje.strftime("%d/%m/%Y"), font=font_small, fill=DOURADO, anchor="mm")

        # Rodapé
        draw.rectangle([0, H-80, W, H], fill=DOURADO)
        draw.text((W//2, H-40), "jurisperitus.com.br", font=font_small, fill=AZUL, anchor="mm")

        path = f"/tmp/card_instagram_{periodo}.jpg"
        img.save(path, "JPEG", quality=95)
        print(f"✅ Imagem gerada: {path}")
        return path

    except Exception as e:
        print(f"⚠️  Erro ao gerar imagem: {e}")
        return None


def publicar_instagram(legenda, imagem_path):
    """Publica no Instagram via instagrapi."""
    if not USUARIO or not SENHA:
        print("ERRO: IG_USUARIO ou IG_SENHA não definidos.")
        sys.exit(1)

    from instagrapi import Client

    print(f"Conectando como @{USUARIO}...")
    cl = Client()
    cl.delay_range = [2, 5]

    # Tentar carregar sessão salva
    session_file = "/tmp/ig_session.json"
    if Path(session_file).exists():
        try:
            cl.load_settings(session_file)
            cl.login(USUARIO, SENHA)
            print("✅ Sessão restaurada")
        except:
            cl.login(USUARIO, SENHA)
            print("✅ Login realizado")
    else:
        cl.login(USUARIO, SENHA)
        print("✅ Login realizado")

    cl.dump_settings(session_file)

    if imagem_path and Path(imagem_path).exists():
        media = cl.photo_upload(imagem_path, legenda)
        print(f"✅ POST PUBLICADO!")
        print(f"   Media ID: {media.pk}")
        print(f"   Ver em: https://instagram.com/p/{media.code}/")
        return True
    else:
        print("❌ Imagem não encontrada — necessária para publicar no feed.")
        return False


if __name__ == "__main__":
    print(f"=== Jurisperitus Instagram Action ===")
    print(f"Data: {hoje.strftime('%d/%m/%Y')} ({nome_dia})")
    print(f"Período: {PERIODO} | Tema: {tema}")
    print("-" * 40)

    if PERIODO == "manha":
        legenda       = gerar_legenda_manha()
        texto_card    = f"DICA DE {nome_dia.upper()}\n\n{tema}"
    elif PERIODO == "tarde":
        legenda       = gerar_legenda_tarde()
        texto_card    = f"{produto[0]}\n\n{produto[1]}"
    else:
        legenda       = gerar_legenda_noite()
        texto_card    = f"REFLEXÃO DE\n{nome_dia.upper()}"

    imagem = gerar_imagem_card(texto_card, PERIODO)
    print(f"Legenda gerada ({len(legenda)} chars)")
    print("-" * 40)

    sucesso = publicar_instagram(legenda, imagem)
    if not sucesso:
        sys.exit(1)
