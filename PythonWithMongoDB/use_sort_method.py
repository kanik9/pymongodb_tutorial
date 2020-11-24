from PythonWithMongoDB.create_collection import main

"""
    sort("name", 1) #ascending
    sort("name", -1) #descending
"""


def apply_sort_default_ascending(sorted_column):
    collection_object = main()
    data = collection_object.find({}, {"_id": 1, "name": 1}).sort(sorted_column)
    for ele in data:
        print(ele)


def apply_sort_descending(sorted_column):
    collection_object = main()
    data = collection_object.find({}, {"_id": 1, "name": 1}).sort(sorted_column, -1)
    for ele in data:
        print(ele)


if __name__ == "__main__":
    column_name = "name"
    column_name1 = "age"
    column_name2 = "class"
    column_name3 = "gender"

    # Call Default Sort method :
    # apply_sort_default_ascending(column_name)
    # apply_sort_default_ascending(column_name1)
    # apply_sort_default_ascending(column_name2)
    # apply_sort_default_ascending(column_name3)

    # call descending method:
    # apply_sort_descending(column_name)
    # apply_sort_descending(column_name1)
    # apply_sort_descending(column_name2)
    # apply_sort_descending(column_name3)

