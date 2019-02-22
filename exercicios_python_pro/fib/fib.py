def fib(number: int) -> int:
    """
    >>> fib(2)
    1

    >>> fib(0)
    0
    """
    if number <= 1:
        return number

    else:
        while number > 1:
            number = (number - 1) + (number - 2)

        return number
