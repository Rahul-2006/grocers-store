import mysql.connector
import os

def get_sql_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 18032)),
            buffered = True
        )
        print("✅ Database connection established successfully!") 
        return connection
    except mysql.connector.Error as e:
        print(f"❌ Database connection failed: {e}") 
        return None
