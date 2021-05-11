#!/usr/bin/env python3
""" Python module """


def list_all(mongo_collection):
    """
    list_all - lists all documents in a collection
    Args:
        - mongo_collection: mongodb collection object
    Return:
        - list of all documents in a collection
    """
    return mongo_collection.find()
