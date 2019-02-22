def reverse_integer(number: int) -> int:
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:

    Input: 123
    Output: 321

    Example 2:

    Input: -123
    Output: -321

    Example 3:

    Input: 120
    Output: 21

    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

    >>> reverse_integer(543)
    345
    """
    limit = 2 ** 31 if number > 0 else -2 ** 31

    reversed_number = int(str(number)[::-1]) if number > 0 else int(str(number * -1)[::-1]) * -1

    if reversed_number.bit_length() >= limit.bit_length():
        return 0


    return reversed_number
