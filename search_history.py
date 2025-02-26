from db_connection import connect_mongo
from datetime import datetime

def save_search_query(query_text, search_type):
    db = connect_mongo()
    if not db:
        return

    collection = db["search_queries"]
    search_entry = {
        "query": query_text,
        "search_type": search_type,
        "timestamp": datetime()
    }
    collection.insert_one(search_entry)
    print(f" Query '{query_text}' has been saved to MongoDB.")

def get_popular_searches():
    db = connect_mongo()
    if not db:
        return []

    collection = db["search_queries"]
    popular_searches = collection.aggregate([
        {"$group": {"_id": "$query", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    return list(popular_searches)

