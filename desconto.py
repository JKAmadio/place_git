def aplicar_desconto(preco, percentual):
    valor = preco + (preco * percentual / 100)
    return round(valor, 2)


def descricao_desconto(percentual):
    return f"Desconto de {percentual}% aplicado"
