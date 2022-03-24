from array import array
from ctypes import Array
from typing import Tuple


def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    first: int = 0
    last: int = len(numbers)-1
    while first <= last:
        middle: int = int((first+last)/2)
        if numbers[middle] == value:
            return True, middle
        if numbers[middle] < value:
            first += 1
            if numbers[middle] > value:
                last -= 1
    return False, -1
