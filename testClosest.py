'''
Closest pair problem tests

Tests the solution for the closest pair of numbers problem.

Usage:

    python closest_pair.py [size of list of numbers]

[Jesse Melanson, Makenna Worley]

[8/21/24]
'''
import pytest
import Closest

def testClosest1():
    # Create list
    testList1 = [-13, 5, 18, 7, -14, 21]

    # Expected value
    expected = (-13, -14)

    # assert actual == expected
    assert Closest.closest_pair(testList1) == expected

def testClosest2():
    # Create list
    testList1 = [-13, 5, 18, 7, -14, 21, -13]

    # Expected value
    expected = (-13, -13)

    # assert actual == expected
    assert Closest.closest_pair(testList1) == expected