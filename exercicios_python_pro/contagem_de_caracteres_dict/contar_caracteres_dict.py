def contagem_caracteres(palavra: str) -> dict:
    """Realiza a contagem dos caracteres em uma string.

    Retornará a seguinte estrutura de dados:
    {
        'caracter': número de ocorrências,
        'caracter': número de ocorrências,
    }

    exemplo palavra possui o valor 'ovo':
    retorno = {
        'o': 2,
        'v': 1
    }

    >>> contagem_caracteres('ovo')
    {'o': 2, 'v': 1}
    """
    caracteres_ordenados = sorted(palavra)
    caracter_anterior = caracteres_ordenados[0]
    retorno = dict()

    for caracter in caracteres_ordenados[1:]:
        if caracter != caracter_anterior:
            retorno[caracter_anterior] = retorno.get(caracter_anterior, 0) + 1
            caracter_anterior = caracter
        else:
            retorno[caracter_anterior] = retorno.get(caracter_anterior, 0) + 1

    retorno[caracter_anterior] = retorno.get(caracter_anterior, 0) + 1

    return retorno
