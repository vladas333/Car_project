from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database
from typing import Dict, Any, List

def filter_documents(collection: Collection, filter_criteria: List[Dict[str, Any]]) -> Cursor:
    pipeline = [
        {
            '$match': {
                '$and': filter_criteria
            }
        }
    ]
    return collection.aggregate(pipeline)

# Establish a connection to the MongoDB server
client: MongoClient = MongoClient('mongodb://localhost:27017')
db: Database = client['All_cars']  # Type: Database
collection: Collection = db['Cars']  # Type: Collection


# Define the filter criteria
criteria: List[Dict[str, Any]] = [
    {'year': 1955},
    {'$or': [{'make': 'Ford'}, {'model': 'Corvette'}]},
    {'$not': {'year': {'$gt': 1980}}}
]  # Type: List[Dict[str, Any]]

# Call the filter_documents function
result: Cursor = filter_documents(collection, criteria)  # Type: Cursor

# Iterate over the cursor and print the filtered documents
for doc in result:
    print(doc)