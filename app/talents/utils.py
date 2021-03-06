from pymongo import MongoClient
import json

with open("../configs.json", "r") as config_file:
    configs = json.load(config_file)

def mongo_connect(connection_string):
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(connection_string)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client

def mongo_connect_talents():
    client = mongo_connect(configs["mongo_url"])
    database = client[configs["mongo_db"]]
    collection = database[configs["mongo_collection"]]
    return collection