#!/usr/bin/env python3
""" Python module """


def top_students(mongo_collection):
    """
    top_students - function that returns all students sorted by average score
    Args:
        - mongo_collection: mongodb database pymongo collection object
    Return:
        - list of students sorted by average score
    """

    pipeline = [
            {
                "$addFields":
                {
                    "averageScore":
                    {
                        "$divide": [
                            {"$sum": "$topics.score"},
                            {"$size": "$topics.score"}
                        ]
                    }
                }
            },
            {
                "$sort": {"averageScore": -1}
            }
        ]
    return list(mongo_collection.aggregate(pipeline))
