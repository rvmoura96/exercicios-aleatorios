from functools import lru_cache


@lru_cache
def fib(self, number: int) -> int:
    if number == 0 or number == 1:
        return number

    if number > 1:
        number = self.fib(number - 1) + self.fib(number - 2)

    return number
