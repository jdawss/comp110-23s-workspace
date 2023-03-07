"""Building List Ultility functions."""

__author__: "730474369"


def only_evens(ev_list: list[int]) -> list[int]:
    """Finding and returning only the even numbers in a list."""
    even_list = []
    for num in ev_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Generating a new list which contains all of the elements of the first followed by the second."""
    result = []
    for object in list_one:
        result.append(object)
    for object in list_two:
        result.append(object)
    return result


def sub(a_list: list[str], idx_start: int, idx_end: int) -> list[int]:
    """Generates a list that is a subset of the given list."""
    if len(a_list) == 0 or idx_start >= len(a_list) or idx_end <= 0:
        return [] 
    result = []
    if idx_start < 0:
        idx_start = 0
    if idx_end > len(a_list):
        idx_end = len(a_list)
    for idx in range(idx_start, idx_end):
        result.append(a_list[idx])
    return result