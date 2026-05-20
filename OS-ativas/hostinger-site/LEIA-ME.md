# INSTRUÇÕES DE UPLOAD — jurisperitus.com.br
## Claude Coworking | Jurisperitus

---

## ARQUIVOS DESTE PACOTE

| Arquivo | Destino no Hostinger | Descrição |
|---------|---------------------|-----------|
| `index.html` | `public_html/index.html` | Landing page de captura |
| `.htaccess` | `public_html/.htaccess` | Redirects + HTTPS + segurança |

---

## PASSO A PASSO DE UPLOAD

1. Acessar **hpanel.hostinger.com** → Hospedagem → Gerenciador de Arquivos
2. Navegar até a pasta **public_html/**
3. Se houver arquivos antigos: fazer backup antes de substituir
4. Fazer upload de `index.html` e `.htaccess`
5. Testar: abrir https://jurisperitus.com.br no navegador

---

## PERSONALIZAÇÃO OBRIGATÓRIA ANTES DO UPLOAD

### 1. Formulário de captura — integrar com lista de e-mails
Abrir `index.html` e localizar a linha:
```
action="https://formspree.io/f/SEU_ID_AQUI"
```

Substituir pela URL real. Opções:

**Formspree (gratuito, mais simples):**
- Acessar formspree.io → criar conta → New Form
- Copiar o ID gerado → substituir `SEU_ID_AQUI`

**RD Station / ActiveCampaign / Hotmart:**
- Substituir o `<form>` pelo código de embed da plataforma

---

### 2. Redirects /tutor e /diagnostico
Abrir `.htaccess` e substituir:
```
COLE_AQUI_URL_NETLIFY_TUTOR        → URL real do projeto tutor no Netlify
COLE_AQUI_URL_NETLIFY_DIAGNOSTICO  → URL real do projeto diagnóstico no Netlify
```

Para encontrar as URLs:
- Acessar app.netlify.com
- Clicar em cada projeto
- Copiar a URL em "Domain settings" (formato: nome-projeto.netlify.app)

---

## APÓS O SITE NO AR — PRÓXIMOS PASSOS

1. ✅ Site de captura funcionando em jurisperitus.com.br
2. ⬜ Testar /tutor e /diagnostico (redirects funcionando)
3. ⬜ Integrar formulário com lista de e-mails
4. ⬜ Adicionar CNAME do blog no DNS Hostinger
5. ⬜ Configurar domínio customizado no Blogger
6. ⬜ Conectar Google Analytics / Search Console

---

*Jurisperitus Escola Online | CNPJ: 55.274.545/0001-88*
*Claude Coworking — OS-07*
