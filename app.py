from pymongo import MongoClient

client = MongoClient('localhost', 37017)

# database name
db=client['meat']

# create collection
collection = db['sausage']

# data example
item_1 ={"brand": "Berlinki", "weight_grams":300, "cost":3.25}
item_2 = {"brand":"Medziotoju", "weight_grams":150, "cost":2.55}
item_3 = {"brand":"Grill", "weight_grams":200, "cost":2.05}
item_4 = {"brand":"Biovela", "weight_grams":500, "cost":4.99}

#insert a documents to a collection

collection.insert_many([item_1, item_2, item_3, item_4])
collection.find_one({})

result = collection.find({})
print([x for x in result])

#find items -> returns items object
# result = collections.find({"cost":1.50, "alco":5})
# print([x for x in result]) #  <- list comprehension

#find one item
# result = collections.find_one({"cost":1.85})
# print(result)


#delete first item from collection by first ID
# collections.delete_one({"cost":1.5})

#list all items
# result = collections.find({})
# print([x for x in result])

#delete all items
# collections.delete_many({})

#Update/Replace
# collections.update_one({"brand": "Svyturys"}, {"$set": {"alco": 5}})
# result = collections.find({})
# print([x for x in result])

#count documents

# count = collections.count_documents({})
# print(count)

