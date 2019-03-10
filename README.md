# puppies

An exercise in coding, learning, and finding puppies.

## Learning objectives and outcomes

#### Set-up MongoDB

MongoDB: a "document database" (a nonrelational database that stores data in JSON-like documents). 

Why use one? It can be more flexible. MongoDb does not require predefined schemas, so you need not do heavy data cleaning and prep beforehand, and a change to your data structures would not risk undermining your database. For example, every entity in the database might be stored as a document: this can be useful if your data has diversity within a single resource – so, a database of songs, but all those songs have different attributes, in which case relational models would be prohibitive and potentially inefficient.

How to get started? [Follow the official tutorial (for PyMongo).](https://docs.mongodb.com/manual/tutorial/getting-started/) The tutorial suggests using [Atlas](https://docs.mongodb.com/manual/tutorial/atlas-free-tier-setup/#create-free-tier-manual). I set up an account and learned some terms:

* Atlas: a cloud service for MongoDB
* An Atlas account has a structural heirarchary with: organizations, which have projects, which have clusters.
* Projects manage deployments or "clusters" – similar to an "instance," in that it has a size, region, type, etc.
* A cluster has some security restrictions: it can only be accessed by authenticated users, and it only allows client connections through IP addresses on a "whitelist."

Unfortunately, I could not connect to MongoDb. I received this error, whcih strikes me as unusual because my other services that require up-to-date SSL certs work fine. It is possible that my version of OpenSSL is not compatibile with the version of pymongo in the Atlas cloud.

```
pymongo.errors.ServerSelectionTimeoutError: SSL handshake failed: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:645),SSL handshake failed: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:645),SSL handshake failed: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:645)
```

Next steps? Install MongoDB locally. Mongo-Community-4.0 is not compatible with my OS, but I could easily install 3.4 view brew: `brew search mongodb` and `brew install mongodb@3.4`. The local install, in the end, was more instructive. It requires you to open a Mongo daemon process that listens for mongo connections on port 27017.

```
# start mongo service on mongodb://127.0.0.1:27017
mongod

# connect! this opens an interactive mongo shell
mongo
```

The mongo shell comes with several useful commands (particularly, for local testing and development).

```
# see all available databases
show dbs

# select a database
use test_database

# view all documents in selected database
db.inventory.find({})

# drop the selected database
db.dropDatabase()
```

Resources:
https://www.mongodb.com/what-is-mongodb
https://aws.amazon.com/nosql/document/  
https://medium.com/xplenty-blog/the-sql-vs-nosql-difference-mysql-vs-mongodb-32c9980e67b2

#### Data, data where do you live?

Creating a new Mongo database requires little effort. 

`pymongo` comes with a `MongoClient`. Instantiate a client, and specify the name of a database. The database need not exist: by saving data to it, MongoDB automatically creates the specified database.

`pymongo` expects json when inserting to the database. The provided `data.json` file is not proper JSON. Its main oddities include: single strings (rather than double strings), and a trailing semi-colon. It also presents a nested structure with 'canines' containing an array of objects (list of dicts). In short, the basic tools for converting this file to JSON do not work as expected, in that the result is always a string:

```
json.loads(<data>)
json.dump(<data>)
ast.literal_eval(<data>)
```

It is poor practice to modify the raw data ("data.json"), but I may need to do that, in order to make a little more progress! 