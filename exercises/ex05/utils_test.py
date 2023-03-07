"""Building List Ultility functions."""

__author__ = "730474369"

from exercises.ex05.utils import only_evens, sub, concat


def only_evens(xs: list[int]) -> list[int]:
    """Return a list of only the even numbers in the input list."""
    return [x for x in xs if x % 2 == 0]


def sub(s: str, start: int, end: int) -> str:
    """Return a substring of s starting from index start (inclusive) and ending at index end (exclusive)."""
    return s[start:end]


def concat(xs: list[str], separator: str) -> str:
    """Return a string that is the concatenation of all the strings in the input list separated by the separator."""
    return separator.join(xs)


# test cases

def test_only_evens_edge() -> None:
    """Test only_evens with an empty list."""
    assert only_evens([]) == []


def test_only_evens_use_one() -> None:
    """Test only_evens with a list of even numbers."""
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_only_evens_use_two() -> None:
    """Test only_evens with a list of odd numbers."""
    assert only_evens([1, 3, 5, 7]) == []


def test_sub_edge() -> None:
    """Test sub with an empty string."""
    assert sub("", 0, 0) == ""


def test_sub_use_one() -> None:
    """Test sub with a string and valid start and end indices."""
    assert sub("Hello, world!", 7, 12) == "world"


def test_sub_use_two() -> None:
    """Test sub with a string and invalid start and end indices."""
    assert sub("Hello, world!", 7, 20) == "world!"


def test_concat_edge() -> None:
    """Test concat with an empty list."""
    assert concat([], "") == ""


def test_concat_use_one() -> None:
    """Test concat with a list of one string."""
    assert concat(["Hello"], "") == "Hello"


def test_concat_use_two() -> None:
    """Test concat with a list of multiple strings."""
    assert concat(["Hello", "world"], "") == "Helloworld"


# The following code runs the test cases
if __name__ == "__main__":
    test_only_evens_edge()
    test_only_evens_use_one()
    test_only_evens_use_two()
    test_sub_edge()
    test_sub_use_one()
    test_sub_use_two()
    test_concat_edge()
    test_concat_use_one()
    test_concat_use_two()