#!/usr/bin/env python3
"""
PUBLICADOR INSTAGRAM — GITHUB ACTIONS
Jurisperitus Escola Online | Claude Coworking
"""
import os, sys, datetime, json
from pathlib import Path

LOG_FILE = "resultado_instagram.txt"

def log(msg):
    print(msg)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

USUARIO = os.environ.get("IG_USUARIO", "")
SENHA   = os.environ.get("IG_SENHA", "")
PERIODO = os.environ.get("PERIODO", "manha")
hoje    = datetime.date.today()

TEMAS = {
    0: "Gramatica e Portugues",
    1: "Linguagem Juridica",
    2: "IA e Tecnologia no Direito",
    3: "Oratoria e Comunicacao",
    4: "Mentalidade e Motivacao",
    5: "Concursos OAB e Carreira",
    6: "Bastidores e Comunidade",
}

PRODUTOS = [
    ("Corretor de Redacoes IA", "R$ 19,90"),
    ("50 Prompts para Advogados", "R$ 37"),
    ("Cartilha OAB 1a Fase", "R$ 47"),
    ("Analisador de TCC", "R$ 97"),
    ("Planner do Concurseiro", "R$ 47"),
    ("50 Prompts para Concurseiros", "R$ 37"),
    ("Cartilha de TCC", "R$ 37"),
]

HASHTAGS = ("#jurisperitus #linguagemjuridica #OAB #concursopublico "
            "#direito #advogado #gramatica #aprovacao #professorfreire")

dia      = hoje.weekday()
tema     = TEMAS.get(dia, "Portugues Juridico")
nomes    = ["Segunda","Terca","Quarta","Quinta","Sexta","Sabado","Domingo"]
nome_dia = nomes[dia]
produto  = PRODUTOS[dia % len(PRODUTOS)]

def gerar_legenda():
    if PERIODO == "manha":
        return (f"Dica de {nome_dia} - {hoje.strftime('%d/%m/%Y')}\n\n"
                f"Tema: {tema}\n\n"
                f"Todo profissional do Direito que domina a lingua portuguesa "
                f"tem uma vantagem decisiva.\n\n"
                f"Link na bio - jurisperitus.com.br\n\n{HASHTAGS}")
    elif PERIODO == "tarde":
        nome_prod, preco = produto
        return (f"Produto em destaque\n\n{nome_prod}\n{preco} - acesso imediato\n\n"
                f"Link na bio - jurisperitus.com.br\n\n{HASHTAGS}")
    else:
        return (f"Reflexao de {nome_dia}\n\n"
                f"A excelencia no Direito comeca pela excelencia na palavra.\n\n"
                f"jurisperitus.com.br\n\n{HASHTAGS}")

def gerar_imagem():
    try:
        from PIL import Image, ImageDraw, ImageFont
        import textwrap as tw

        W, H    = 1080, 1080
        AZUL    = (0, 59, 131)
        DOURADO = (255, 180, 0)
        BRANCO  = (255, 255, 255)

        img  = Image.new("RGB", (W, H), AZUL)
        draw = ImageDraw.Draw(img)
        draw.rectangle([20, 20, W-20, H-20], outline=DOURADO, width=6)
        draw.rectangle([0, 0, W, 120], fill=DOURADO)

        try:
            font_titulo = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
            font_corpo  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 38)
            font_pequena = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        except:
            font_titulo  = ImageFont.load_default()
            font_corpo   = font_titulo
            font_pequena = font_titulo

        draw.text((W//2, 60), "JURISPERITUS", font=font_titulo, fill=AZUL, anchor="mm")
        draw.text((W//2, 220), tema.upper(), font=font_corpo, fill=DOURADO, anchor="mm")

        linhas = tw.wrap(f"Dica de {nome_dia}", width=22)
        y = 340
        for linha in linhas:
            draw.text((W//2, y), linha, font=font_corpo, fill=BRANCO, anchor="mm")
            y += 70

        draw.text((W//2, 900), hoje.strftime("%d/%m/%Y"), font=font_pequena, fill=DOURADO, anchor="mm")
        draw.rectangle([0, H-80, W, H], fill=DOURADO)
        draw.text((W//2, H-40), "jurisperitus.com.br", font=font_pequena, fill=AZUL, anchor="mm")

        path = f"/tmp/card_{PERIODO}.jpg"
        img.save(path, "JPEG", quality=95)
        log(f"Imagem gerada: {path} ({os.path.getsize(path)} bytes)")
        return path

    except Exception as e:
        log(f"ERRO ao gerar imagem: {e}")
        return None

def publicar():
    if not USUARIO or not SENHA:
        log("ERRO: IG_USUARIO ou IG_SENHA nao definidos.")
        sys.exit(1)

    log(f"Usuario: @{USUARIO}")
    log(f"Periodo: {PERIODO}")

    try:
        from instagrapi import Client
        log("instagrapi importado OK")
    except Exception as e:
        log(f"ERRO importando instagrapi: {e}")
        sys.exit(1)

    cl = Client()
    cl.delay_range = [2, 5]

    try:
        log("Tentando login...")
        cl.login(USUARIO, SENHA)
        log("Login realizado com sucesso")
    except Exception as e:
        log(f"ERRO no login: {type(e).__name__}: {e}")
        sys.exit(1)

    legenda = gerar_legenda()
    log(f"Legenda gerada ({len(legenda)} chars)")

    imagem = gerar_imagem()
    if not imagem:
        log("ERRO: sem imagem para publicar")
        sys.exit(1)

    try:
        log("Publicando foto...")
        media = cl.photo_upload(imagem, legenda)
        log(f"PUBLICADO COM SUCESSO!")
        log(f"Media ID: {media.pk}")
        log(f"URL: https://instagram.com/p/{media.code}/")
    except Exception as e:
        log(f"ERRO ao publicar: {type(e).__name__}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    log(f"=== Instagram Action {hoje.strftime('%d/%m/%Y')} ({nome_dia}) ===")
    publicar()
    log("=== FIM ===")
