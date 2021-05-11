#!/usr/bin/env python3
""" Python module """


def schools_by_topic(mongo_collection, topic):
    """
    schools_by_topic - returns db for documents matching query
    Args:
        - mongo_collection: mongodb collection object
        - topic: string, topic searched for 
    Return:
        - list of documents matching specific topic
    """
    return mongo_collection.find({"topics": topic})
