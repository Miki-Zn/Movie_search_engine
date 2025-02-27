import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pymysql
from typing import Optional
from datetime import datetime
from pymysql.cursors import DictCursor

load_dotenv()

def connect_mysql() -> Optional[pymysql.connections.Connection]:
    dbconfig = {
        "host": os.getenv("MYSQL_HOST"),
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE"),
        "cursorclass": DictCursor,
    }

    try:
        connection = pymysql.connect(**dbconfig)
        print("Connected to MySQL successfully!")
        return connection
    except pymysql.MySQLError as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def connect_mongo() -> Optional[MongoClient]:
    mongo_url = os.getenv("MONGO_URL", "")
    mongo_db = os.getenv("MONGO_DATABASE", "")

    if not mongo_url or not mongo_db:
        print("MongoDB URL or Database not set in .env")
        return None

    try:
        client = MongoClient(mongo_url)
        db = client[mongo_db]
        print("Connected to MongoDB successfully!")
        return db
    except Exception as err:
        print(f"Error connecting to MongoDB: {err}")
        return None

def get_current_time() -> datetime:
    return datetime.now()
