from flask import request,jsonify,Flask
import json
from flask_cors import CORS
import products_dao
import orders_dao
from sql_connector import get_sql_connection
import os
from dotenv import load_dotenv

load_dotenv() 
print("DB Host:", os.getenv("DB_HOST")) 

app = Flask(__name__)
CORS(app)
connection = get_sql_connection()

@app.route("/")
def home():
    return "Welcome to Grocery Store API!"

@app.route('/getProducts' , methods = ['GET'])

def get_products():
    try:
        connection = get_sql_connection()
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("""
            SELECT p.product_id, p.product_name, p.price_per_unit, p.uom_id,u.uom_name 
            FROM products p 
            JOIN uom u ON p.uom_id = u.uom_id
        """)
        
        products = cursor.fetchall()
        cursor.close()
        connection.close()

        return jsonify(products)  
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/storeOrder', methods=['POST'])
def store_order():
    try:
        connection = get_sql_connection()
        data = request.json
        print("Received order data:", data) 

        customer_name = data.get("customer_name")
        date = data.get("order_time") 

        items = data.get("items", [])
        if not customer_name or not items:
            return jsonify({"error": "Invalid order data"}), 400
            
        for item in data.get("items", []):
            print("Item received:", item)

        order_response = orders_dao.store_order_in_db(connection, customer_name, date, items)

        return jsonify(order_response)

    except Exception as e:
        print("Error processing order:", str(e))
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500
        
@app.route("/test_db")
def test_db():
    connection = get_sql_connection()
    
    if connection is None:
        return jsonify({"error": "Failed to connect to Railway database!"})
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1") 
        cursor.close()
        connection.close()
        return jsonify({"message": "Database connection successful!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__=="__main__":
    print("Starting flask server at port 5000")
    app.run(port=5000)
