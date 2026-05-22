#!/usr/bin/env python3
"""
PUBLICADOR DE BANNERS — TODAS AS REDES
Jurisperitus Escola Online | Claude Coworking
Publica o banner do dia no Facebook e YouTube comunidade.
Variáveis: FB_TOKEN, FB_PAGE_ID, YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN
"""

import os, sys, datetime, requests, json

hoje    = datetime.date.today()
DATA    = hoje.strftime("%d/%m")
PERIODO = os.environ.get("PERIODO", "manha")

FB_TOKEN    = os.environ.get("FB_TOKEN", "")
FB_PAGE_ID  = os.environ.get("FB_PAGE_ID", "")
YT_CLIENT   = os.environ.get("YOUTUBE_CLIENT_ID", "")
YT_SECRET   = os.environ.get("YOUTUBE_CLIENT_SECRET", "")
YT_REFRESH  = os.environ.get("YOUTUBE_REFRESH_TOKEN", "")

LOG = "resultado_banners.txt"

def log(msg):
    print(msg)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

# ─── CONTEÚDO ─────────────────────────────────────────────────────────────────
CALENDARIO = {
    "22/05": {
        "tema": "Gramática e Português",
        "manha":  "📚 DICA DE HOJE\n\nVocê comete esse erro todo dia?\n\nA diferença entre 'a fim de' e 'afim':\n— 'A fim de' = finalidade\n— 'Afim' = afinidade\n\nSimples assim. Mas 90% dos advogados erram nas petições.\n\n🔗 jurisperitus.com.br\n#jurisperitus #gramatica #OAB #direito #portugues",
        "tarde":  "💼 PRODUTO EM DESTAQUE\n\n📌 Corretor de Redações IA\n💰 R$ 19,90 por correção\n\nFeedback detalhado em segundos.\nIdeal para concurseiros e advogados.\n\n👉 jurisperitus.com.br\n#jurisperitus #OAB #concursopublico #redacao",
        "noite":  "🌙 REFLEXÃO DO DIA\n\nNo Direito, uma vírgula mal colocada pode mudar o sentido de uma sentença.\n\nDominar o Português é dominar o Direito.\n\n💬 Qual é sua maior dificuldade com a língua portuguesa?\n\n🔗 jurisperitus.com.br\n#jurisperitus #linguagemjuridica #direito",
    },
    "23/05": {
        "tema": "Linguagem Jurídica",
        "manha":  "📚 DICA DE HOJE\n\nExcelentíssimo ou Meritíssimo?\n\nSó para o Presidente da República e presidentes do Senado, Câmara e STF.\nPara juízes: Meritíssimo.\nPara demais autoridades: Vossa Excelência.\n\n🔗 jurisperitus.com.br\n#jurisperitus #linguagemjuridica #OAB #advogado",
        "tarde":  "💼 PRODUTO EM DESTAQUE\n\n📌 50 Prompts para Advogados\n💰 R$ 37 — acesso imediato\n\nUse a IA com segurança jurídica.\n50 comandos prontos para petições, pareceres e contratos.\n\n👉 jurisperitus.com.br\n#jurisperitus #IA #advogado #direito",
        "noite":  "🌙 REFLEXÃO DO DIA\n\nO advogado que fala bem convence antes de começar.\n\nTreine sua linguagem jurídica todos os dias.\n\n🔗 jurisperitus.com.br\n#jurisperitus #oratoria #linguagemjuridica #OAB",
    },
    "24/05": {
        "tema": "IA e Tecnologia no Direito",
        "manha":  "📚 DICA DE HOJE\n\nA IA já está no seu tribunal.\n\nEscriórios modernos usam IA para petições e pesquisa jurídica.\nMas atenção: IA erra. IA inventa jurisprudência.\n\nQuem domina o Português revisa melhor. Sempre.\n\n🔗 jurisperitus.com.br\n#jurisperitus #IA #direito #advogado",
        "tarde":  "💼 PRODUTO EM DESTAQUE\n\n📌 Analisador de TCC e Monografias\n💰 R$ 97 — resultado em minutos\n\nAnálise completa: ABNT, coesão, argumentação.\n\n👉 jurisperitus.com.br\n#jurisperitus #TCC #monografia #direito",
        "noite":  "🌙 REFLEXÃO DO DIA\n\nUm advogado usou IA para citar um acórdão.\nO número existia. O conteúdo? Inventado pela IA.\nO juiz percebeu. A ação foi arquivada.\n\nDomine a língua antes da tecnologia.\n\n🔗 jurisperitus.com.br\n#jurisperitus #IA #direito #advogado",
    },
    "25/05": {
        "tema": "Oratória e Comunicação",
        "manha":  "📚 DICA DE HOJE\n\nO erro que destrói sustentações orais:\n\nFalar rápido demais.\nRegra de ouro: 120 palavras por minuto.\nPause após cada argumento.\nO silêncio estratégico é sua arma mais poderosa.\n\n🔗 jurisperitus.com.br\n#jurisperitus #oratoria #OAB #advogado",
        "tarde":  "💼 PRODUTO EM DESTAQUE\n\n📌 Cartilha OAB 1ª Fase\n💰 R$ 47 — material completo\n\nTudo sobre linguagem jurídica para a OAB.\n\n👉 jurisperitus.com.br\n#jurisperitus #OAB #cartilha #direito",
        "noite":  "🌙 REFLEXÃO DO DIA\n\nAdvogados que falam devagar parecem mais seguros.\nParecem mais preparados.\nParecem — e são — mais convincentes.\n\n🔗 jurisperitus.com.br\n#jurisperitus #oratoria #comunicacao #OAB",
    },
    "26/05": {
        "tema": "Motivação e Mentalidade",
        "manha":  '📚 DICA DE HOJE\n\n⚔️ "Apenas dize uma palavra — e meu servo sarará."\n(Mt 8,8)\n\nO Centurião sabia o poder das palavras.\nVocê também sabe?\n\n🔗 jurisperitus.com.br\n#jurisperitus #motivacao #aprovacao #fe',
        "tarde":  "💼 PRODUTO EM DESTAQUE\n\n📌 Planner do Concurseiro\n💰 R$ 47 — organize seus estudos\n\nMetas, revisões e simulados em um só lugar.\n\n👉 jurisperitus.com.br\n#jurisperitus #concursopublico #planner #estudos",
        "noite":  "🌙 REFLEXÃO DO DIA\n\nSua aprovação não é uma questão de sorte.\nNem de genialidade.\nÉ de método, disciplina e linguagem.\n\nA Jurisperitus tem os três.\n\n🔗 jurisperitus.com.br\n#jurisperitus #aprovacao #metodo #concursopublico",
    },
    "27/05": {
        "tema": "Concursos OAB e Carreira",
        "manha":  "📚 DICA DE HOJE\n\nPor que candidatos que sabem o conteúdo reprovam?\n\nA redação vale até 30% da prova.\nFuga ao tema, falta de coesão e erros gramaticais custam a vaga.\n\nTreine sua redação agora.\n\n🔗 jurisperitus.com.br\n#jurisperitus #concursopublico #redacao #OAB",
        "tarde":  "💼 PRODUTO EM DESTAQUE\n\n📌 50 Prompts para Concurseiros\n💰 R$ 37 — acesso imediato\n\nEstude com IA de forma eficiente e segura.\n\n👉 jurisperitus.com.br\n#jurisperitus #concursopublico #IA #estudos",
        "noite":  "🌙 REFLEXÃO DO DIA\n\nO candidato que domina a língua portuguesa tem vantagem decisiva em qualquer concurso público.\n\nComece hoje.\n\n🔗 jurisperitus.com.br\n#jurisperitus #concursopublico #portugues #aprovacao",
    },
    "28/05": {
        "tema": "Gramática Avançada",
        "manha":  "📚 DICA DE HOJE\n\nCrase: o terror das petições.\n\nRegra prática: substitua por 'ao'.\nSe couber → usa crase.\nSe não couber → não usa.\n\n'Refiro-me à decisão' → 'Refiro-me ao decisão'? Não. Logo: crase.\n\n🔗 jurisperitus.com.br\n#jurisperitus #gramatica #crase #portugues #OAB",
        "tarde":  "💼 PRODUTO EM DESTAQUE\n\n📌 Cartilha de TCC\n💰 R$ 37 — guia completo\n\nDo projeto à defesa: normas ABNT, estrutura e argumentação.\n\n👉 jurisperitus.com.br\n#jurisperitus #TCC #ABNT #monografia",
        "noite":  '🌙 REFLEXÃO DO DIA\n\n"Não espere, amanhã será tarde."\n"Não espere amanhã, será tarde."\n\nA mesma frase. Dois sentidos opostos.\nNo Direito, uma vírgula pode mudar tudo.\n\n🔗 jurisperitus.com.br\n#jurisperitus #gramatica #virgula #direito',
    },
    "29/05": {
        "tema": "Redação Jurídica",
        "manha":  "📚 DICA DE HOJE\n\nA petição perfeita começa pela língua.\n\nClareza, precisão e coesão.\nSão os três pilares da redação jurídica.\n\nNão basta conhecer o Direito.\nÉ preciso saber escrever o Direito.\n\n🔗 jurisperitus.com.br\n#jurisperitus #redacaojuridica #peticao #advogado",
        "tarde":  "💼 PRODUTO EM DESTAQUE\n\n📌 Corretor de Redações IA\n💰 R$ 19,90 por correção\n\nFeedback detalhado em segundos.\nIdeal para concursos e OAB.\n\n👉 jurisperitus.com.br\n#jurisperitus #redacao #OAB #concursopublico",
        "noite":  "🌙 REFLEXÃO DO DIA\n\nO objetivo da redação jurídica não é impressionar.\nÉ comunicar com precisão.\n\nSimples, claro e correto.\n\n🔗 jurisperitus.com.br\n#jurisperitus #redacaojuridica #comunicacao #direito",
    },
    "30/05": {
        "tema": "Jurisperitus Escola Online",
        "manha":  "📚 JURISPERITUS\n\nA única escola online que une Português, Gramática e Linguagem Jurídica em um só lugar.\n\nCursos · E-books · Cartilhas · Produtos de IA\n\n🔗 jurisperitus.com.br\n#jurisperitus #escolaonline #direito #portugues #OAB",
        "tarde":  "💼 CONHEÇA NOSSOS PRODUTOS\n\n📌 Corretor de Redações IA — R$ 19,90\n📌 Analisador de TCC — R$ 97\n📌 Cartilha OAB — R$ 47\n📌 50 Prompts Advogados — R$ 37\n\n👉 jurisperitus.com.br\n#jurisperitus #produtosdigitais #direito #OAB",
        "noite":  "🌙 OBRIGADO\n\nCada dica, cada post, cada aula tinha um único objetivo:\n\nFazer você dominar a língua e conquistar sua aprovação.\n\nContinue. A Jurisperitus está com você.\n\n🔗 jurisperitus.com.br\n#jurisperitus #aprovacao #obrigado #comunidade",
    },
}

def get_texto():
    texto_data = CALENDARIO.get(DATA, {})
    if not texto_data:
        return f"Conteúdo Jurisperitus — {DATA}\n\n🔗 jurisperitus.com.br\n#jurisperitus #direito #OAB"
    return texto_data.get(PERIODO, "")

def get_banner():
    data_fmt = DATA.replace("/", "-")
    return f"banners/banner_{data_fmt}_{PERIODO}.jpg"

def publicar_facebook(texto, banner_path):
    if not FB_TOKEN or not FB_PAGE_ID:
        log("Facebook: credenciais não definidas")
        return False
    try:
        # Publicar com imagem via multipart
        url = f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}/photos"
        with open(banner_path, "rb") as img:
            r = requests.post(url, data={
                "caption": texto,
                "access_token": FB_TOKEN
            }, files={"source": img}, timeout=30)
        if r.status_code == 200:
            log(f"✅ Facebook: publicado! ID: {r.json().get('id','')}")
            return True
        else:
            log(f"❌ Facebook erro {r.status_code}: {r.text[:200]}")
            return False
    except Exception as e:
        log(f"❌ Facebook exceção: {e}")
        return False

def publicar_youtube_comunidade(texto):
    if not YT_CLIENT or not YT_SECRET or not YT_REFRESH:
        log("YouTube: credenciais não definidas")
        return False
    try:
        # Obter access token
        r = requests.post("https://oauth2.googleapis.com/token", data={
            "client_id": YT_CLIENT,
            "client_secret": YT_SECRET,
            "refresh_token": YT_REFRESH,
            "grant_type": "refresh_token"
        })
        if r.status_code != 200:
            log(f"❌ YouTube token erro: {r.text[:200]}")
            return False
        access_token = r.json().get("access_token")
        # Publicar post comunidade
        url = "https://www.googleapis.com/youtube/v3/communityPosts?part=snippet"
        resp = requests.post(url,
            headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
            json={"snippet": {"type": "TEXT_ONLY", "textOriginal": texto}},
            timeout=30)
        if resp.status_code in [200, 201]:
            log(f"✅ YouTube: publicado! ID: {resp.json().get('id','')}")
            return True
        else:
            log(f"❌ YouTube erro {resp.status_code}: {resp.text[:200]}")
            return False
    except Exception as e:
        log(f"❌ YouTube exceção: {e}")
        return False

if __name__ == "__main__":
    log(f"=== Publicador Banners {DATA} — {PERIODO.upper()} ===")

    banner = get_banner()
    texto  = get_texto()

    if not os.path.exists(banner):
        log(f"❌ Banner não encontrado: {banner}")
        sys.exit(1)

    log(f"Banner: {banner}")
    log(f"Texto: {len(texto)} chars")
    log("-" * 40)

    fb_ok = publicar_facebook(texto, banner)
    yt_ok = publicar_youtube_comunidade(texto)

    log("-" * 40)
    log(f"Facebook:  {'✅' if fb_ok else '❌'}")
    log(f"YouTube:   {'✅' if yt_ok else '❌'}")
    log("=== FIM ===")

    if not fb_ok and not yt_ok:
        sys.exit(1)
