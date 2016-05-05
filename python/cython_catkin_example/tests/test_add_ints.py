#!/usr/bin/env python

from nose.tools import assert_equal


def test_add_ints():
    from cython_catkin_example.add_ints import add_ints
    assert_equal(add_ints(1, 3), 4)
