# app.py
# Autor: Gemini CLI Agent
# Descripción: Aplicación Flask de ejemplo para el servicio de pedidos.

from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Configuración de la base de datos (ejemplo, en un entorno real usaríamos variables de entorno)
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'orders_db')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    return conn

@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM orders;')
        orders = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(orders)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders', methods=['POST'])
def create_order():
    try:
        new_order = request.json
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO orders (item, quantity) VALUES (%s, %s); ',
                    (new_order['item'], new_order['quantity']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Order created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # En un entorno de producción, el puerto se gestionaría por ECS/Fargate
    app.run(host='0.0.0.0', port=5000)
