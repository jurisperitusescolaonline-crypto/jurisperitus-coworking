# OS-07 — FASE 0: CORRIGIR jurisperitus.com.br (URGENTE — BLOQUEADOR)
## Claude Coworking | Jurisperitus | Maio de 2026

---

## SITUAÇÃO ATUAL (diagnóstico técnico — 19/05/2026)

| Item | Status |
|------|--------|
| Domínio registrado no Registro.br | ✅ OK |
| Nameservers apontando para Hostinger | ✅ OK (`dns1-4.p09.nsone.net`) |
| Site configurado no Hostinger | ❌ PROBLEMA |
| HTTP 403 em todas as rotas | ❌ BLOQUEADOR |
| IPs AWS EC2 ainda respondendo (legado) | ⚠️ Resquício da migração |

**Diagnóstico:** O DNS já está no Hostinger. O problema é que o Hostinger
não tem o site vinculado/configurado para este domínio.
HTTP 403 significa: "servidor existe, mas não tem site para mostrar aqui."

---

## CAUSA RAIZ — 3 POSSIBILIDADES

### Possibilidade A (mais provável) — Site não vinculado ao domínio no Hostinger
O plano de hospedagem existe, mas `jurisperitus.com.br` não está
adicionado como domínio principal na hospedagem.

**Solução:**
1. Acessar hPanel (painel.hostinger.com.br)
2. Ir em **Hospedagem** → seu plano → **Domínios**
3. Verificar se `jurisperitus.com.br` aparece na lista
4. Se não aparecer: clicar em **Adicionar domínio** → inserir `jurisperitus.com.br`

---

### Possibilidade B — Domínio adicionado mas pasta pública vazia
O domínio está vinculado, mas não há arquivos na pasta `public_html`.

**Solução:**
1. hPanel → **Gerenciador de Arquivos**
2. Navegar até `public_html/` (ou subpasta do domínio)
3. Verificar se há arquivos do site (index.html, wp-config.php etc.)
4. Se vazio: fazer upload do site / instalar WordPress

---

### Possibilidade C — Plano de hospedagem inativo/expirado
O plano Hostinger pode ter vencido ou estar suspenso.

**Solução:**
1. hPanel → **Faturamento** → verificar status do plano
2. Se suspenso: reativar ou renovar
3. Se vencido: contratar novo plano e vincular o domínio

---

## PASSO A PASSO COMPLETO PARA RESOLVER

```
1. Acessar: https://hpanel.hostinger.com
   → Fazer login com a conta usada na migração

2. Verificar status do plano:
   Hospedagem → [nome do plano] → Status
   ✅ Ativo  |  ❌ Suspenso/Expirado

3. Se ativo → ir em Domínios:
   Verificar se jurisperitus.com.br está listado como domínio do plano
   → Se não: Adicionar domínio → jurisperitus.com.br

4. Se domínio vinculado → Gerenciador de Arquivos:
   public_html/ → verificar se há conteúdo
   → Se vazio: o site precisa ser (re)instalado

5. Verificar se o site era WordPress:
   hPanel → WordPress → verificar instalações
   → Se aparece: clicar em Gerenciar → ativar
   → Se não aparece: reinstalar WordPress neste domínio

6. Após qualquer alteração: aguardar 5-30 minutos e testar:
   https://jurisperitus.com.br
```

---

## SOBRE /tutor E /diagnostico DURANTE A CORREÇÃO

**O /tutor (IP 18.208.88.157 — AWS EC2 separado) NÃO será afetado**
pela correção do Hostinger. São servidores distintos.

Porém: como o DNS agora é do Hostinger, se houver um registro A
apontando `/tutor` para o IP AWS, esse registro precisa ser preservado.

**Verificar no Hostinger (após acessar o hPanel):**
DNS → Zona DNS → procurar registros A com valor `18.208.88.157`
→ NÃO deletar esses registros

---

## SEQUÊNCIA CORRETA DE AÇÕES

```
ETAPA 1 — HOJE
└─ Corrigir jurisperitus.com.br no Hostinger (este documento)

ETAPA 2 — Após ETAPA 1 concluída e site funcionando
└─ Adicionar CNAME do blog no DNS Hostinger
   jurisperitusescolaonline → ghs.google.com

ETAPA 3 — Após ETAPA 2
└─ Configurar domínio customizado no Blogger
└─ Ativar redirecionamento blogspot → novo domínio

ETAPA 4 — 30 dias após ETAPA 3
└─ Solicitar aprovação Google AdSense
```

---

## INFORMAÇÕES A CONFIRMAR COM PROF. DR. FREIRE

1. O login do Hostinger (e-mail usado na migração)
2. Se o site era WordPress ou HTML puro
3. Se há backup do site disponível
4. Quais são as URLs exatas das planilhas vinculadas ao domínio

---

*Jurisperitus Escola Online | CNPJ: 55.274.545/0001-88*
*Claude Coworking — OS-07 Fase 0 — AG02 (Sites & SEO)*
