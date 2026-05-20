#!/usr/bin/env python3
"""
JURISPERITUS — ROTINA DIÁRIA AUTOMATIZADA
Claude Coworking | Versão 1.0
Executa checklist diário, gera relatório e prepara fila de conteúdo.
"""

import datetime
import os
import json

BASE = "/home/claude/jurisperitus"
LOG_DIR = f"{BASE}/relatorios"
os.makedirs(LOG_DIR, exist_ok=True)

hoje = datetime.date.today()
dia_semana = hoje.weekday()  # 0=Segunda, 6=Domingo
nomes_dia = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
nome_hoje = nomes_dia[dia_semana]

# ─── CALENDÁRIO DE CONTEÚDO ──────────────────────────────────────────────────
CALENDARIO = {
    "Segunda":  {"tema": "Gramática / Dica de Português",         "agente": "AG02+AG06", "formato": "Artigo blog + Post"},
    "Terça":    {"tema": "Direito / Linguagem Jurídica",           "agente": "AG04",      "formato": "Reel + Carrossel"},
    "Quarta":   {"tema": "IA & Tecnologia aplicada ao Direito",    "agente": "AG05",      "formato": "Post LinkedIn + Thread X"},
    "Quinta":   {"tema": "Oratória / Comunicação",                 "agente": "AG06",      "formato": "Script HeyGen + Short"},
    "Sexta":    {"tema": "Motivação / Mentalidade (Centurião)",     "agente": "AG07",      "formato": "Story + Post motivacional"},
    "Sábado":   {"tema": "Concursos / Carreira Jurídica",          "agente": "AG08",      "formato": "Artigo blog + Relatório"},
    "Domingo":  {"tema": "Bastidores / Depoimentos / Comunidade",  "agente": "AG01",      "formato": "Relatório semanal consolidado"},
}

# ─── CHECKLIST DIÁRIO ────────────────────────────────────────────────────────
CHECKLIST_DIARIO = [
    "[ ] Verificar indexação Google Search Console",
    "[ ] Publicar conteúdo do dia (conforme calendário)",
    "[ ] Responder comentários e DMs nas redes sociais",
    "[ ] Checar performance anúncios Google Ads",
    "[ ] Verificar vendas do dia (Hotmart/plataforma)",
    "[ ] Atualizar PAINEL_OS se necessário",
    "[ ] Gerar 1 artigo de blog (fila SEO)",
    "[ ] Monitorar concorrência (tendências do dia)",
]

# ─── SITES A GESTIONAR ───────────────────────────────────────────────────────
SITES = [
    {"url": "jurisperitusescolaonline.com.br",  "status": "Otimizado",  "prioridade": "Alta"},
    {"url": "jurisperitus.com.br",               "status": "Pendente",   "prioridade": "Alta"},
    {"url": "professorfreire.com.br",            "status": "Pendente",   "prioridade": "Média"},
    {"url": "professorfreire.com",               "status": "Pendente",   "prioridade": "Média"},
    {"url": "advogadodagramatica.com.br",        "status": "Pendente",   "prioridade": "Média"},
    {"url": "portuguesinesquecivel.com.br",      "status": "Pendente",   "prioridade": "Média"},
]

# ─── REDES SOCIAIS ───────────────────────────────────────────────────────────
REDES = [
    {"plataforma": "YouTube",   "handle": "@jurisperitus", "meta": "1.000 inscritos"},
    {"plataforma": "Instagram", "handle": "@jurisperitus", "meta": "10k seguidores"},
    {"plataforma": "TikTok",    "handle": "@jurisperitus", "meta": "Viral nicho jurídico"},
    {"plataforma": "Facebook",  "handle": "Jurisperitus",  "meta": "Comunidade ativa"},
    {"plataforma": "LinkedIn",  "handle": "Jurisperitus",  "meta": "Autoridade B2B"},
    {"plataforma": "Twitter/X", "handle": "@jurisperitus", "meta": "Engajamento diário"},
]

# ─── GERADOR DE RELATÓRIO DIÁRIO ────────────────────────────────────────────
def gerar_relatorio():
    conteudo_hoje = CALENDARIO.get(nome_hoje, {})
    
    relatorio = f"""# RELATÓRIO DIÁRIO — CLAUDE COWORKING JURISPERITUS
**Data:** {hoje.strftime('%d/%m/%Y')} ({nome_hoje})
**Gerado por:** Sistema de Automação Claude Coworking

---

## TEMA DO DIA
**{conteudo_hoje.get('tema', 'N/A')}**  
Agente responsável: {conteudo_hoje.get('agente', 'N/A')}  
Formato de entrega: {conteudo_hoje.get('formato', 'N/A')}

---

## CHECKLIST DIÁRIO

{chr(10).join(CHECKLIST_DIARIO)}

---

## STATUS DOS SITES

| Site | Status | Prioridade |
|------|--------|------------|
"""
    for s in SITES:
        relatorio += f"| {s['url']} | {s['status']} | {s['prioridade']} |\n"

    relatorio += f"""
---

## REDES SOCIAIS — PUBLICAÇÃO DO DIA

| Plataforma | Handle | Meta |
|------------|--------|------|
"""
    for r in REDES:
        relatorio += f"| {r['plataforma']} | {r['handle']} | {r['meta']} |\n"

    relatorio += f"""
---

## AÇÕES PRIORITÁRIAS HOJE

1. Produzir conteúdo: **{conteudo_hoje.get('tema', '—')}**
2. Formato: **{conteudo_hoje.get('formato', '—')}**
3. Publicar em todas as redes ativas
4. Verificar Google Ads — orientar para conversão de vendas
5. Checar migração blog: blogspot → jurisperitusescolaonline.jurisperitus.com.br

---

## ALERTA BLOG (CRÍTICO)
⚠️ O blog atual em **jurisperitusescolaonline.blogspot.com** deve ser migrado  
para **jurisperitusescolaonline.jurisperitus.com.br** para habilitar monetização Google AdSense.  
Ação: configurar domínio customizado no Blogger ou migrar para WordPress/Ghost.

---

*Jurisperitus Escola Online | CNPJ: 55.274.545/0001-88 | jurisperitusescolaonline.com.br*
"""
    return relatorio


# ─── GERADOR DE PROMPT DIÁRIO PARA CLAUDE ───────────────────────────────────
def gerar_prompt_claude():
    conteudo_hoje = CALENDARIO.get(nome_hoje, {})
    return f"""PROMPT AUTOMÁTICO — {hoje.strftime('%d/%m/%Y')} ({nome_hoje})

Você é o Claude Coworking da Jurisperitus. Hoje é {nome_hoje}.

TAREFA DO DIA:
- Tema: {conteudo_hoje.get('tema', 'N/A')}
- Formato de entrega: {conteudo_hoje.get('formato', 'N/A')}
- Agente responsável: {conteudo_hoje.get('agente', 'N/A')}

Produza o conteúdo completo para publicação hoje nas redes sociais da Jurisperitus.
Padrão visual: #003B83 (azul) + #FFB400 (dourado). Tom: professor + especialista + mentor.
Inclua CTA para os cursos em jurisperitusescolaonline.com.br.
Âncora narrativa disponível: O Centurião Romano (Mt 8:5-13) — use se tema permitir.
"""


# ─── EXECUÇÃO PRINCIPAL ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"🚀 Claude Coworking Jurisperitus — {hoje.strftime('%d/%m/%Y')} ({nome_hoje})")
    print("=" * 60)
    
    # Gerar relatório
    relatorio = gerar_relatorio()
    nome_arquivo = f"{LOG_DIR}/relatorio_{hoje.strftime('%Y-%m-%d')}.md"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(relatorio)
    print(f"✅ Relatório gerado: {nome_arquivo}")
    
    # Gerar prompt do dia
    prompt = gerar_prompt_claude()
    prompt_arquivo = f"{LOG_DIR}/prompt_dia_{hoje.strftime('%Y-%m-%d')}.txt"
    with open(prompt_arquivo, "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"✅ Prompt do dia gerado: {prompt_arquivo}")
    
    # Exibir checklist
    print("\n📋 CHECKLIST DO DIA:")
    for item in CHECKLIST_DIARIO:
        print(f"  {item}")
    
    print(f"\n🎯 TEMA DO DIA: {CALENDARIO.get(nome_hoje, {}).get('tema', 'N/A')}")
    print("=" * 60)
    print("Claude Coworking pronto para operação.")
