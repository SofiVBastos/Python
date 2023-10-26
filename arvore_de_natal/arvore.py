def arvoreDeNatal():
    tamanho = 10

    folha = "\033[92m\u22EF\033[0m"
    estrela = "\033[93m\u2605\033[0m"

    print(" "*9+estrela+" "*9)
    for i in range(1, tamanho + 1):
        espaco = tamanho - i
        texto = 2 * i - 1
        print(' ' * espaco + folha * texto)

    alturaBase = tamanho // 5
    larguraBase = tamanho // 5

    for _ in range(alturaBase):
        print(' ' * (tamanho - alturaBase) + '|' *  larguraBase)

    print(' ' * (tamanho // 2) + '\______/')

arvoreDeNatal()