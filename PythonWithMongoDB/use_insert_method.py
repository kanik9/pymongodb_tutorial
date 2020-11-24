from PythonWithMongoDB.create_collection import main


def insert_one(query):
    collection_object = main()
    insert_query_execute = collection_object.insert_one(query)
    """
    For getting the inserted object id as an output for insert_one() method use 'inserted_id'
    
    1. If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.
    2. In the example above no _id field was specified, so MongoDB assigned a unique _id for the record (document).
    """
    print(insert_query_execute.inserted_id)


def insert_many(query):
    """"
    The insert_many() method returns a InsertManyResult object, which has a property, inserted_ids, that holds the ids
    of the inserted documents.
    """
    collection_object = main()
    insert_query_execute = collection_object.insert_many(query)
    print(insert_query_execute.inserted_ids)


def insert(query):
    """
    This will Show warning {Use 'Insert one' and 'Insert Many' for insert operation}
    """
    collection_object = main()
    insert_query_execute = collection_object.insert(query)
    print("Inserted Data : \n", insert_query_execute)


if __name__ == "__main__":
    data_dict = {
        "name": "Kanik Vijay",
        "class": "General",
        "gender": "Male",
        "age": 21
    }
    data_dict1 = [
        {
            "name": "Ram Vijay",
            "class": "General",
            "gender": "Male",
            "age": 22
        },
        {
            "name": "Jay Sharma",
            "class": "General",
            "gender": "Male",
            "age": 20
        },
        {
            "name": "Ajay Malawat",
            "class": "SC",
            "gender": "Male",
            "age": 25
        },
        {
            "name": "Vijay Kumar",
            "class": "General",
            "gender": "Male",
            "age": 21
        }
    ]

    insert_one(query=data_dict)
    insert_many(query=data_dict1)
    # insert(query=data_dict1)
