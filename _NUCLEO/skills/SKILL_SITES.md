# SKILL: SITES JURISPERITUS
## Versão 1.0 | Claude Coworking

## QUANDO USAR
Ao atualizar, corrigir ou criar páginas em qualquer domínio da Jurisperitus.

## MAPA DE DOMÍNIOS

| Domínio | Infraestrutura | Deploy | Status |
|---------|---------------|--------|--------|
| jurisperitus.com.br | GitHub Pages | git push origin main | ✅ Ativo |
| jurisperitusescolaonline.com.br | Cloudflare CDN | Website Builder Hostinger | ✅ Ativo |
| professorfreire.com.br | IP 88.223.87.136 | A confirmar | ⏳ |
| professorfreire.com | A confirmar | A confirmar | ⏳ |
| advogadodagramatica.com.br | A confirmar | A confirmar | ⏳ |
| portuguesinesquecivel.com.br | A confirmar | A confirmar | ⏳ |

## REPOSITÓRIO GITHUB
- Usuário: jurisperitusescolaonline-crypto
- Repo: jurisperitus-coworking
- Branch principal: main
- Pasta pública: /docs
- Deploy: automático via GitHub Pages

## COMANDO DE DEPLOY (jurisperitus.com.br)
```bash
cd /home/claude/jurisperitus
python3 deploy.py "descrição da alteração"
```

## ESTRUTURA /docs
```
docs/
├── index.html          ← Landing page principal
├── CNAME               ← jurisperitus.com.br
├── tutor/
│   └── index.html      ← Professor de Português IA
└── diagnostico/
    └── index.html      ← Quiz de nível
```

## PADRÃO VISUAL OBRIGATÓRIO
- Azul: #003B83
- Dourado: #FFB400
- Branco: #FFFFFF
- Fonte título: Cormorant Garamond
- Fonte corpo: DM Sans
- Rodapé: "Jurisperitus Escola Online | CNPJ: 55.274.545/0001-88 | Brasília/DF"

## WEB3FORMS (captura de leads)
- Access key: ca893d25-4ac0-43c2-b917-8a39c39040b9
- Leads chegam por e-mail após envio do formulário
- Endpoint: https://api.web3forms.com/submit

## CHECKLIST ANTES DE DEPLOYAR
- [ ] HTML válido (sem tags abertas)
- [ ] Cores corretas (#003B83 / #FFB400)
- [ ] Rodapé institucional presente
- [ ] CTA apontando para jurisperitusescolaonline.com.br ou produto Hotmart
- [ ] Responsivo (mobile-first)
