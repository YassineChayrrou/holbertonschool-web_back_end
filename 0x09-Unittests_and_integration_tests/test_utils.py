#!/usr/bin/env python3


import unittest
from utils import access_nested_map
from parameterized import parameterized, param


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test_access_nested_map - test method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
