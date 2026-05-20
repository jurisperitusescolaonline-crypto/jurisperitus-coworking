# PLANO DE AÇÃO CRÍTICO — BLOG & GOOGLE ADS
**Claude Coworking | Jurisperitus | Maio de 2026**

---

## ⚠️ AÇÃO 1 — MIGRAÇÃO DO BLOG (URGENTE — MONETIZAÇÃO)

### Problema
Blog atual: `jurisperitusescolaonline.blogspot.com`  
O Google AdSense **não monetiza blogs em subdomínio blogspot.com**.  
Exige domínio próprio para aprovação.

### Solução: 2 caminhos

#### CAMINHO A — Domínio customizado no Blogger (mais simples)
1. Acessar Blogger → Configurações → Domínio personalizado
2. Inserir: `blog.jurisperitus.com.br` ou `jurisperitusescolaonline.jurisperitus.com.br`
3. No painel DNS do seu domínio (jurisperitus.com.br), adicionar:
   - CNAME: `www` → `ghs.google.com`
   - CNAME verificação fornecida pelo Blogger
4. Aguardar propagação (até 48h)
5. Ativar redirecionamento do blogspot para o novo domínio
6. **Após 30 dias de conteúdo** → solicitar AdSense

#### CAMINHO B — Migrar para WordPress (recomendado para SEO avançado)
1. Instalar WordPress em `blog.jurisperitus.com.br`
2. Importar posts do Blogger (Ferramentas → Importar → Blogger)
3. Configurar redirecionamentos 301
4. Instalar plugins: Yoast SEO, WooCommerce, MonsterInsights
5. **Vantagem:** controle total, SEO superior, plugins de conversão

### Recomendação Claude Coworking
**Caminho A agora** (rápido, sem custo) → **Caminho B em 60 dias** quando o site estiver gerando receita.

---

## ⚠️ AÇÃO 2 — CORREÇÃO GOOGLE ADS (URGENTE — VENDAS)

### Diagnóstico dos problemas prováveis

| Problema | Sintoma | Correção |
|----------|---------|----------|
| Objetivo errado | Tráfego sem compras | Mudar para "Conversões" |
| Sem tag de conversão | Google não rastreia vendas | Instalar Google Tag + evento |
| Landing page fraca | Visitante não compra | Criar LP dedicada por curso |
| Palavras-chave amplas | Cliques irrelevantes | Usar correspondência exata |
| Sem remarketing | Visitantes somem | Criar lista de remarketing |
| Sem extensões | Anúncio pequeno | Adicionar sitelinks + chamadas |

### Plano de Correção em 5 Passos

#### PASSO 1 — Instalar rastreamento de conversão
```
Google Ads → Ferramentas → Conversões → Nova conversão
Tipo: Site → Compra
Valor: Dinâmico (valor do curso)
Instalar tag via Google Tag Manager no botão de compra
```

#### PASSO 2 — Reconfigurar objetivo da campanha
```
Campanha atual → Configurações → Objetivo
Trocar: "Tráfego do site" → "Vendas" ou "Leads"
Estratégia de lances: CPA desejado ou ROAS desejado
```

#### PASSO 3 — Palavras-chave cirúrgicas
```
ALTA INTENÇÃO (compra):
[curso linguagem jurídica online]
[curso redação jurídica OAB]
[gramática para concursos jurídicos]
[oratória jurídica curso]
[português para advogados]

EXCLUIR (negativas):
grátis, gratuito, pirata, baixar, download
```

#### PASSO 4 — Landing Pages dedicadas
```
Criar 1 LP por curso (não enviar para página inicial):
/lp-linguagem-juridica
/lp-redacao-juridica
/lp-gramatica-juridica

Cada LP: headline forte + benefícios + depoimentos + CTA único
```

#### PASSO 5 — Campanha de remarketing
```
Audiência: visitantes do site (últimos 30 dias)
Excluir: quem já comprou
Anúncio: "Você visitou o curso X. Inscreva-se hoje com desconto."
Lance: +30% sobre campanha fria
```

---

## FUNIL DE VENDAS COMPLETO

```
ANÚNCIO GOOGLE
     ↓
LANDING PAGE DO CURSO (LP dedicada)
     ↓
BOTÃO "INSCREVA-SE AGORA"
     ↓
CHECKOUT (Hotmart ou plataforma)
     ↓
CONFIRMAÇÃO DE COMPRA → e-mail de boas-vindas
     ↓
UPSELL: "Conheça o Pacote Completo"
     ↓
COMUNIDADE / FIDELIZAÇÃO
```

---

## CALENDÁRIO DE IMPLEMENTAÇÃO

| Semana | Ação | Responsável |
|--------|------|-------------|
| S1 | Migrar blog para domínio próprio | Prof. Dr. Freire + AG02 |
| S1 | Instalar Google Tag Manager | Prof. Dr. Freire + AG05 |
| S1 | Reconfigurar objetivo das campanhas | AG05 |
| S2 | Criar LPs dedicadas por curso | AG02 + AG06 |
| S2 | Adicionar palavras-chave de alta intenção | AG05 |
| S2 | Lançar campanha de remarketing | AG05 |
| S3 | Publicar 10 artigos de blog (AdSense) | AG03 |
| S4 | Relatório de resultados e ajustes | AG01 |

---

*Jurisperitus Escola Online | CNPJ: 55.274.545/0001-88*  
*jurisperitusescolaonline.com.br | Brasília/DF*
