# app.py
from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data')
def get_data():
    db = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DB')
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM your_table")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
