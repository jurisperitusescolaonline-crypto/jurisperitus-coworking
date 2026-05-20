# PLANO DE MIGRAÇÃO DO BLOG — MAPA COMPLETO DE DEPENDÊNCIAS
## Claude Coworking | Jurisperitus | Maio de 2026

---

## 1. DIAGNÓSTICO DA INFRAESTRUTURA (verificado em 19/05/2026)

### Servidores identificados

| IP | Servidor | Hospeda |
|----|----------|---------|
| `98.84.224.111` | AWS EC2 (us-east-1) | jurisperitus.com.br (principal) |
| `18.208.88.157` | AWS EC2 (us-east-1) — **DIFERENTE** | jurisperitus.com.br/tutor |
| `104.21.51.151` | Cloudflare CDN | jurisperitusescolaonline.com.br |
| `142.250.125.132` | Google (Blogger) | jurisperitusescolaonline.blogspot.com |

### ⚠️ Achado crítico
`jurisperitus.com.br/tutor` resolve para um IP AWS **diferente** do domínio raiz.
Isso indica que `/tutor` é uma aplicação separada (possivelmente um LMS, painel de aluno
ou ferramenta externa) hospedada em outra instância AWS — não é uma pasta no mesmo servidor.

### Subdomínios livres (prontos para criar)
- `blog.jurisperitus.com.br` — NÃO EXISTE ✅
- `jurisperitusescolaonline.jurisperitus.com.br` — NÃO EXISTE ✅

---

## 2. MAPA COMPLETO DE URLs A PRESERVAR

### URLs ativas confirmadas (NÃO podem quebrar)

| URL | Servidor | Tipo | Ação na migração |
|-----|----------|------|-----------------|
| `jurisperitus.com.br` | AWS EC2 #1 | Site principal | **Não tocar** |
| `jurisperitus.com.br/tutor` | AWS EC2 #2 | Aplicação separada (LMS?) | **Não tocar — servidor próprio** |
| `jurisperitus.com.br/diagnostico` | AWS EC2 #1 | Página/ferramenta | **Não tocar** |
| `jurisperitusescolaonline.com.br` | Cloudflare | Site principal escola | **Não tocar** |
| `jurisperitusescolaonline.blogspot.com` | Google | Blog atual | Migrar + redirecionar |

### Links de planilhas (a confirmar com Prof. Dr. Freire)
> ⚠️ Os links de planilhas mencionados precisam ser listados pelo Prof. Dr. Freire
> para incluir no mapa. Possíveis formatos:
> - `docs.google.com/spreadsheets/...`
> - `jurisperitus.com.br/planilha-X`
> - Links encurtados apontando para jurisperitus.com.br

---

## 3. ESTRATÉGIA DE MIGRAÇÃO — ZERO IMPACTO NAS URLs EXISTENTES

### Princípio fundamental
A migração do blog opera **exclusivamente no DNS de jurisperitus.com.br**,
adicionando um novo subdomínio. Nenhuma rota existente é alterada.

```
ANTES DA MIGRAÇÃO:
jurisperitus.com.br          → AWS EC2 #1 (INALTERADO)
jurisperitus.com.br/tutor    → AWS EC2 #2 (INALTERADO)
jurisperitus.com.br/diagnostico → AWS EC2 #1 (INALTERADO)
[planilhas]                  → destinos atuais (INALTERADO)

DEPOIS DA MIGRAÇÃO (apenas adição):
jurisperitusescolaonline.jurisperitus.com.br → Google Blogger (NOVO)
```

### Por que é seguro
- Criar um subdomínio novo **nunca** afeta rotas existentes
- O DNS de `jurisperitus.com.br` tem registros `A` e possivelmente registros de subdomínio
- Adicionar `jurisperitusescolaonline` como CNAME é uma operação isolada
- `/tutor`, `/diagnostico` e planilhas continuam intocados

---

## 4. PASSO A PASSO DA MIGRAÇÃO

### FASE 1 — Configurar domínio no Blogger (10 minutos)

1. Acessar: **blogger.com** → Jurisperitus Escola Online → **Configurações**
2. Ir em: **Domínio personalizado**
3. Inserir: `jurisperitusescolaonline.jurisperitus.com.br`
4. O Blogger vai exibir **2 registros CNAME** para configurar no DNS. Anotar:
   - CNAME 1: `jurisperitusescolaonline` → `ghs.google.com`
   - CNAME 2: código de verificação (ex: `abcdef1234` → `gv-xxxx.dv.googlehosted.com`)

---

### FASE 2 — Configurar DNS (5-15 minutos + até 48h propagação)

Acessar o painel DNS do domínio `jurisperitus.com.br`.

**Registros a ADICIONAR** (não alterar nenhum existente):

```
Tipo    Host                              Valor                    TTL
CNAME   jurisperitusescolaonline          ghs.google.com           3600
CNAME   [código do Blogger]               [valor do Blogger]       3600
```

> O painel DNS depende de onde o domínio está registrado.
> Verificar: Registro.br, GoDaddy, Hostgator, Locaweb ou similar.
> **Atenção:** só adicionar — não editar nem remover registros existentes.

---

### FASE 3 — Ativar e verificar no Blogger (após propagação DNS)

1. Voltar ao Blogger → Configurações → Domínio personalizado
2. Clicar em **Salvar** / **Verificar**
3. Ativar opção: **"Redirecionar jurisperitusescolaonline.blogspot.com para novo domínio"**
   - Isso cria redirecionamento 301 automático
   - Todos os links antigos do blogspot continuam funcionando (redirecionam)
   - Google preserva o SEO dos artigos existentes

---

### FASE 4 — Verificar integridade das URLs existentes (pós-migração)

Após ativar, testar manualmente:
- [ ] `jurisperitus.com.br` → abre normalmente
- [ ] `jurisperitus.com.br/tutor` → abre normalmente
- [ ] `jurisperitus.com.br/diagnostico` → abre normalmente
- [ ] [links de planilhas] → abrem normalmente
- [ ] `jurisperitusescolaonline.jurisperitus.com.br` → abre o blog
- [ ] `jurisperitusescolaonline.blogspot.com` → redireciona para novo domínio

---

## 5. APÓS A MIGRAÇÃO — SOLICITAR GOOGLE ADSENSE

### Pré-requisitos AdSense
- [x] Domínio próprio (concluído com esta migração)
- [ ] Mínimo 20-30 artigos publicados de qualidade
- [ ] Política de privacidade publicada no blog
- [ ] Página "Sobre" publicada no blog
- [ ] Tráfego orgânico iniciado (SEO básico ativo)
- [ ] Blog com pelo menos 30-60 dias de existência no domínio próprio

### Sequência pós-migração
1. Publicar **1 artigo por dia** (AG03 em operação)
2. Adicionar página "Política de Privacidade"
3. Adicionar página "Sobre o Prof. Dr. Freire / Jurisperitus"
4. Após 30 dias + 30 artigos → acessar **adsense.google.com** e solicitar aprovação
5. Inserir código AdSense no Blogger → Tema → HTML → `<head>`

---

## 6. INFORMAÇÕES QUE PRECISAM SER CONFIRMADAS PELO PROF. DR. FREIRE

Antes de executar a migração, confirmar:

1. **Onde está registrado o domínio `jurisperitus.com.br`?**
   (Registro.br / GoDaddy / Hostgator / outro — para acessar o DNS correto)

2. **Quais são exatamente os links das planilhas conectados a `jurisperitus.com.br`?**
   (Para incluir no teste pós-migração e garantir que continuam funcionando)

3. **O `/tutor` é um LMS externo (Hotmart, Kiwify, EAD Plataforma)?**
   (Para entender se há login de alunos que pode ser afetado)

4. **Quantos artigos existem no blogspot hoje?**
   (Para planejar a migração de conteúdo existente)

---

## 7. RISCOS E MITIGAÇÕES

| Risco | Probabilidade | Mitigação |
|-------|--------------|-----------|
| DNS propagação lenta (até 48h) | Média | Planejar para sexta à noite — não em dia de campanha ativa |
| Blogger recusar domínio | Baixa | Verificar se subdomínio tem CNAME correto antes de salvar |
| Links antigos do blogspot quebrarem | Mínima | Ativar redirecionamento automático no Blogger |
| URLs `/tutor` ou `/diagnostico` quebrarem | Nenhuma | Operação isolada em subdomínio novo — não toca nas rotas existentes |
| Planilhas quebrarem | Nenhuma | Links de planilhas Google não passam por DNS do domínio |

---

*Jurisperitus Escola Online | CNPJ: 55.274.545/0001-88*
*Claude Coworking — AG02 (Sites & SEO) + AG03 (Blog & Monetização)*
