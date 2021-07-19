"""
Module containing test cases for the objective_1.py
Author: Shilpaj Bhalerao
Date: July 11, 2021
"""
# Standard Library Imports
import pytest

# Local Imports
from iterables import *


def is_namedtuple_instance(instance) -> bool:
    """
    Function to check whether a variable is an instance of a namedtuple
    :param instance: variable to be checked
    :return: True/False
    """
    # Check type and base classes
    _type = type(instance)
    _bases = _type.__bases__

    # Tuple is the parent class of namedtuple so if tuple is not present in bases then return False
    if len(_bases) != 1 or _bases[0] != tuple:
        return False

    # Named-tuples have _fields attributes like dictionary so return False if attributes are not instance of tuples
    fields_ = getattr(_type, '_fields', None)
    if not isinstance(fields_, tuple):
        return False

    return all(type(field) == str for field in fields_)


def test_custom_polygon_edges():
    """
    Test case to check if exceptions are raised when invalid value of edges is passed
    """
    with pytest.raises(ValueError):
        angle = Polygons(2, 5)

    with pytest.raises(ValueError):
        line = Polygons(1, 5)

    with pytest.raises(ValueError):
        line = Polygons(0, 5)

    with pytest.raises(ValueError):
        _ = Polygons(-5, 5)


def test_custom_polygon_circumradius():
    """
    Test case to check if exceptions are raised when invalid value of circumradius is passed
    """
    with pytest.raises(ValueError):
        _ = Polygons(3, 0)

    with pytest.raises(ValueError):
        line = Polygons(3, -3)


def test_custom_polygon_repr():
    """
    Test case to check if __repr__ method is implemented
    """
    # Create an object of the class
    _object = Polygons(3, 4)

    # Check if __repr__ method is present
    assert hasattr(_object, '__repr__')


def test_custom_polygon_len():
    """
    Test case to check if __len__ method is implemented
    """
    # Create an object of the class
    _object = Polygons(3, 4)

    # Check if __repr__ method is present
    assert hasattr(_object, '__len__')


def test_custom_polygon_getitem():
    """
    Test case to check if __getitem__ method is implemented
    """
    # Create an object of the class
    _object = Polygons(3, 4)

    # Check if __repr__ method is present
    assert hasattr(_object, '__getitem__')


def test_custom_polygon_max_efficiency():
    """
    Test case to check if __getitem__ method is implemented
    """
    # Create an object of the class
    _object = Polygons(3, 4)

    # Check if __repr__ method is present
    assert hasattr(_object, 'max_efficiency_polygon_edges')


def test_custom_polygon_max_efficiency_output():
    """
    Test case to return the number of edges of a polygon with maximum area:perimeter ratio
    """
    # Create an object of the class
    _object = Polygons(25, 4)

    # From the formula, it's clear that large the number of edges, larger the efficiency
    assert 25 == _object.max_efficiency_polygon_edges()


def test_getitem_inputs():
    """
    Test case to check positive, negative and zero indexing is supported by __getitem__ function
    """
    # Create an object of a class
    _sequence = Polygons(25, 5)

    # Assigning indexing outputs
    output_1 = _sequence[0]
    output_2 = _sequence[20]
    output_3 = _sequence[-20]

    # Check if all outputs are float and not None
    assert is_namedtuple_instance(output_1)
    assert is_namedtuple_instance(output_2)
    assert is_namedtuple_instance(output_3)


def test_getitem_raises():
    """
    Test case to check if proper errors are raised when wrong index are passed to __getitem__
    """
    # Create an object of a class
    _sequence = Polygons(25, 5)

    # Test if index error is raised when trying to access out of index values
    with pytest.raises(IndexError):
        _ = _sequence[25]

    # Test if index error is raised when trying to access out of index values
    with pytest.raises(IndexError):
        _ = _sequence[-25]


def test_getitem_slicing():
    """
    Test case to check if __getitem__ supports slicing
    """
    # List for comparison
    output_list = []

    # Create an object of a class
    _sequence = Polygons(25, 5)

    # Fetch the output one by one from the sequence and reverse the order
    [output_list.append(_sequence[index]) for index in range(len(_sequence))]
    output_list.reverse()

    # Fetch the output in reverse order using slicing
    calculated_output = _sequence[::-1]

    # Compare the result of above two outputs
    assert output_list == calculated_output


def test_len():
    """
    Test case to check if the length of object is correct
    """
    # Create an object of a class
    _sequence = Polygons(25, 5)

    # Check if the length is max_edges-2 since regular polygon starts with minimum 3 edges
    assert len(_sequence) == 23


def test_iterables():
    """
    Test case to check if Polygons is an Iterables and not Iterator
    """
    from collections.abc import Iterable, Iterator
    _obj = Polygons(25, 5)

    assert not isinstance(_obj, Iterator)
    assert isinstance(_obj, Iterable)
