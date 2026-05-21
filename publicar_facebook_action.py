#!/usr/bin/env python3
"""
PUBLICADOR FACEBOOK — GITHUB ACTIONS
Jurisperitus Escola Online | Claude Coworking
"""
import os, sys, datetime, requests, json

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
    return (f"📚 DICA DE {nome_dia.upper()} — {hoje.strftime('%d/%m/%Y')}\n\n"
            f"🎯 Tema: {tema}\n\n"
            "Todo profissional do Direito que domina a língua portuguesa tem uma vantagem "
            "decisiva — na advocacia, nos concursos e na vida.\n\n"
            f"Hoje: {tema.lower()}. Um dos pilares para quem quer se destacar no universo jurídico.\n\n"
            "💡 Acompanhe nossa página para dicas diárias de Português e Linguagem Jurídica.\n\n"
            "🔗 jurisperitus.com.br\n\n" + HASHTAGS)

def gerar_texto_tarde():
    nome_prod, preco, link = produto
    return (f"💼 PRODUTO EM DESTAQUE\n\n📌 {nome_prod}\n💰 {preco} — acesso imediato\n\n"
            "Desenvolvido para advogados, concurseiros e estudantes de Direito que querem "
            "dominar a linguagem jurídica com excelência.\n\n"
            f"👉 Acesse: {link}\n\n" + HASHTAGS + " #hotmart #cursonline")

def gerar_texto_noite():
    ancora = ('\n\n⚔️ "Apenas dize uma palavra — e meu servo sarará." (Mt 8,8)\n'
              'O Centurião sabia o poder das palavras. Você também sabe?\n'
              if dia == 4 else "")
    return (f"🌙 REFLEXÃO DE {nome_dia.upper()}{ancora}\n\n"
            "A excelência no Direito começa pela excelência na palavra.\n\n"
            "Quem domina o Português domina o argumento.\n"
            "Quem domina o argumento domina o tribunal. ⚖️\n\n"
            "💬 Qual é sua maior dificuldade com a linguagem jurídica?\n\n"
            "🔗 jurisperitus.com.br\n\n" + HASHTAGS + " #motivacao #aprovacao")

def publicar(texto, link=None):
    if not TOKEN or not PAGE_ID:
        print("ERRO: FB_TOKEN ou FB_PAGE_ID não definidos nos segredos.")
        sys.exit(1)
    print(f"Page ID: {PAGE_ID}")
    print(f"Token (primeiros 20 chars): {TOKEN[:20]}...")
    url     = f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
    payload = {"message": texto, "access_token": TOKEN}
    if link:
        payload["link"] = link
    r = requests.post(url, data=payload, timeout=30)
    print(f"HTTP Status: {r.status_code}")
    print(f"Resposta: {r.text[:500]}")
    return r.status_code, r.text

if __name__ == "__main__":
    print(f"=== Jurisperitus Facebook Action ===")
    print(f"Data: {hoje.strftime('%d/%m/%Y')} ({nome_dia})")
    print(f"Período: {PERIODO} | Tema: {tema}")
    print("-" * 40)
    if PERIODO == "manha":
        texto, link = gerar_texto_manha(), "https://jurisperitus.com.br"
    elif PERIODO == "tarde":
        texto, link = gerar_texto_tarde(), produto[2]
    else:
        texto, link = gerar_texto_noite(), "https://jurisperitus.com.br"
    print(f"Texto gerado ({len(texto)} chars)")
    print("-" * 40)
    status, resp = publicar(texto, link)
    if status == 200:
        resp_json = json.loads(resp)
        print(f"\n✅ PUBLICADO COM SUCESSO!")
        print(f"Post ID: {resp_json.get('id','')}")
    else:
        print(f"\n❌ FALHA NA PUBLICAÇÃO — Status {status}")
        sys.exit(1)
