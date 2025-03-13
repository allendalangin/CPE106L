from pymongo import MongoClient
import pprint
import re

client = MongoClient("mongodb+srv://shldrlv80:MyMongoDBpass@cluster0.dhh4k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.chinook

db = client["chinook"]

customers_collection = db["customers"]

#doc1 = customers_collection.find_one()
#print(doc1)

#for all_doc in customers_collection.find():
#     print(all_doc)

#for rec in customers_collection.find({},{"_id":0, "LastName": 1, "FirstName": 1}):
#    print(rec)

rgx = re.compile('^G.*?$', re.IGNORECASE)
cursor = customers_collection.find({"LastName":rgx})
num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))
client.close