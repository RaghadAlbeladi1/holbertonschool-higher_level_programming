from flask import Flask, render_template, request
import json
import csv

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
