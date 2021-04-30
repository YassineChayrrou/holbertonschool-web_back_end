# 0x09-Unittests_and_integration_tests

## Introduction:

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

This project will focus on creating unittests and integration tests for different sets of modules.

## Resources:

**read or watch**
- <a href="https://docs.python.org/3/library/unittest.html" target="_blank">unittest — Unit testing framework</a>
- <a href="https://docs.python.org/3/library/unittest.mock.html" target="_blank">unittest.mock — mock object library</a>
- <a href="https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock" target="_blank">How to mock a readonly property with mock?</a>
- <a href="https://pypi.org/project/parameterized/" target="_blank">parameterized</a>
- <a href="https://en.wikipedia.org/wiki/Memoization" target="_blank">Memoization</a>

## Objectives:

At the end of this project,we are expected to be able to explain to anyone, without the help of Google:
- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures

## Requirements:

Unittest : a python unit test framework

## Extras:
...

## Author:

Yassine Chayrrou
