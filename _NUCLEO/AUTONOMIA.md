# MODELO DE AUTONOMIA — CLAUDE COWORKING JURISPERITUS
## Como dar ao Claude capacidade de agir de forma independente
**Versão 1.0 | Maio de 2026**

---

## O QUE JÁ ESTÁ INSTALADO E OPERACIONAL

| Ferramenta | Versão | Função |
|------------|--------|--------|
| Claude Code | 2.1.145 | IA autônoma no terminal |
| Node.js | 22.22.2 | Runtime para automações |
| Netlify CLI | 26.0.2 | Deploy direto sem browser |
| Python 3 | 3.12.3 | Scripts de automação |
| Git | 2.43.0 | Controle de versão |
| Repositório Git | ativo | Histórico de todas as entregas |

---

## O QUE FALTA — 3 TOKENS (ações humanas, 10 minutos)

### TOKEN 1 — Netlify (deploy autônomo)
**Para que serve:** Claude faz deploys diretos sem você arrastar arquivos.

**Como gerar:**
1. Acessar `app.netlify.com`
2. Avatar no canto superior direito → **User settings**
3. **Applications → Personal access tokens → New access token**
4. Nome: `Claude Coworking Jurisperitus`
5. Copiar o token gerado (aparece uma única vez)
6. Trazer aqui para Claude configurar

**O que Claude poderá fazer:**
- `python3 /home/claude/jurisperitus/deploy.py` → deploy em produção
- Atualizar a landing page sem intervenção humana
- Fazer deploys de preview para testes

---

### TOKEN 2 — GitHub (repositório remoto + CI/CD)
**Para que serve:** backup de todo o código, histórico completo,
e deploy automático ao commitar (Netlify lê o GitHub e deploya sozinho).

**Como criar:**
1. Acessar `github.com` → criar conta ou logar
2. **Settings → Developer settings → Personal access tokens → Tokens (classic)**
3. **Generate new token** → marcar: `repo`, `workflow`
4. Nome: `Claude Coworking Jurisperitus`
5. Copiar o token
6. Trazer aqui para Claude configurar e fazer o push inicial

**O que Claude poderá fazer:**
- Commitar e empurrar código autonomamente
- O Netlify detecta o push e deploya sozinho (deploy automático zero-clique)

---

### TOKEN 3 — Formspree ou serviço de e-mail (captura de leads)
**Para que serve:** os leads do formulário da landing page chegam
numa lista ativa (e-mail marketing, CRM).

**Opções:**
- **Formspree** (gratuito até 50 envios/mês): `formspree.io` → criar formulário → copiar ID
- **RD Station** / **ActiveCampaign**: copiar URL do formulário de captura
- **Hotmart Club**: usar endpoint de lead da lista

---

## ARQUITETURA DE AUTONOMIA COMPLETA

```
Prof. Dr. Freire
    │
    │  Aprova estratégia
    │  Fornece tokens (1 vez)
    ▼
Claude Coworking (esta máquina)
    │
    ├── Edita arquivos    → /home/claude/jurisperitus/
    ├── Commita no Git    → git commit + push → GitHub
    ├── Deploy Netlify    → netlify deploy --prod
    ├── Gera relatórios   → python3 rotina_diaria.py
    └── Monitora domínios → scripts de verificação DNS/HTTP
```

**Fluxo de trabalho autônomo (após tokens configurados):**
1. Claude recebe instrução → edita/cria arquivos
2. Claude testa localmente → valida o resultado
3. Claude commita no Git → histórico preservado
4. Claude deploya no Netlify → live em segundos
5. Claude envia relatório → Prof. Dr. Freire valida

---

## FLUXO ATUAL (sem tokens) vs FLUXO AUTÔNOMO

| Ação | Sem tokens | Com tokens |
|------|-----------|------------|
| Atualizar landing page | Claude cria arquivo → você faz upload | Claude deploya direto |
| Novo artigo no blog | Claude escreve → você publica | Claude publica via API |
| Corrigir DNS | Claude instrui → você executa | Claude via Hostinger API |
| Backup do código | Manual | Git automático a cada entrega |
| Relatório diário | Manual | `python3 rotina_diaria.py` agendado |

---

## NÍVEL DE AUTONOMIA POR CAMADA

| Camada | Autonomia atual | Com tokens |
|--------|----------------|------------|
| Criação de conteúdo | ✅ 100% autônomo | ✅ 100% |
| Edição de código | ✅ 100% autônomo | ✅ 100% |
| Deploy Netlify | ❌ requer upload manual | ✅ autônomo |
| Git / versionamento | ✅ local (sem push remoto) | ✅ remoto |
| DNS / Hostinger | ❌ requer acesso manual | ⚡ parcial via API |
| E-mail marketing | ❌ requer integração | ✅ via Formspree/RD |

---

## PRÓXIMA SESSÃO — O QUE TRAZER

Para ativar autonomia total na próxima sessão:
1. Token do Netlify (gerado em app.netlify.com)
2. Token do GitHub (gerado em github.com/settings)
3. URLs exatas dos projetos `/tutor` e `/diagnostico` no Netlify
4. Decisão sobre plataforma de e-mail (Formspree / RD Station / Hotmart)

---

*Claude Coworking — Jurisperitus Escola Online*
*CNPJ: 55.274.545/0001-88 | jurisperitusescolaonline.com.br*
