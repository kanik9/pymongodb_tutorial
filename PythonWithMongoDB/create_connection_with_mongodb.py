# Importing Library to use
import pymongo as mongo
import json


# Creating the Clint to interact with Databases

def create_connection_with_mongodb_and_database(conn_url, database_name):
    my_client = mongo.MongoClient(conn_url)
    # Create or find that database is exist or not .
    """
        my_db = my_client["Database_name"]
    """
    my_db = my_client[database_name]

    db_list = my_client.list_database_names()
    if database_name in db_list:
        print(f"The database exists. And the name is '{database_name}'")
    return my_db


""""
if __name__ == "__main__":
    url = "mongodb://127.0.0.1:27017/"
    database_name = "practice"
    ans = create_connection_with_mongodb_and_database(conn_url=url,
                                                database_name=database_name)
"""