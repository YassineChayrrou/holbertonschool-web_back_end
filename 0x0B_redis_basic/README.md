# 0x0B. Redis basic

An introductory project to Redis

## Resources:

**Read or watch:**
- <a href="https://redis.io/commands" target="_blank">Redis commands</a>
- <a href="https://redis-py.readthedocs.io/en/stable/" target="_blank">Redis python client</a>
- <a href="https://realpython.com/python-redis/" target="_blank">How to use Redis with python</a>
- <a href="https://www.youtube.com/watch?v=Hbt56gFj998" target="_blank">Redis crash course tutorial</a>

## Objectives:


- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache

## Extras:

few tips and trics in this project:

- <a href="https://docs.python.org/3.7/library/functools.html#functools.wraps" target="_blank">functools.wraps</a> a very convinient way to use for a decorator, in this project i used this to implement a counting functionality of how many times a method was invoked, i also used **method.__qualname__** to set as key for my counter.
- __qualname__ is very useful for debugging however in this case to set apart different methods from each class when stored in redis database so that if a method name was to be repeated in other class we don't have overlapping keys and values would be overriden if keys where stored using **method.__name__**

## Author:

YassineChayrrou
