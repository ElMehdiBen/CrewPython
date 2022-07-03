from pymongo import MongoClient
import requests, json

with open("configs.json", "r") as config_file:
    configs = json.load(config_file)

def get_talents(url):
    payload, headers = {}, {}
    
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
    except Exception as e:
        print("Error: " + str(e))

    return response.json()

def mongo_connect(connection_string):
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(connection_string)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client

if __name__ == "__main__":    
    
    # Get the database
    client = mongo_connect(configs["mongo_url"])
    database = client[configs["mongo_db"]]
    collection = database[configs["mongo_collection"]]

    try:
        talents = get_talents(configs["api_url"])
        # replace field id with _id for all talents
        for talent in talents:
            talent["_id"] = talent["id"]
            del talent["id"]
        collection.insert_many(talents)
    except Exception as e:
        print(e)
        print("Error: Could not load talents from API")
        exit(1)

    