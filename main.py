import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/mouryadb")

database = client["mouryadb"]

collection = database["products"]

d = {'company' : "iNeuron",
     'product': "Affordable AI",
     'courseOffered':"ML with deployment"
     }

rec = collection.insert_one(d)

allrec = collection.find()

for idx, rec in allrec.items():
    print(f"{idx}: {rec}")