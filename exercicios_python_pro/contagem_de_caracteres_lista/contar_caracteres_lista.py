def contagem_caracteres(palavra: str) -> list:
    """Realiza a contagem dos caracteres em uma string.

    Retornará a seguinte estrutura de dados:
    [
        ('caracter', número de ocorrências),
        ('caracter', número de ocorrências),
    ]

    exempplo palavra possui o valor 'ovo':
    retorno = [('o', 2), ('v', 1)]

    >>> contagem_caracteres('ovo')
    [('o', 2), ('v', 1)]
    """
    contador = 1
    caracteres_ordenados = sorted(palavra)
    caracter_anterior = caracteres_ordenados[0]
    retorno = list()

    for caracter in caracteres_ordenados[1:]:
        if caracter != caracter_anterior:
            retorno.append((caracter_anterior, contador))
            caracter_anterior = caracter
            contador = 1
        else:
            contador += 1
    retorno.append((caracter_anterior, contador))

    return retorno
