#!/usr/bin/env python3
"""
GERADOR DE FILA INSTAGRAM — GOOGLE SHEETS
Jurisperitus Escola Online | Claude Coworking
Gera conteúdo do dia e salva numa planilha Google Sheets.
O Zapier monitora a planilha e publica no Instagram.
Variáveis: GOOGLE_SHEETS_ID, GOOGLE_CREDENTIALS_JSON
"""
import os, sys, datetime, json

hoje     = datetime.date.today()
agora    = datetime.datetime.now()
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

tema     = TEMAS.get(dia, "Português Jurídico")
produto  = PRODUTOS[dia % len(PRODUTOS)]

def gerar_posts():
    posts = []

    # Manhã
    posts.append({
        "data":     hoje.strftime("%d/%m/%Y"),
        "horario":  "07:00",
        "periodo":  "manha",
        "legenda":  (f"📚 DICA DE {nome_dia.upper()} — {hoje.strftime('%d/%m/%Y')}\n\n"
                    f"🎯 Tema: {tema}\n\n"
                    f"Todo profissional do Direito que domina a língua portuguesa "
                    f"tem uma vantagem decisiva — na advocacia, nos concursos e na vida.\n\n"
                    f"Salva esse post! 📌\n\n"
                    f"🔗 Link na bio → jurisperitus.com.br\n\n{HASHTAGS}"),
        "status":   "pendente",
        "gerado_em": agora.strftime("%d/%m/%Y %H:%M"),
    })

    # Tarde
    nome_prod, preco = produto
    posts.append({
        "data":     hoje.strftime("%d/%m/%Y"),
        "horario":  "12:00",
        "periodo":  "tarde",
        "legenda":  (f"💼 PRODUTO EM DESTAQUE\n\n"
                    f"📌 {nome_prod}\n💰 {preco} — acesso imediato\n\n"
                    f"Para advogados, concurseiros e estudantes de Direito "
                    f"que querem dominar a linguagem jurídica.\n\n"
                    f"👉 Link na bio → jurisperitus.com.br\n\n{HASHTAGS} #hotmart #cursonline"),
        "status":   "pendente",
        "gerado_em": agora.strftime("%d/%m/%Y %H:%M"),
    })

    # Noite
    ancora = ('⚔️ "Apenas dize uma palavra — e meu servo sarará." (Mt 8,8)\n\n'
              if dia == 4 else "")
    posts.append({
        "data":     hoje.strftime("%d/%m/%Y"),
        "horario":  "19:00",
        "periodo":  "noite",
        "legenda":  (f"🌙 REFLEXÃO DE {nome_dia.upper()}\n\n{ancora}"
                    f"A excelência no Direito começa pela excelência na palavra.\n\n"
                    f"Quem domina o Português domina o argumento.\n"
                    f"Quem domina o argumento domina o tribunal. ⚖️\n\n"
                    f"💬 Qual é sua maior dificuldade com a linguagem jurídica?\n\n"
                    f"🔗 jurisperitus.com.br\n\n{HASHTAGS} #motivacao #aprovacao"),
        "status":   "pendente",
        "gerado_em": agora.strftime("%d/%m/%Y %H:%M"),
    })

    return posts

def salvar_sheets(posts):
    """Salva os posts na planilha Google Sheets via API."""
    sheets_id = os.environ.get("GOOGLE_SHEETS_ID", "")
    creds_json = os.environ.get("GOOGLE_CREDENTIALS_JSON", "")

    if not sheets_id or not creds_json:
        print("AVISO: GOOGLE_SHEETS_ID ou GOOGLE_CREDENTIALS_JSON não definidos.")
        print("Salvando localmente em fila_instagram.json")
        with open("fila_instagram.json", "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
        return False

    try:
        import google.oauth2.service_account as sa
        from googleapiclient.discovery import build

        creds_dict = json.loads(creds_json)
        creds = sa.Credentials.from_service_account_info(
            creds_dict,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        service = build("sheets", "v4", credentials=creds)
        sheet   = service.spreadsheets()

        # Cabeçalho se planilha estiver vazia
        header = [["Data", "Horário", "Período", "Legenda", "Status", "Gerado em"]]
        valores = [[p["data"], p["horario"], p["periodo"],
                    p["legenda"], p["status"], p["gerado_em"]] for p in posts]

        sheet.values().append(
            spreadsheetId=sheets_id,
            range="Fila!A1",
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body={"values": valores}
        ).execute()

        print(f"✅ {len(posts)} posts adicionados à planilha Google Sheets")
        return True

    except Exception as e:
        print(f"ERRO ao salvar no Sheets: {e}")
        return False

if __name__ == "__main__":
    print(f"Gerando fila Instagram — {hoje.strftime('%d/%m/%Y')} ({nome_dia})")
    print(f"Tema: {tema}")
    posts = gerar_posts()
    salvar_sheets(posts)
    print(f"✅ {len(posts)} posts gerados")
    for p in posts:
        print(f"  {p['horario']} — {p['periodo']}: {len(p['legenda'])} chars")
