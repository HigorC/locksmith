import db.mongo_connection as mongo_connection
from pymongo import ReturnDocument

def getSecretByUserIdAndAppName(userId, appName):
    db = mongo_connection.getDb()
    userFounded = db["users"].find_one({"idLoginme": userId})

    appFounded = list(filter(lambda x: x["name"] == appName, userFounded["applications"]))[0]
    return appFounded["secret"]