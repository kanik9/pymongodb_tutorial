from PythonWithMongoDB.create_connection_with_mongodb import create_connection_with_mongodb_and_database


def create_collection(conn_url, database_name, collection_name):
    my_db_object = create_connection_with_mongodb_and_database(conn_url=conn_url,
                                                               database_name=database_name)
    # Create Collection of collection name
    collection = my_db_object[collection_name]

    return collection


def main():
    url = "mongodb://127.0.0.1:27017/"
    database_name = "practice"
    col_name = "Employee1"
    collection_object = create_collection(conn_url=url,
                                          database_name=database_name,
                                          collection_name=col_name)

    return collection_object
