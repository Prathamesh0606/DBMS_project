import pymongo

connection = pymongo.MongoClient('localhost',27017)

database = connection['mydb']
collection = database['employees_info']
