# AUTOMAÇÃO DE REDES SOCIAIS — PLANO DE EXECUÇÃO
## Jurisperitus | Claude Coworking OS-09

---

## SITUAÇÃO REAL — HONESTIDADE OPERACIONAL

Instagram, TikTok, Facebook, LinkedIn e Twitter **não permitem
que uma IA externa publique diretamente** sem autorização OAuth
do titular da conta. Isso é uma política das próprias plataformas,
não uma limitação do Claude.

**O que é possível agora:**
- Claude produz TODO o conteúdo pronto (texto, script, legenda, hashtag)
- Uma ferramenta de agendamento publica automaticamente
- Prof. Dr. Freire autoriza a ferramenta 1 vez → automação permanente

---

## SOLUÇÃO: BUFFER (gratuito, 10 minutos de configuração)

### O que o Buffer faz
Você conecta suas redes sociais uma vez.
Claude gera o conteúdo.
O Buffer publica nos horários programados (07h / 12h / 19h).

### Planos
| Plano | Preço | Canais | Posts/mês |
|-------|-------|--------|-----------|
| Free | Grátis | 3 canais | 30/canal |
| Essentials | ~R$55/mês | 1 canal ilimitado | Ilimitado |
| Team | ~R$110/mês | Canais ilimitados | Ilimitado |

**Recomendação:** Free para testar esta semana → Team quando as vendas cobrirem.

### Como configurar (15 minutos)
1. Acessar **buffer.com** → Create account
2. Conectar: Instagram, Facebook, LinkedIn, Twitter
3. TikTok: usar **TikTok Scheduler** dentro do próprio TikTok Studio (gratuito)
4. Programar horários: 07:00 / 12:00 / 19:00 (horário de Brasília)

---

## FLUXO DE TRABALHO APÓS BUFFER CONFIGURADO

```
DIARIAMENTE (Claude executa automaticamente):
python3 gerar_conteudo.py
→ Gera POST_MANHA.md + POST_TARDE.md + POST_NOITE.md

PROF. DR. FREIRE (5 minutos/dia):
→ Abre os 3 arquivos
→ Cola no Buffer
→ Buffer publica nos horários

RESULTADO:
3 publicações/dia × 5 plataformas = 15 posts/dia
→ Crescimento orgânico contínuo
→ Geração de leads para jurisperitus.com.br
→ Vendas no Hotmart
```

---

## PLANO DE AUTOMAÇÃO POR SITE

### jurisperitus.com.br — AUTOMAÇÃO TOTAL ✅
Claude altera e deploya sozinho via git push.

### jurisperitusescolaonline.com.br (EADSimples) — SEMI-AUTO
Claude produz: banners, textos de curso, descrições, thumbnails
Prof. Dr. Freire: cola no painel EADSimples

### professorfreire.com.br / .com — CRIAR AGORA
Claude cria o site completo (HTML estático)
Prof. Dr. Freire: faz upload via hPanel Hostinger (1x)
Depois: Claude atualiza via FTP ou novo deploy manual

### advogadodagramatica.com.br — CRIAR AGORA
Mesmo processo

### portuguesinesquecivel.com.br — CRIAR AGORA
Mesmo processo

---

## OS-09A — SITES HOSTINGER (entregar esta semana)

### professorfreire.com.br
**Proposta:** landing page do Prof. Dr. Freire como autoridade
- Bio completa
- Cursos da Jurisperitus
- Link para jurisperitusescolaonline.com.br
- Formulário de contato

### advogadodagramatica.com.br
**Proposta:** landing page segmentada para advogados
- Headline: "O português que separa advogados comuns dos excepcionais"
- Cursos: Linguagem Jurídica + Redação + Gramática
- CTA direto para Hotmart

### portuguesinesquecivel.com.br
**Proposta:** landing page para concurseiros e estudantes
- Headline: "Aprenda português de um jeito que você nunca esquece"
- Cursos de gramática + memorização
- CTA para Hotmart

---

## PRÓXIMAS AÇÕES (sequência de velocidade)

| Prioridade | Ação | Tempo | Responsável |
|-----------|------|-------|-------------|
| 🔴 AGORA | Ativar página de vendas Corretor no Hotmart | 20 min | Prof. Dr. Freire |
| 🔴 AGORA | Configurar Buffer (3 canais gratuitos) | 15 min | Prof. Dr. Freire |
| 🟡 HOJE | Claude cria sites professorfreire.com.br e advogadodagramatica.com.br | 30 min | Claude |
| 🟡 HOJE | Upload dos sites no Hostinger | 10 min | Prof. Dr. Freire |
| 🟢 SEMANA | Gravar 5 vídeos TikTok com scripts prontos | 60 min | Prof. Dr. Freire |
| 🟢 SEMANA | Configurar sequência de e-mails no Hotmart | 30 min | Prof. Dr. Freire |

---

## META S1 (21-27/05): R$ 2.000

**Como chegar lá:**
- Corretor de Redações: 20 vendas × R$19,90 = R$398
- 50 Prompts: 15 vendas × R$37 = R$555
- Cartilha OAB: 10 vendas × R$47 = R$470
- Planner: 8 vendas × R$47 = R$376
- Analisador TCC: 2 vendas × R$97 = R$194
**Total: R$ 1.993 ≈ R$ 2.000 ✅**

Isso com apenas 55 vendas em 7 dias = ~8 vendas/dia.
Com TikTok ativo + Hotmart otimizado = viável.

---

*Jurisperitus Escola Online | Claude Coworking OS-09*
*Meta: R$ 20.000 até 30/07/2026*
