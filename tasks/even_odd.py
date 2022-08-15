__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    sum_even, sum_odd = 0, 0
    for number in arr:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number
    return sum_even / sum_odd if sum_odd else 0
