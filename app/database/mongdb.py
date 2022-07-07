from pymongo import MongoClient
import time

import pymongo
start = time.time()
client = pymongo.MongoClient("mongodb+srv://tas:<password>@cluster0.lo0kf.mongodb.net/?retryWrites=true&w=majority")
# use a database named "myDatabase"
db = client.sample_training
# FIND DOCUMENTS
#
# Now that we have data in Atlas, we can read it. To retrieve all of
# the data in a collection, we call find() with an empty filter. 
my_collection = db["companies"]
result = my_collection.count_documents({})

if result:    
    print(result)
    
else:
  print("No documents found.")

print("\n")
end = time.time()

print("The time used to execute this is given below")
print(end - start)