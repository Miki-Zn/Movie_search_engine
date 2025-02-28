from db_connection import connect_mysql, connect_mongo
from typing import List, Dict, Any
import pymysql
from datetime import datetime
import os

def save_search_to_mongo(search_query: str, search_results: List[Dict[str, Any]]) -> None:
    db_client = connect_mongo()
    if db_client is None:
        print("Error: MongoDB connection failed.")
        return

    mongo_db_name = os.getenv("MONGO_DATABASE")
    mongo_collection_name = os.getenv("MONGO_COLLECTION")

    if not mongo_db_name or not mongo_collection_name:
        print("Error: MongoDB database or collection not set.")
        return

    db = db_client[mongo_db_name]
    collection = db[mongo_collection_name]

    search_data = {
        "query": search_query,
        "results": search_results,
        "timestamp": datetime.now()
    }

    try:
        collection.insert_one(search_data)
        print("Search query saved to MongoDB.")
    except Exception as e:
        print(f"Error saving to MongoDB: {e}")

def search_movies_by_keyword(keyword: str) -> List[Dict[str, Any]]:
    connection = connect_mysql()
    if connection is None:
        return []

    sql = """
    SELECT film_id, title, description, release_year
    FROM film
    WHERE title LIKE %s OR description LIKE %s
    LIMIT 10;
    """

    try:
        with connection.cursor(cursorclass=pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, (f"%{keyword}%", f"%{keyword}%"))
            results = cursor.fetchall()
    finally:
        connection.close()

    if results:
        save_search_to_mongo(keyword, results)

    return results


def get_popular_searches() -> List[Dict[str, Any]]:
    db_client = connect_mongo()
    if db_client is None:
        print("Error: MongoDB connection failed.")
        return []

    mongo_db_name = os.getenv("MONGO_DATABASE")
    mongo_collection_name = os.getenv("MONGO_COLLECTION")

    if not mongo_db_name or not mongo_collection_name:
        print("Error: MongoDB database or collection not set.")
        return []

    db = db_client[mongo_db_name]
    collection = db[mongo_collection_name]

    try:
        popular_searches = collection.aggregate([
            {"$group": {"_id": "$query", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ])

        return list(popular_searches)
    except Exception as e:
        print(f"Error retrieving popular searches: {e}")
        return []
