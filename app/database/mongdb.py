

import pymongo

def test():
  client = pymongo.MongoClient("mongodb+srv://tas:<password>@cluster0.lo0kf.mongodb.net/?retryWrites=true&w=majority")

  db = client.sample_training

  my_collection = db["companies"]
  result = my_collection.count_documents({})

  res=result if result else "no documents found"
  return res

