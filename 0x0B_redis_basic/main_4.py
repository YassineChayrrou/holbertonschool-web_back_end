#!/usr/bin/env python3
""" Main module"""


from exercise import Cache, replay


cache = Cache()


cache.store("foo")
cache.store("bar")
cache.store(42)
cache.store(32)


replay(cache.store)
