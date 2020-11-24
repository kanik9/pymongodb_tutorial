from PythonWithMongoDB.create_collection import main


def drop_collection():
    collection_object = main()
    if collection_object.drop():
        print(f"'{collection_object.col_name}' Collection is Dropped ")
    else :
        print("Deletion of Collection have an error")


drop_collection()

