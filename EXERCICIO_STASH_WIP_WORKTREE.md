# Exercicio: Stash vs Commit WIP vs Worktree

Diferente dos outros exercicios, este nao pode vir pronto em commits: stash e
worktree sao mecanismos locais (nao viajam no `git push`). Siga os passos na
sua propria copia do repositorio, nesta branch.

## Cenario

Voce esta no meio de uma alteracao em `app.py` quando alguem pede para voce
revisar com urgencia a `hotfix/1.0.1`.

## Parte 1 - Stash

1. Edite `app.py` (ex: mude o texto de `saudacao`) e NAO faca commit.
2. Rode `git status` para ver a mudanca suja.
3. Rode `git stash push -m "ajuste saudacao"`.
4. Confirme que `git status` esta limpo e que `app.py` voltou ao original.
5. Troque para `hotfix/1.0.1`, revise o arquivo, volte para esta branch.
6. Rode `git stash list` e depois `git stash pop` para recuperar o trabalho.

Pergunta para discussao: o que aconteceria se voce tivesse trocado de branch
com o `app.py` sujo, sem stash?

## Parte 2 - Commit WIP

1. Faca outra alteracao incompleta em `app.py`.
2. Em vez de stash, rode `git commit -m "WIP: ajuste em andamento"`.
3. Continue o trabalho e finalize com `git commit --amend` ou um novo commit.
4. Compare: quando faz mais sentido commitar um WIP em vez de usar stash?
   (dica: pense em maquinas diferentes, backup, ou pausas longas)

## Parte 3 - Worktree

Em vez de trocar de branch (e ter que guardar/recuperar o trabalho sujo),
`git worktree` cria uma segunda pasta de trabalho apontando para outra
branch do mesmo repositorio, ao mesmo tempo.

1. Sem sair desta branch, rode:
   `git worktree add ../place_git-hotfix hotfix/1.0.1`
2. Abra a nova pasta `../place_git-hotfix` em outra aba/janela e revise o
   hotfix, sem afetar o que esta aberto aqui.
3. Quando terminar, rode `git worktree remove ../place_git-hotfix`.

Pergunta para discussao: quando `worktree` resolve melhor que `stash`?

## Sintese

| Situacao | Ferramenta |
|---|---|
| Pausa curta, mesma branch, resolvo em minutos | `git stash` |
| Quero registrar progresso, backup, ou trocar de maquina | commit `WIP` (+ squash/amend depois) |
| Preciso trabalhar em duas branches ao mesmo tempo, sem alternar contexto | `git worktree` |
