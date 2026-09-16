# Exercicio: Reset vs Revert + Reflog

Esta branch tem 4 commits sobre `main`:

```
git log --oneline main..exercicio/reset-revert
```

1. `Adiciona funcao de calculo de desconto` (ok)
2. `Corrige arredondamento no calculo de desconto` (ok)
3. `Ajusta formula de desconto` (BUG: trocou subtracao por soma - o
   "desconto" na verdade aumenta o preco)
4. `Adiciona logging ao calculo de desconto` (ok, ja em cima do bug)

## Parte 1 - Revert (branch ja compartilhada/publicada)

Trate esta branch como se ja tivesse sido enviada para o repositorio remoto
e outras pessoas tivessem baseado trabalho nela - ou seja, **reescrever o
historico aqui seria perigoso**.

1. Identifique o hash do commit com bug: `git log --oneline`.
2. Rode `git revert <hash-do-commit-3>`.
3. Observe que o Git consegue aplicar o revert mesmo havendo um commit
   (o de logging) por cima do commit ruim, e que um commit NOVO e criado
   desfazendo apenas aquela mudanca - o historico original continua visivel.
4. Confira `desconto.py`: o calculo voltou a subtrair o percentual?

## Parte 2 - Reset (trabalho local, ainda nao compartilhado)

Faca esta parte numa branch descartavel, para nao perder o resultado do
Parte 1:

```
git branch sandbox-reset exercicio/reset-revert
git checkout sandbox-reset
```

1. `git reset --soft HEAD~1` - o que aconteceu com o working directory?
   E com a staging area? (`git status`, `git diff --staged`)
2. `git commit` de novo para voltar ao estado anterior, depois
   `git reset --mixed HEAD~1` (ou so `git reset HEAD~1`) - qual a diferenca
   para o `--soft`?
3. `git commit` de novo, depois `git reset --hard HEAD~1` - o que sumiu?
4. Discuta: por que `reset --hard` em uma branch ja compartilhada e
   arriscado, mas `revert` e seguro?

## Parte 3 - Reflog (recuperando o "perdido")

Ainda em `sandbox-reset`:

1. Rode `git reflog` e encontre a entrada de ANTES do `reset --hard`.
2. Recupere o commit "perdido" com:
   `git reset --hard <hash-encontrado-no-reflog>`
   (ou, se preferir manter o estado atual, `git cherry-pick <hash>`)
3. Confirme com `git log --oneline` que o commit voltou.

## Sintese

| Ferramenta | Reescreve historico? | Seguro em branch compartilhada? |
|---|---|---|
| `git revert` | Nao (cria commit novo) | Sim |
| `git reset` | Sim (move o ponteiro da branch) | So localmente, antes do push |
| `git reflog` | N/A - e uma rede de seguranca | Ajuda a recuperar apos um reset errado |
