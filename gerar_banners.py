#!/usr/bin/env python3
"""
GERADOR DE BANNERS — JURISPERITUS
22 a 30 de maio de 2026
Gera banners 1080x1080 para Facebook, Instagram, YouTube e TikTok
3 posts por dia: manhã, tarde e noite
"""

from PIL import Image, ImageDraw, ImageFont
import os, datetime, textwrap

# ─── CORES JURISPERITUS ───────────────────────────────────────────────────────
AZUL    = (0, 59, 131)
DOURADO = (255, 180, 0)
BRANCO  = (255, 255, 255)
CINZA   = (220, 220, 220)

# ─── FONTES ───────────────────────────────────────────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
def fonte(tamanho, negrito=False):
    try:
        arq = "DejaVuSans-Bold.ttf" if negrito else "DejaVuSans.ttf"
        return ImageFont.truetype(FONT_DIR + arq, tamanho)
    except:
        return ImageFont.load_default()

# ─── CALENDÁRIO DE CONTEÚDO ───────────────────────────────────────────────────
CALENDARIO = {
    "22/05": {
        "tema":    "Gramática e Português",
        "manha":   ("Você comete esse erro todo dia", "A diferença entre 'a fim de' e 'afim'.\n'A fim de' = finalidade.\n'Afim' = afinidade.\nSimples assim."),
        "tarde":   ("Corretor de Redações IA", "Corrija sua redação agora.\nFeedback em segundos.\nR$ 19,90 por correção.\njurisperitus.com.br"),
        "noite":   ("A palavra certa abre portas", "No Direito, uma vírgula mal colocada\npode mudar o sentido de uma sentença.\nDominar o Português é dominar o Direito."),
    },
    "23/05": {
        "tema":    "Linguagem Jurídica",
        "manha":   ("Excelentíssimo ou Meritíssimo?", "Só para o Presidente da República\ne presidentes do Senado, Câmara e STF.\nPara juízes: Meritíssimo.\nPara demais: Vossa Excelência."),
        "tarde":   ("50 Prompts para Advogados", "Use a IA com segurança jurídica.\n50 comandos prontos para petições,\npareceres e contratos.\nR$ 37 — acesso imediato."),
        "noite":   ("Linguagem é poder", "O advogado que fala bem\nconvence antes de começar.\nTreine sua linguagem jurídica."),
    },
    "24/05": {
        "tema":    "IA e Tecnologia no Direito",
        "manha":   ("A IA já está no seu tribunal", "Escritórios modernos usam IA\npara petições e pesquisa jurídica.\nMas atenção: IA erra. Revise sempre.\nQuem domina o Português revisa melhor."),
        "tarde":   ("Analisador de TCC e Monografias", "Análise completa do seu trabalho.\nFormatação ABNT, coesão, argumentação.\nR$ 97 — resultado em minutos.\njurisperitus.com.br"),
        "noite":   ("Tecnologia sem língua é perigosa", "Um advogado usou IA para citar acórdão.\nO número existia. O conteúdo? Inventado.\nO juiz percebeu. Caso arquivado.\nDomine a língua antes da tecnologia."),
    },
    "25/05": {
        "tema":    "Oratória e Comunicação",
        "manha":   ("O erro que destrói sustentações orais", "Falar rápido demais.\nRegra de ouro: 120 palavras por minuto.\nPause após cada argumento.\nO silêncio é sua arma mais poderosa."),
        "tarde":   ("Cartilha OAB 1ª Fase", "Tudo que você precisa saber\nsobre linguagem jurídica para a OAB.\nR$ 47 — material completo.\njurisperitus.com.br"),
        "noite":   ("Fale menos. Convença mais.", "Advogados que falam devagar\nparecem mais seguros.\nParecem mais preparados.\nParecem — e são — mais convincentes."),
    },
    "26/05": {
        "tema":    "Motivação e Mentalidade",
        "manha":   ("Apenas dize uma palavra", '"Apenas dize uma palavra —\ne meu servo sarará."\n(Mt 8,8)\nO Centurião sabia o poder das palavras.'),
        "tarde":   ("Planner do Concurseiro", "Organize sua rotina de estudos.\nMetas, revisões e simulados.\nTudo em um só lugar.\nR$ 47 — comece hoje."),
        "noite":   ("Sua aprovação é uma questão de método", "Não de sorte.\nNão de genialidade.\nDe método, disciplina e linguagem.\nA Jurisperitus tem os três."),
    },
    "27/05": {
        "tema":    "Concursos OAB e Carreira",
        "manha":   ("Por que candidatos aprovados reprovam?", "A redação vale até 30% da prova.\nFuga ao tema, falta de coesão\ne erros gramaticais custam a vaga.\nTreine sua redação agora."),
        "tarde":   ("50 Prompts para Concurseiros", "Comandos prontos para estudar\ncom IA de forma eficiente.\nR$ 37 — acesso imediato.\njurisperitus.com.br"),
        "noite":   ("A vaga existe. A questão é quem chega lá.", "O candidato que domina\na língua portuguesa\ntem vantagem decisiva\nem qualquer concurso público."),
    },
    "28/05": {
        "tema":    "Gramática Avançada",
        "manha":   ("Crase: o terror das petições", "Usa-se crase antes de palavras femininas\nque aceitam o artigo 'a'.\nTeste: substitua por 'ao'.\nSe couber, usa crase. Se não couber, não usa."),
        "tarde":   ("Cartilha de TCC", "Do projeto à defesa.\nNormas ABNT, estrutura e argumentação.\nR$ 37 — guia completo.\njurisperitus.com.br"),
        "noite":   ("Uma vírgula muda tudo", '"Não espere, amanhã será tarde."\n"Não espere amanhã, será tarde."\nA mesma frase. Dois sentidos opostos.\nNo Direito, isso pode mudar tudo.'),
    },
    "29/05": {
        "tema":    "Redação Jurídica",
        "manha":   ("A petição perfeita começa pela língua", "Clareza, precisão e coesão.\nSão os três pilares da redação jurídica.\nNão basta conhecer o Direito.\nÉ preciso saber escrever o Direito."),
        "tarde":   ("Corretor de Redações IA", "Corrija sua redação agora.\nFeedback detalhado em segundos.\nR$ 19,90 por correção.\njurisperitus.com.br"),
        "noite":   ("Escreva para ser entendido", "O objetivo da redação jurídica\nnão é impressionar.\nÉ comunicar com precisão.\nSimples, claro e correto."),
    },
    "30/05": {
        "tema":    "Jurisperitus — Escola Online",
        "manha":   ("Jurisperitus: português e direito", "A única escola online que une\nPortuguês, Gramática e Linguagem Jurídica\nem um só lugar.\nConheça em jurisperitus.com.br"),
        "tarde":   ("Nossos produtos digitais", "Cursos · E-books · Cartilhas\nCorretor de Redações IA\nAnalisador de TCC\nTudo em jurisperitus.com.br"),
        "noite":   ("Obrigado por nos acompanhar", "Cada dica, cada post, cada aula\ntinha um único objetivo:\nfazer você dominar a língua\ne conquistar sua aprovação."),
    },
}

HASHTAGS = "#jurisperitus #linguagemjuridica #OAB #direito #portugues #advogado #aprovacao"

def gerar_banner(titulo, corpo, periodo, data_str, tema, pasta_saida):
    """Gera um banner 1080x1080 nas cores da Jurisperitus."""

    W, H = 1080, 1080
    img  = Image.new("RGB", (W, H), AZUL)
    draw = ImageDraw.Draw(img)

    # Borda dourada
    draw.rectangle([15, 15, W-15, H-15], outline=DOURADO, width=8)

    # Cabeçalho dourado
    draw.rectangle([0, 0, W, 110], fill=DOURADO)
    draw.text((W//2, 55), "JURISPERITUS", font=fonte(54, True), fill=AZUL, anchor="mm")

    # Tema (subtítulo do cabeçalho)
    draw.rectangle([0, 110, W, 160], fill=(0, 45, 100))
    draw.text((W//2, 135), tema.upper(), font=fonte(28), fill=DOURADO, anchor="mm")

    # Período
    periodos = {"manha": "☀ MANHÃ", "tarde": "☀ TARDE", "noite": "🌙 NOITE"}
    label = periodos.get(periodo, periodo.upper())
    draw.text((W//2, 200), label, font=fonte(32, True), fill=DOURADO, anchor="mm")

    # Título
    linhas_titulo = textwrap.wrap(titulo, width=24)
    y = 270
    for linha in linhas_titulo[:3]:
        draw.text((W//2, y), linha, font=fonte(52, True), fill=BRANCO, anchor="mm")
        y += 68

    # Linha separadora
    draw.rectangle([80, y+10, W-80, y+14], fill=DOURADO)
    y += 40

    # Corpo
    linhas_corpo = []
    for paragrafo in corpo.split("\n"):
        linhas_corpo.extend(textwrap.wrap(paragrafo, width=32) or [""])
    for linha in linhas_corpo[:7]:
        draw.text((W//2, y), linha, font=fonte(36), fill=CINZA, anchor="mm")
        y += 52

    # Data
    draw.text((W//2, 880), data_str, font=fonte(28), fill=DOURADO, anchor="mm")

    # Hashtags
    draw.text((W//2, 925), HASHTAGS[:55], font=fonte(22), fill=(180, 180, 180), anchor="mm")

    # Rodapé
    draw.rectangle([0, H-80, W, H], fill=DOURADO)
    draw.text((W//2, H-40), "jurisperitus.com.br", font=fonte(34, True), fill=AZUL, anchor="mm")

    # Salvar
    nome_arquivo = f"{pasta_saida}/banner_{data_str.replace('/','-')}_{periodo}.jpg"
    img.save(nome_arquivo, "JPEG", quality=95)
    return nome_arquivo

# ─── GERAR TODOS OS BANNERS ───────────────────────────────────────────────────
if __name__ == "__main__":
    pasta = "/root/jurisperitus-banners"
    os.makedirs(pasta, exist_ok=True)

    total = 0
    for data_str, conteudo in CALENDARIO.items():
        tema = conteudo["tema"]
        for periodo in ["manha", "tarde", "noite"]:
            titulo, corpo = conteudo[periodo]
            arquivo = gerar_banner(titulo, corpo, periodo, data_str, tema, pasta)
            print(f"✅ {arquivo.split('/')[-1]}")
            total += 1

    print(f"\n=== {total} banners gerados em {pasta} ===")
