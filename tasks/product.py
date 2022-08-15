from typing import Any

from itertools import combinations, zip_longest

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    if arr1 and arr2:
        res_arr = []
        for element1 in arr1:
            for element2 in arr2:
                res_arr.append((element1, element2))
        return res_arr
    else:
        return []
