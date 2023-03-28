"""Test file for EX07."""

__author__ = "730474369"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


# test for invert function
def test_invert_edge_case():
    """Test invert function with an empty dictionary."""
    assert invert({}) == {}


def test_invert_use_case_1():
    """Test invert function with a dictionary containing unique keys and values."""
    assert invert({"a": "1", "b": "2", "c": "3"}) == {"1": "a", "2": "b", "3": "c"}


def test_invert_use_case_2():
    """Test invert function with a dictionary containing duplicate values."""
    with pytest.raises(KeyError):
        invert({"a": "1", "b": "2", "c": "1"})


# test for favorite_color function
def test_favorite_color_edge_case():
    """Test favorite_color function with an empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_use_case_1():
    """Test favorite_color function with a dictionary containing one most frequent color."""
    assert favorite_color({"steve": "red", "jobs": "green", "jon": "red"}) == "red"


def test_favorite_color_use_case_2():
    """Test favorite_color function with a dictionary containing multiple most frequent colors."""
    assert favorite_color({"steve": "red", "jobs": "green", "jon": "green", "dawson": "blue", "joel": "blue"}) == "green"


# test for count function
def test_count_edge_case():
    """Test count function with an empty list."""
    assert count([]) == {}


def test_count_use_case_1():
    """Test count function with a list containing unique values."""
    assert count(["1", "2", "3"]) == {"1": 1, "2": 1, "3": 1}


def test_count_use_case_2():
    """Test count function with a list containing duplicate values."""
    assert count(["1", "2", "2", "3", "3", "3"]) == {"1": 1, "2": 2, "3": 3}