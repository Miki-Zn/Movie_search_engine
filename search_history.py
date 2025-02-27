from db_connection import connect_mysql, connect_mongo
from typing import List, Dict, Any
import pymysql
from datetime import datetime


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
        return []

    db = os.getenv("MONGO_DATABASE")
    search_collection = os.getenv("MONGO_COLLECTION")

    search_data = {
        "query": search_query,
        "results": search_results,
        "timestamp": datetime.now()
    }

    try:
        search_collection.insert_one(search_data)
        print("Request saved to MongoDB.")
    except Exception as e:
        print(f"Error: did not save to MongoDB: {e}")
