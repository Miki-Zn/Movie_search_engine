from typing import List, Dict, Any
import pymysql
from db_connection import connect_mysql

def search_movies_by_keyword(keyword: str) -> List[Dict[str, Any]]:
    connection = connect_mysql()
    if connection is None:
        return []

    query = """
    SELECT film_id, title, release_year
    FROM film
    WHERE LOWER(title) LIKE LOWER(%s) OR LOWER(description) LIKE LOWER(%s)
    LIMIT 10;
    """

    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        results = cursor.fetchall()

    connection.close()
    return results


def search_movies_by_genre_and_year(genre: str, year: int) -> List[Dict[str, Any]]:
    connection = connect_mysql()
    if connection is None:
        return []

    query = """
    SELECT f.film_id, f.title, f.release_year
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    WHERE TRIM(LOWER(c.name)) = TRIM(LOWER(%s)) AND f.release_year = %s
    LIMIT 10;
    """

    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(query, (genre, year))
        results = cursor.fetchall()

    connection.close()
    return results
