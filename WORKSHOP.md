# Workshop de Git - roteiro e branches

Guia das branches preparadas para o workshop. Cada topico tem seu proprio
conjunto de branches, isolado dos demais, para que cada pessoa possa
experimentar sem afetar o exercicio de outra.

Para comecar, todo mundo deve buscar todas as branches:

```
git fetch origin
git branch -r
```

E criar uma branch local de acompanhamento para a que for usar, por exemplo:

```
git checkout -b exercicio/rebase-conflito origin/exercicio/rebase-conflito
```

## 1. Gitflow - estrutura de mudancas coexistindo

Branches: `main`, `develop`, `feature/autenticacao`, `feature/relatorio-vendas`,
`feature/exportar-csv` (ja integrada em `develop`), `release/1.1.0`,
`hotfix/1.0.1`.

Visualize tudo de uma vez:

```
git log --oneline --graph --all --decorate
```

Discussao / exercicios:

- Identifiquem, so pelo grafico, qual feature ja foi integrada e quais ainda
  estao em andamento.
- Por que `hotfix/1.0.1` parte de `main` e nao de `develop`?
- Exercicio pratico: "fechem" a release. Isso envolve normalmente:
  1. Merge de `release/1.1.0` em `main` (`--no-ff`) + tag `v1.1.0`.
  2. Merge de `release/1.1.0` de volta em `develop` (para nao perder o bump
     de versao).
- Exercicio pratico: apliquem `hotfix/1.0.1` tanto em `main` quanto em
  `develop`.

## 2. Rebase e conflitos

Branch: `exercicio/rebase-conflito`.

Ela e `main` mudaram a mesma linha de `app.py` e a mesma secao de
`CHANGELOG.md` de formas diferentes - um conflito garantido.

```
git checkout exercicio/rebase-conflito
git rebase main
```

Resolvam o conflito, `git add`, `git rebase --continue`. Depois discutam:

- O que muda no historico depois do rebase (hashes, ordem, "quem teria feito
  isso primeiro")?
- Por que rebasear uma branch que outras pessoas ja usam e arriscado?
- Se preferirem abortar tudo e comecar de novo: `git rebase --abort`.

## 3. Stash vs commit WIP vs Worktree

Branch: `exercicio/stash-wip-worktree` (contem o roteiro completo em
`EXERCICIO_STASH_WIP_WORKTREE.md`).

Esse exercicio e feito na hora, ja que stash e worktree sao mecanismos locais.

## 4. Tipos de mesclagem

Quatro branches, cada uma isolando um tipo de merge a partir de `main`:

- `exercicio/merge-fast-forward`: `main` nao andou desde que a branch foi
  criada -> `git merge` faz fast-forward puro (tente tambem
  `git merge --no-ff` para comparar o resultado).
- `exercicio/merge-three-way`: `main` e a branch divergiram, mas em arquivos
  diferentes -> merge automatico, com commit de merge (estrategia
  recursiva/`ort`).
- `exercicio/merge-squash`: tres commits "sujos" (`wip`, `wip: ...`,
  `corrige typo...`) para condensar com `git merge --squash`.
- `exercicio/merge-conflito`: divergencia real na mesma secao do
  `CHANGELOG.md` -> conflito de verdade para resolver manualmente.

Para cada uma, a partir de `main`:

```
git checkout main
git merge exercicio/merge-fast-forward
# desfaça com: git reset --hard origin/main (antes de fazer push)
```

Depois de cada teste, se nao quiserem manter o resultado local, resetem
`main` local para `origin/main` antes de tentar o proximo tipo de merge.

## 5. Reset vs Revert + Reflog

Branch: `exercicio/reset-revert` (roteiro completo em
`EXERCICIO_RESET_REVERT_REFLOG.md`).

Resumo: a branch tem um commit com bug no meio do historico. A Parte 1 usa
`git revert` (seguro, nao reescreve historico). A Parte 2 e a Parte 3 devem
ser feitas numa branch descartavel (`sandbox-reset`) e exploram
`git reset --soft/--mixed/--hard` e a recuperacao via `git reflog`.

## Convite para interagir

Sintam-se livres para:

- Criar branches proprias a partir de qualquer uma destas para testar
  variacoes (ex: `exercicio/rebase-conflito-<seu-nome>`).
- Quebrar de propositos e usar `git reflog` para se recuperar - esse
  repositorio existe para isso.
