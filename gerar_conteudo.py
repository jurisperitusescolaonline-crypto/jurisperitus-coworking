#!/usr/bin/env python3
"""
GERADOR DE CONTEÚDO DIÁRIO — JURISPERITUS
Gera os 3 pacotes (manhã/tarde/noite) para todas as plataformas.
Execução: python3 gerar_conteudo.py
"""

import datetime, os, sys

BASE    = "/home/claude/jurisperitus"
SAIDA   = f"{BASE}/conteudo-diario"
hoje    = datetime.date.today()
dia     = hoje.weekday()  # 0=Seg
nomes   = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
nome    = nomes[dia]

TEMAS = {
    "Segunda":  ("Gramática / Português",      "concurseiros e advogados"),
    "Terça":    ("Linguagem Jurídica",           "advogados e OAB"),
    "Quarta":   ("IA & Tecnologia no Direito",   "todos os públicos"),
    "Quinta":   ("Oratória / Comunicação",       "advogados e concurseiros"),
    "Sexta":    ("Mentalidade / Motivação",      "todos"),
    "Sábado":   ("Concursos / OAB / Carreira",   "concurseiros"),
    "Domingo":  ("Bastidores / Comunidade",      "todos"),
}

PRODUTOS_ROTACAO = [
    ("Corretor de Redações IA", "R$ 19,90/correção"),
    ("50 Prompts para Advogados", "R$ 37"),
    ("Cartilha OAB 1ª Fase", "R$ 47"),
    ("Planner do Concurseiro", "R$ 47"),
    ("Analisador de TCC", "R$ 97"),
    ("50 Prompts para Concurseiros", "R$ 37"),
    ("Cartilha de TCC", "R$ 37"),
    ("Calculadora de Edital", "R$ 27"),
]

tema, publico = TEMAS.get(nome, ("Conteúdo Jurídico", "todos"))
produto_dia   = PRODUTOS_ROTACAO[dia % len(PRODUTOS_ROTACAO)]

HASHTAGS = "#jurisperitus #linguagemjuridica #OAB #concursopublico #direito #advogado #gramatica #aprovacao"

def salvar(pasta, nome_arq, conteudo):
    os.makedirs(pasta, exist_ok=True)
    caminho = f"{pasta}/{nome_arq}"
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)
    return caminho

def gerar_manha():
    return f"""# CONTEÚDO MANHÃ — {hoje.strftime('%d/%m/%Y')} ({nome})
## Tema: {tema} | Público: {publico}
## Publicar: 07h00

---

## INSTAGRAM — Carrossel (5 slides)

**Slide 1 (Capa):**
Título: [INSERIR DICA SOBRE: {tema}]
Subtítulo: Jurisperitus Escola Online
Fundo: #003B83 | Texto: #FFB400

**Slide 2:** [Conceito principal — 1 regra ou definição]

**Slide 3:** [Exemplo prático do universo jurídico]

**Slide 4:** [Erro comum + como corrigir]

**Slide 5 (CTA):**
"Quer dominar {tema.lower()}?
Acesse: jurisperitus.com.br"

**Legenda Instagram:**
🎯 {tema} — o que todo profissional do Direito precisa saber.

[INSERIR 3 LINHAS DE CONTEÚDO SOBRE O TEMA]

Salva esse post para consultar depois! 📌

{HASHTAGS}

---

## TIKTOK — Script (45 segundos)

[0:00] GANCHO: "[INSERIR PERGUNTA PROVOCATIVA SOBRE {tema}]"
[0:05] Desenvolvimento — regra ou conceito principal
[0:20] Exemplo prático jurídico
[0:35] CTA: "Segue para mais dicas. Link na bio — Jurisperitus."
🎵 [som trending do nicho jurídico]

---

## LINKEDIN — Post (400 palavras)

**Título:** [INSERIR INSIGHT PROFISSIONAL SOBRE {tema}]

[INSERIR 4 PARÁGRAFOS:
1. Abertura com dado ou provocação
2. O problema que o tema resolve
3. A solução / aprendizado principal
4. CTA para jurisperitus.com.br]

#Direito #LinguagemJurídica #OAB #ConcursoPublico #Jurisperitus

---

## TWITTER/X — Thread (5 tweets)

1/ [Abertura com gancho sobre {tema}] 🧵

2/ [Regra principal]

3/ [Exemplo jurídico]

4/ [Erro comum]

5/ Gostou? Segue @jurisperitus para mais.
Cursos: jurisperitus.com.br

---

*Claude Coworking | Jurisperitus | {hoje.strftime('%d/%m/%Y')}*
"""

def gerar_tarde():
    prod_nome, prod_preco = produto_dia
    return f"""# CONTEÚDO TARDE — {hoje.strftime('%d/%m/%Y')} ({nome})
## Produto em destaque: {prod_nome} ({prod_preco})
## Publicar: 12h00

---

## INSTAGRAM — Post único com CTA

**Visual:** fundo #003B83, texto dourado #FFB400
**Título:** "{prod_nome}"
**Subtítulo:** "{prod_preco} — link na bio"

**Legenda:**
💡 Você já conhece o {prod_nome} da Jurisperitus?

[INSERIR 2-3 LINHAS SOBRE O BENEFÍCIO PRINCIPAL DO PRODUTO]

👉 {prod_preco} — acesso imediato
🔗 Link na bio → jurisperitus.com.br

{HASHTAGS} #hotmart #cursonline

---

## TIKTOK — Script produto (30 segundos)

[0:00] *"[GANCHO SOBRE PROBLEMA QUE O PRODUTO RESOLVE]"*
[0:05] Mostrar o produto / resultado
[0:15] Benefício principal em 1 frase
[0:20] Prova: "[resultado de quem usou]"
[0:25] CTA: "{prod_preco}. Link na bio."
🏷️ #IA #direito #OAB #jurisperitus

---

## TODOS OS CANAIS — Texto curto

"{prod_nome} | {prod_preco} | jurisperitus.com.br"

---

*Claude Coworking | OS-08 | Meta R$20k/30jul*
"""

def gerar_noite():
    centurao = dia == 4  # Sexta-feira
    return f"""# CONTEÚDO NOITE — {hoje.strftime('%d/%m/%Y')} ({nome})
## Tipo: {'Mentalidade (Centurião Romano)' if centurao else 'Engajamento / Comunidade'}
## Publicar: 19h00

---

## INSTAGRAM — Story (3 slides)

**Story 1:** Pergunta de engajamento
"[PERGUNTA SOBRE {tema} para os seguidores responderem]"
Adicionar enquete: Sim / Não  OU  Caixa de perguntas

**Story 2:** Bastidores ou curiosidade
[INSERIR CONTEÚDO LEVE / MOTIVACIONAL]

**Story 3:** CTA suave
"Amanhã tem mais. Ativa as notificações! 🔔"

---

## POST MOTIVACIONAL — Todos os canais

{'**ÂNCORA CENTURIÃO ROMANO:**' if centurao else '**MOTIVAÇÃO DA SEMANA:**'}

{'*"Apenas dize uma palavra — e meu servo sarará."* (Mt 8:5-13)' if centurao else ''}

[INSERIR TEXTO MOTIVACIONAL SOBRE APROVAÇÃO / PERSISTÊNCIA / EXCELÊNCIA]

Jurisperitus — porque dominar a palavra é dominar o Direito. ⚖️

{HASHTAGS} #motivacao #aprovacao #mentalidade

---

## FACEBOOK — Post comunidade

[INSERIR PERGUNTA PARA GERAR COMENTÁRIOS:
"Qual foi sua maior dificuldade com [tema] nos estudos? Conta nos comentários!"]

---

*Claude Coworking | Jurisperitus | {hoje.strftime('%d/%m/%Y')}*
"""

if __name__ == "__main__":
    pasta_hoje = f"{SAIDA}/{hoje.strftime('%Y-%m-%d')}"

    f1 = salvar(f"{pasta_hoje}/manha",  "POST_MANHA.md",  gerar_manha())
    f2 = salvar(f"{pasta_hoje}/tarde",  "POST_TARDE.md",  gerar_tarde())
    f3 = salvar(f"{pasta_hoje}/noite",  "POST_NOITE.md",  gerar_noite())

    print(f"\n🎯 CONTEÚDO DO DIA — {hoje.strftime('%d/%m/%Y')} ({nome})")
    print(f"   Tema: {tema}")
    print(f"   Produto destaque: {produto_dia[0]} ({produto_dia[1]})")
    print(f"\n✅ Manhã  → {f1}")
    print(f"✅ Tarde  → {f2}")
    print(f"✅ Noite  → {f3}")
    print(f"\n📊 Meta: R$ 20.000 até 30/07/2026")
    print(f"   Vendas necessárias hoje: ~6 | Ticket médio: R$ 47")
