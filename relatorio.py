def total_vendas(vendas):
    return sum(vendas)


def media_vendas(vendas):
    if not vendas:
        return 0
    return total_vendas(vendas) / len(vendas)
