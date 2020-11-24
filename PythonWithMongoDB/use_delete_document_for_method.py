from PythonWithMongoDB.create_collection import main

"""
    To Delete Document from Collection we have 3 method : 
        1. delete_one()
        2. delete_many()
        3. delete_many({})
"""


def delete_one(query):
    collection_object = main()
    if collection_object.delete_one(query):
        print("Deletion of document is done")
    else:
        print("There is an error in deletion of document")


def delete_many(query):
    collection_object = main()
    delete_count = collection_object.delete_many(query)
    delete_count = delete_count.deleted_count
    if delete_count:
        print(f"Deletion of document is done and the total number of deleted documents : {delete_count}")
    else:
        print("There is an error in deletion of document")


def delete_all_documents():
    collection_object = main()
    delete_count = collection_object.delete_many({})
    delete_count = delete_count.deleted_count
    if delete_count == 0:
        print("Deletion of document is done and the total number of deleted documents")
    else:
        print("There is an error in deletion of document")


if __name__ == "__main__":
    delete_query = {"name": "Kanik Vijay"}
    delete_query1 = {"age": {"$eq": 21}}

    # calling functions:
    delete_one(delete_query)
    delete_many(delete_query1)
    delete_all_documents()