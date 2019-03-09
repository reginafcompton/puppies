import pymongo
from pymongo import MongoClient
import ssl

from secrets import MONGODB_ADMIN_PASSWORD

connection_uri = "mongodb://reginafcompton:{}@puppiescluster-shard-00-00-jk350.mongodb.net:27017,puppiescluster-shard-00-01-jk350.mongodb.net:27017,puppiescluster-shard-00-02-jk350.mongodb.net:27017/test?ssl=true&replicaSet=PuppiesCluster-shard-0&authSource=admin&retryWrites=true".format(MONGODB_ADMIN_PASSWORD)

client = pymongo.MongoClient(connection_uri, ssl_cert_reqs=ssl.CERT_NONE)

db = client['puppiesdatabase']

db.inventory.insert_many([
   # MongoDB adds the _id field with an ObjectId if _id is not present
   { "item": "journal", "qty": 25, "status": "A",
       "size": { "h": 14, "w": 21, "uom": "cm" }, "tags": [ "blank", "red" ] },
   { "item": "notebook", "qty": 50, "status": "A",
       "size": { "h": 8.5, "w": 11, "uom": "in" }, "tags": [ "red", "blank" ] },
   { "item": "paper", "qty": 100, "status": "D",
       "size": { "h": 8.5, "w": 11, "uom": "in" }, "tags": [ "red", "blank", "plain" ] },
   { "item": "planner", "qty": 75, "status": "D",
       "size": { "h": 22.85, "w": 30, "uom": "cm" }, "tags": [ "blank", "red" ] },
   { "item": "postcard", "qty": 45, "status": "A",
       "size": { "h": 10, "w": 15.25, "uom": "cm" }, "tags": [ "blue" ] }
])

if __name__ == "__main__":
    main()