. Поиск фильмов по ключевому слову (в названии или описании)
SELECT film_id, title, description, release_year
FROM film
WHERE title LIKE CONCAT('%', %(keyword)s, '%')
   OR description LIKE CONCAT('%', %(keyword)s, '%')
LIMIT 10;

Поиск фильмов по жанру и году
SELECT f.film_id, f.title, f.release_year, c.name AS genre
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = %(genre)s
AND f.release_year = %(year)s
LIMIT 10;

####
Получение списка популярных поисковых запросов из MongoDB
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_popular_searches():
    """Получает 10 самых популярных поисковых запросов из MongoDB."""
    mongo_url = os.getenv('MONGO_URL')
    mongo_db = os.getenv('MONGO_DATABASE')
    collection_name = os.getenv("MONGO_COLLECTION")

    client = MongoClient(mongo_url)
    db = client[mongo_db]
    collection = db[collection_name]

    popular_searches = collection.aggregate([
        {"$group": {"_id": "$query", "count": {"$sum": 1}}},  # Группируем запросы и считаем их количество
        {"$sort": {"count": -1}},  # Сортируем по убыванию частоты
        {"$limit": 10}  # Берем топ-10 запросов
    ])

    return list(popular_searches)

# Проверка работы:
if __name__ == "__main__":
    for search in get_popular_searches():
        print(search)




Функция для сохранения запроса в MongoDB
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

# Загружаем переменные окружения
load_dotenv()

def save_search_query(query_text, search_type):
    """Сохраняет поисковый запрос в MongoDB."""
    mongo_url = os.getenv('MONGO_URL')
    mongo_db = os.getenv('MONGO_DATABASE')
    collection_name = os.getenv("MONGO_COLLECTION")

    client = MongoClient(mongo_url)
    db = client[mongo_db]
    collection = db[collection_name]

    search_entry = {
        "query": query_text,
        "search_type": search_type,
        "timestamp": datetime.utcnow()
    }

    collection.insert_one(search_entry)
    print(f"✅ Запрос '{query_text}' сохранен в MongoDB.")

# Пример использования:
if __name__ == "__main__":
    save_search_query("Inception", "keyword")  # Сохранение поиска по ключевому слову


Функция для поиска фильмов и сохранения запроса

(а) Поиск фильмов по ключевому слову + сохранение запроса
def search_movies_by_keyword(cursor, keyword):
    """Ищет фильмы по ключевому слову и сохраняет запрос в MongoDB."""
    sql = """
    SELECT film_id, title, description, release_year
    FROM film
    WHERE title LIKE CONCAT('%', %s, '%')
       OR description LIKE CONCAT('%', %s, '%')
    LIMIT 10;
    """

    cursor.execute(sql, (keyword, keyword))
    results = cursor.fetchall()

    # Сохранение запроса в MongoDB
    save_search_query(keyword, "keyword")

    return results
######
 Поиск фильмов по жанру и году + сохранение запроса
 def search_movies_by_genre_and_year(cursor, genre, year):
    """Ищет фильмы по жанру и году и сохраняет запрос в MongoDB."""
    sql = """
    SELECT f.film_id, f.title, f.release_year, c.name AS genre
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = %s
    AND f.release_year = %s
    LIMIT 10;
    """

    cursor.execute(sql, (genre, year))
    results = cursor.fetchall()

    # Сохранение запроса в MongoDB
    save_search_query(f"{genre} - {year}", "genre_year")

    return results

###
Получение списка популярных запросов из MongoDB
def get_popular_searches():
    """Получает 10 самых популярных поисковых запросов из MongoDB."""
    mongo_url = os.getenv('MONGO_URL')
    mongo_db = os.getenv('MONGO_DATABASE')
    collection_name = os.getenv("MONGO_COLLECTION")

    client = MongoClient(mongo_url)
    db = client[mongo_db]
    collection = db[collection_name]

    popular_searches = collection.aggregate([
        {"$group": {"_id": "$query", "count": {"$sum": 1}}},  # Группируем запросы и считаем их количество
        {"$sort": {"count": -1}},  # Сортируем по убыванию
        {"$limit": 10}  # Ограничиваем результат 10 запросами
    ])

    return list(popular_searches)

# Проверка работы:
if __name__ == "__main__":
    for search in get_popular_searches():
        print(search)


###
Запрос для MongoDB
def get_popular_searches_mongo():
    """Получает 10 самых популярных поисковых запросов из MongoDB."""
    mongo_url = os.getenv('MONGO_URL')
    mongo_db = os.getenv('MONGO_DATABASE')
    collection_name = os.getenv("MONGO_COLLECTION")

    client = MongoClient(mongo_url)
    db = client[mongo_db]
    collection = db[collection_name]

    popular_searches = collection.aggregate([
        {"$group": {"_id": "$query", "count": {"$sum": 1}}},  # Группируем запросы и считаем их количество
        {"$sort": {"count": -1}},  # Сортируем по убыванию
        {"$limit": 10}  # Ограничиваем результат 10 запросами
    ])

    return list(popular_searches)

# Пример вызова функции:
if __name__ == "__main__":
    for search in get_popular_searches_mongo():
        print(search)
