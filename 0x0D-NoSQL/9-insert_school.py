#!/usr/bin/env python3
""" python module """


def insert_school(mongo_collection, **kwargs):
    """
    insert_school - fucntion that inserts a new document in a collection based
                    on kwargs
    Args:
        - mongo_collection: mongodb collection object
        - **kwargs: keyword arguments to pass contains keys and values of what
                    what to insert in DB
    Return:
        - _id of inserted document in a collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
