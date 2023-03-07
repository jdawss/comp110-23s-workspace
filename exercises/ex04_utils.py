"""Practice with lists and implementing them."""


__author__ = "730474369"


def all(num_list: list[int], num_test: int) -> bool:
    """Goes through the list and returns a bool."""
    idx_all: int = 0
    if len(num_list) == 0:
        return False
    while idx_all < len(num_list):
        if num_test != num_list[idx_all]:
            return False
        idx_all += 1
    return True


def max(input_list: list[int]) -> int:
    """Returns max integer of the list."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    idx_max: int = 0
    value_max: int = input_list[0]
    while idx_max < len(input_list):
        if input_list[idx_max] > value_max:
            value_max = input_list[idx_max]
        idx_max += 1
    return value_max


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Returns a bool from comparison of both lists."""
    if len(list_one) != len(list_two):
        return False
    idx_list: int = 0
    while idx_list < len(list_one):
        if list_one[idx_list] != list_two[idx_list]:
            return False
        idx_list += 1
    return True