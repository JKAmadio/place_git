def aplicar_desconto(preco, percentual):
    valor = preco - (preco * percentual / 100)
    return round(valor, 2)
