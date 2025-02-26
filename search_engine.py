from db_connection import connect_mysql


def search_movies_by_keyword(keyword):
    connection = connect_mysql()
    if not connection:
        return []

    sql = """
    SELECT film_id, title, description, release_year
    FROM film
    WHERE title LIKE %s OR description LIKE %s
    LIMIT 10;
    """

    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()
    connection.close()

    return results


def search_movies_by_genre_and_year(genre, year):
    connection = connect_mysql()
    if not connection:
        return []

    sql = """
    SELECT f.film_id, f.title, f.release_year, c.name AS genre
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = %s AND f.release_year = %s
    LIMIT 10;
    """

    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (genre, year))
    results = cursor.fetchall()
    connection.close()

    return results
