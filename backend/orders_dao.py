import sqlite3
from datetime import datetime

def store_order_in_db(connection, customer_name, date, items):
    cursor = connection.cursor()

    formatted_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")
    total_price = sum(item["quantity"] * item["price_per_unit"] for item in items)
    query_order = ("INSERT INTO orders (customer_name, date, total) VALUES (%s, %s,%s)")
    cursor.execute(query_order, (customer_name, formatted_date,total_price))
    order_id = cursor.lastrowid

    query_order_details = ("INSERT INTO order_details (order_id, product_id, quantity, total) "
                           "VALUES (%s, %s, %s, %s)")

    for item in items:
        cursor.execute(query_order_details, (order_id, item['product_id'], item['quantity'], item['quantity'] * item['price_per_unit']))

    connection.commit()

    response = {
        "order_id": order_id,
        "customer_name": customer_name,
        "date": date,
        "total": total_price,
        "items": [{"product_id": item["product_id"], "quantity": item["quantity"], "total": item["quantity"] * item["price_per_unit"]} for item in items]
    }

    return response