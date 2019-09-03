import pymongo
import os

# Startar mongo local na 27018
#  mongod --dbpath C:\ws\dbs-mongodb\locksmith-27018 --port 27018
#  mongod --dbpath C:\hc\db2-mongo --port 27018

def getDb():
    client_url = os.environ.get("MONGO_CLIENT_URL", "mongodb://127.0.0.1:27018/?gssapiServiceName=mongodb")
    client = pymongo.MongoClient(client_url)
    print(client)
    db = client["locksmith"]
    print(db)
    return db
    # return pymongo.MongoClient(client_url)["locksmith"]