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
@app.route('/getProducts' , methods = ['GET'])

def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response

@app.route('/storeOrder', methods=['POST'])
def store_order():
    try:
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

if __name__=="__main__":
    print("Starting flask server at port 5000")
    app.run(port=5000)