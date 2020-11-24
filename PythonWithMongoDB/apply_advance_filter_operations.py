from PythonWithMongoDB.create_collection import main


def apply_filter_with_specific_query(query):
    collection_object = main()
    data = collection_object.find(query)

    for ele in data:
        print(ele)


def apply_advance_filter_to_the_collection(query):
    collection_object = main()
    data = collection_object.find(query)
    for ele in data:
        print(ele)


def apply_filter_with_regular_expression(query):
    collection_object = main()
    data = collection_object.find(query)
    for ele in data:
        print(ele)


if __name__ == "__main__":
    # Normal Filter Condition :

    filter_query = {"age": 21}

    # Advance Filter Condition with conditional statement :

    advance_query_with_equal_condition = {"name": {"$eg": "Kanik Vijay"}}
    advance_query_with_less_than_condition = {"age": {"$lt": 25}}
    advance_query_with_less_than_or_equal_condition = {"age": {"$lte": 22}}
    advance_query_with_grater_than_condition = {"age": {"$gt": 20}}
    advance_query_with_grater_than_or_equal_condition = {"age": {"$gte": 20}}
    advance_query_with_not_equal_condition = {"age": {"$ne": 20}}
    advance_query_with_and_condition = {"$and": [{"class": "General"}, {"age": 21}]}
    advance_query_with_or_condition = {"$or": [{"class": "General"}, {"age": 21}]}
    advance_query_with_not_condition = {"age": {"$not": {"$gt": 24}}}
    advance_query_with_nor_condition = {"$nor": [{"name": "Kanik Vijay"}, {"age": 21}]}

    # Advance filter query using regex. :

    # 1. To find only the documents where the "class" field starts with the letter "G", use the regular expression
    advance_query_with_regex_condition_for_start = {"class": {"$regex": "^G"}}
    # 2. The following regex query searches for all the name containing string 'vijay' in it
    advance_query_with_regex_condition_for_checking_string = {"name": {"$regex": "/vijay/"}}

    # Call Function by passing query

    # apply_filter_with_specific_query(query=filter_query)
    # print("Now the Result in next line is came from advance query : \n")
    # apply_advance_filter_to_the_collection(advance_query_with_nor_condition)
    apply_filter_with_regular_expression(advance_query_with_regex_condition_for_checking_string)
