#!/usr/bin/env python3
"""
PUBLICADOR FACEBOOK — GITHUB ACTIONS
Jurisperitus Escola Online | Claude Coworking
Lê o conteúdo do dia e publica no Facebook via Graph API.
Variáveis de ambiente: FB_TOKEN, FB_PAGE_ID, PERIODO (manha/tarde/noite)
"""

import os, sys, datetime, requests, re

TOKEN   = os.environ.get("FB_TOKEN", "")
PAGE_ID = os.environ.get("FB_PAGE_ID", "")
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
    ("Corretor de Redações IA", "R$ 19,90/correção", "https://jurisperitus.com.br"),
    ("50 Prompts para Advogados", "R$ 37", "https://jurisperitus.com.br"),
    ("Cartilha OAB 1ª Fase", "R$ 47", "https://jurisperitus.com.br"),
    ("Analisador de TCC", "R$ 97", "https://jurisperitus.com.br"),
    ("Planner do Concurseiro", "R$ 47", "https://jurisperitus.com.br"),
    ("50 Prompts para Concurseiros", "R$ 37", "https://jurisperitus.com.br"),
    ("Cartilha de TCC", "R$ 37", "https://jurisperitus.com.br"),
]

HASHTAGS = "#jurisperitus #linguagemjuridica #OAB #concursopublico #direito #advogado #gramatica #aprovacao"

dia       = hoje.weekday()
tema      = TEMAS.get(dia, "Português Jurídico")
nomes_dia = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
nome_dia  = nomes_dia[dia]
produto   = PRODUTOS[dia % len(PRODUTOS)]


def gerar_texto_manha():
    return f"""📚 DICA DE {nome_dia.upper()} — {hoje.strftime('%d/%m/%Y')}

🎯 Tema: {tema}

Todo profissional do Direito que domina a língua portuguesa tem uma vantagem decisiva — na advocacia, nos concursos e na vida.

Hoje vamos falar sobre {tema.lower()}. Um dos pilares para quem quer se destacar no universo jurídico.

💡 Acompanhe nossa página para dicas diárias de Português e Linguagem Jurídica.

🔗 Acesse nossos cursos: jurisperitus.com.br

{HASHTAGS}"""


def gerar_texto_tarde():
    nome_prod, preco, link = produto
    return f"""💼 PRODUTO EM DESTAQUE

📌 {nome_prod}
💰 {preco} — acesso imediato

Desenvolvido especialmente para advogados, concurseiros e estudantes de Direito que querem dominar a linguagem jurídica com excelência.

👉 Acesse agora: {link}

{HASHTAGS} #hotmart #cursonline #produtodigital"""


def gerar_texto_noite():
    centurao = (dia == 4)
    ancora = (
        '\n\n⚔️ "Apenas dize uma palavra — e meu servo sarará." (Mt 8,8)\n'
        'O Centurião sabia o poder das palavras. Você também sabe?\n'
        if centurao else ""
    )
    return f"""🌙 REFLEXÃO DE {nome_dia.upper()}
{ancora}
A excelência no Direito começa pela excelência na palavra.

Quem domina o Português domina o argumento.
Quem domina o argumento domina o tribunal.

Continue estudando. A aprovação é uma questão de tempo e método. ⚖️

💬 Conta nos comentários: qual é sua maior dificuldade com a linguagem jurídica?

🔗 jurisperitus.com.br

{HASHTAGS} #motivacao #aprovacao #mentalidade"""


def publicar(texto, link=None):
    if not TOKEN or not PAGE_ID:
        print("ERRO: FB_TOKEN ou FB_PAGE_ID não definidos.")
        sys.exit(1)
    url     = f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
    payload = {"message": texto, "access_token": TOKEN}
    if link:
        payload["link"] = link
    r = requests.post(url, data=payload, timeout=30)
    return r.status_code, r.text


if __name__ == "__main__":
    print(f"Jurisperitus Facebook Action — {hoje.strftime('%d/%m/%Y')} ({nome_dia})")
    print(f"Período: {PERIODO} | Tema: {tema}")
    print("-" * 50)

    if PERIODO == "manha":
        texto = gerar_texto_manha()
        link  = "https://jurisperitus.com.br"
    elif PERIODO == "tarde":
        texto = gerar_texto_tarde()
        link  = produto[2]
    else:
        texto = gerar_texto_noite()
        link  = "https://jurisperitus.com.br"

    print("Texto a publicar:")
    print(texto)
    print("-" * 50)

    status, resp = publicar(texto, link)

    if status == 200:
        print(f"✅ PUBLICADO COM SUCESSO — Status {status}")
        print(f"Resposta: {resp}")
    else:
        print(f"❌ ERRO {status}: {resp}")
        sys.exit(1)
