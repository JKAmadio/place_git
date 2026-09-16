def saudacao(nome):
    if not nome:
        nome = "visitante"
    return f"Ola, {nome}!"


def soma(a, b):
    return a + b


if __name__ == "__main__":
    print(saudacao("equipe"))
