import pymongo
from bson import ObjectId


# CONNECT TO DATABASE
connection = pymongo.MongoClient('localhost', 27017)


# create database
database = connection['Mongo']

# create collection
collection = database['employees_data']
#doc = {'photo':bin(0),'name':"Prathamesh Badgujar",'education':"BE",'address':"Pune",'salary':50000}
#collection.insert_one(doc)

print("Database connected")


def insert_single(data):
    """
    Insert new data in collection
    """
    document = collection.insert_one(data)
    return document.inserted_id


def update_or_create(document_id, data):
    """
    This will create new document and update if same document id already exists
    :param document_id:
    :param data:
    :return:
    """
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged


def get_single_data(document_id):
    """
    this will get the document data by document_id
    :param document_id:
    :return:
    """
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data


def get_all_data():
    """
    get list of multiple documents
    :return:
    """
    data = collection.find()
    return list(data)


def update_existing(doc_id, data):
    """
    update existing document only
    this wil not create new document if it doesn't exist
    :param doc_id:
    :param data:
    :return:
    """
    document = collection.update_one({'_id': ObjectId(doc_id)}, {"$set": data})
    return document.acknowledged


def remove_data(doc_id):
    """
    remove a single data item which matches document id
    :param doc_id:
    :return:
    """

    document = collection.delete_one({'_id': ObjectId(doc_id)})
    return document.acknowledged


# close database
connection.close()
