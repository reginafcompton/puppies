import json
import ast

import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')

db = client['puppies']

with open('data.json', 'r') as f:
    # read file as a string
    string = f.read()

    file_data = json.loads(string)
    result = ast.literal_eval(file_data.replace('\n', '\\n'))

db.inventory.insert(this_data)

client.close()