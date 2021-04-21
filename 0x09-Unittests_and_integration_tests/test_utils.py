#!/usr/bin/env python3
"""unittest module for utils.py"""


import unittest

from parameterized import parameterized
from unittest.mock import patch, MagicMock

from utils import access_nested_map, get_json, memoize


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

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test_access_nested_map_exception - test method """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ TestGetJson class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json function
        """
        with patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ class for unittest memoize
    """

    def test_memoize(self):
        """ test_memoize method tests an object within main class
            uses patch.object to mock an object within TestMemoize
        """
        class TestClass:
            """TC class treated as object within TestMemoize"""

            def a_method(self):
                """method of TestClass"""
                return 42

            @memoize
            def a_property(self):
                """method memoized using @memoize decorator reference"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            x = TestClass()
            self.assertEqual(x.a_property, mock.return_value)
            self.assertEqual(x.a_property, mock.return_value)
            mock.assert_called_once()
