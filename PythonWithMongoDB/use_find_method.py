from PythonWithMongoDB.create_collection import main


def find_one():
    """
     1. To select data from a collection in MongoDB, we can use the find_one() method.
     2. The find_one() method returns the first occurrence in the selection.
    """
    collection_object = main()
    data = collection_object.find_one()
    print(f"The Data of collection '{collection_object.col_name}' \n Data : {data}")


def find_all():
    """
    1. To select data from a table in MongoDB, we can also use the find() method.
    2. The find() method returns all occurrences in the selection.
    3. The first parameter of the find() method is a query object. In this example we use an empty query object,
       which selects all documents in the collection.
    """
    collection_object = main()
    data = collection_object.find()
    for ele in data:
        print(f"The Data of collection '{collection_object.col_name}' \n Data : {ele}")


def find_with_filter_columns():
    """
    1. The second parameter of the find() method is an object describing which fields to include in the result.
    2. This parameter is optional, and if omitted, all fields will be included in the result.
    """
    collection_object = main()
    data = collection_object.find({},
                                  {"name": 1,
                                   "class": 1,
                                   "gender": 1})
    """
    Warning : You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the 
              _id field). If you specify a field with the value 0, all other fields get the value 1, and vice versa
    """
    for ele in data:
        print(f"The Data of collection '{collection_object.col_name}' \n Data : {ele}")


if __name__ == "__main__":
    find_with_filter_columns()