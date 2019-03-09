# puppies

An exercise in coding, learning, and finding puppies.

## Learning objectives and outcomes

#### Data, data where do you live?

MongoDB: a "document database" (a nonrelational database that stores data in JSON-like documents). 

Why use one? It can be more flexible. MongoDb does not require predefined schemas, so you need not do heavy data cleaning and prep beforehand, and a change to your data structures would not risk undermining your database. For example, every entity in the database might be stored as a document: this can be useful if your data has diversity within a single resource – so, a database of songs, but all those songs have different attributes, in which case relational models would be prohibitive and potentially inefficient.


How to get started? [Follow the official tutorial (for PyMongo).](https://docs.mongodb.com/manual/tutorial/getting-started/) The tutorial suggests using [Atlas](https://docs.mongodb.com/manual/tutorial/atlas-free-tier-setup/#create-free-tier-manual). I set up an account and learned some terms:

* Atlas: a cloud service for MongoDB
* An Atlas account has a structural heirarchary with: organizations, which have projects, which have clusters.
* Projects manage deployments or "clusters" – similar to an "instance," in that it has a size, region, type, etc.
* A cluster has some security restrictions: it can only be accessed by authenticated users, and it only allows client connections through IP addresses on a "whitelist."

Unfortunately, I could not connect to MongoDb. I received this error:

```
pymongo.errors.ServerSelectionTimeoutError: SSL handshake failed: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:645),SSL handshake failed: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:645),SSL handshake failed: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:645)
```

Resources:
https://www.mongodb.com/what-is-mongodb
https://aws.amazon.com/nosql/document/  
https://medium.com/xplenty-blog/the-sql-vs-nosql-difference-mysql-vs-mongodb-32c9980e67b2
