import pymongo
from pymongo import MongoClient
import ssl

client = MongoClient('mongodb://127.0.0.1:27017')

db = client['test_database']

# db.inventory.insert_many([
#    # MongoDB adds the _id field with an ObjectId if _id is not present
#    { "item": "journal", "qty": 25, "status": "A",
#        "size": { "h": 14, "w": 21, "uom": "cm" }, "tags": [ "blank", "red" ] },
#    { "item": "notebook", "qty": 50, "status": "A",
#        "size": { "h": 8.5, "w": 11, "uom": "in" }, "tags": [ "red", "blank" ] },
#    { "item": "paper", "qty": 100, "status": "D",
#        "size": { "h": 8.5, "w": 11, "uom": "in" }, "tags": [ "red", "blank", "plain" ] },
#    { "item": "planner", "qty": 75, "status": "D",
#        "size": { "h": 22.85, "w": 30, "uom": "cm" }, "tags": [ "blank", "red" ] },
#    { "item": "postcard", "qty": 45, "status": "A",
#        "size": { "h": 10, "w": 15.25, "uom": "cm" }, "tags": [ "blue" ] }
# ])

cursor = db.inventory.find({})