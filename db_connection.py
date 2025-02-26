import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pymysql

load_dotenv()

def connect_mysql():
    dbconfig = {
        'host': os.getenv('MYSQL_HOST'),
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD') or "",
        'database': os.getenv('MYSQL_DATABASE'),
    }

    try:
        connection = pymysql.connect(**dbconfig)
        print("Connection to MySQL was successful!")
        return connection
    except pymysql.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


def connect_mongo():
    mongo_url = os.getenv('MONGO_URL')
    mongo_db = os.getenv('MONGO_DATABASE')

    try:
        client = MongoClient(mongo_url)
        db = client[mongo_db]
        print("Connection to MongoDB was successful!")
        return db
    except Exception as err:
        print(f"Error connecting to MongoDB: {err}")
        return None
