from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_from_json():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception:
        return []

def load_from_csv():
    products = []
    try:
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        return []
    return products

def load_from_sql():
    products = []
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except Exception:
        return []
    return products

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    products = []
    error = None

    if source == "json":
        products = load_from_json()
    elif source == "csv":
        products = load_from_csv()
    elif source == "sql":
        products = load_from_sql()
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error, products=[])

    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid id format"
            products = []

    return render_template("product_display.html", products=products, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
