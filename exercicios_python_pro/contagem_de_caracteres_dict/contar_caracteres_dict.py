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
    retorno = dict()

    for caracter in palavra:
        retorno[caracter] = retorno.get(caracter, 0) + 1

    return retorno
