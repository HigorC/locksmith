import pymongo
import os

def getDb():
    client_url = os.environ.get("MONGO_CLIENT_URL", "mongodb://127.0.0.1:27018/?gssapiServiceName=mongodb")
    client = pymongo.MongoClient(client_url)
    print(client)
    db = client["locksmith"]
    print(db)
    return db
    # return pymongo.MongoClient(client_url)["locksmith"]