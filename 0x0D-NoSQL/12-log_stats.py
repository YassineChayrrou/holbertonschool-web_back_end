#!/usr/bin/env python3
""" Python module """


from pymongo import MongoClient


client = MongoClient()
db = client.logs
mongo_collection = db.nginx

GET = mongo_collection.count_documents({"method": "GET"})
POST = mongo_collection.count_documents({"method": "POST"})
PUT = mongo_collection.count_documents({"method": "PUT"})
PATCH = mongo_collection.count_documents({"method": "PATCH"})
DELETE = mongo_collection.count_documents({"method": "DELETE"})
STATUS = mongo_collection.count_documents({"method": "GET", "path": "/status"})
LOGS = mongo_collection.count_documents({})
screen = f"""
{LOGS} logs
Methods:
    method GET: {GET}
    method POST: {POST}
    method PUT: {PUT}
    method PATCH: {PATCH}
    method DELETE: {DELETE}
{STATUS} status check
"""
print(screen.strip())
