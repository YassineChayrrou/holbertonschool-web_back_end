#!/usr/bin/env python3
""" Python module """


def update_topics(mongo_collection, name, topics):
    """
    update_topics - updates collection documents
    Args:
        - mongo_collection: mongodb collection object
        - name: value to match with in collection documents
        - topics: field to update in collection documents
    Return: [no return]
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
