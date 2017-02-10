from pymongo import MongoClient

client = MongoClient()

DB = client.mydb

def mycol():
    return DB.mycol.find()