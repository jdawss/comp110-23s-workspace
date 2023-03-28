"""EX07 assignment."""

__author__ = "730474369"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and the values."""
    new_dict_1: dict[str, str] = {}
    for elem in dict_1:
        new_dict_1[dict_1[elem]] = elem
    if len(new_dict_1) < len(dict_1):
        raise KeyError("Cannot have multiple of the same key!")
    return new_dict_1


def favorite_color(dict_2: dict[str, str]) -> str:
    """Return color that appears most frequently."""
    highest: int = 0
    counter: dict[str, int] = {}
    fav_color: str = ""
    for elem in dict_2:
        the_color = dict_2[elem]
        if the_color in counter:
            counter[the_color] += 1
        else:
            counter[the_color] = 1
        if counter[the_color] > highest:
            highest = counter[the_color]
            fav_color = the_color
    return fav_color


def count(nums: list[str]) -> dict[str, int]:
    """Return new dict based on numbers."""
    addition: dict[str, int] = {}
    for val in nums:
        if val in addition:
            addition[val] += 1
        else:
            addition[val] = 1
    return addition
        
        