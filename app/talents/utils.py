from pymongo import MongoClient
import json

with open("../conf.json", "r") as config_file:
    configs = json.load(config_file)

def mongo_connect(CONNECTION_STRING):
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client

def mongo_connect_talents():
    client = mongo_connect(configs["mongo_url"])
    database = client[configs["mongo_db"]]
    collection = database[configs["mongo_collection"]]
    return collection