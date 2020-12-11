import pymongo

connection = pymongo.MongoClient('localhost',27017)

database = connection['mydb']
collection = database['employees_info']

data = {'Name':"Tanmay"}
collection.insert_one(data)
