from flask import Flask, request, send_from_directory, jsonify
import json
import random
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")

# Serve frontend files (index.html, style.css, app.js)
@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("../frontend", path)

# Serve products.json from backend folder
@app.route("/products.json")
def products():
    return send_from_directory(".", "products.json")

# Serve images from images/ folder
@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory("images", filename)

# Match endpoint to receive image and return similar products
@app.route("/match", methods=["POST"])
def match():
    uploaded_img = request.files.get("image")
    # (Optional) Save uploaded file temporarily if needed for real matching
    # For now, dummy matching: load products and return a few random results
    
    products_path = os.path.join(os.getcwd(), "products.json")
    with open(products_path) as f:
        products = json.load(f)

    if not products:
        return jsonify([])

    # Select up to 3 random products as similar matches (placeholder)
    matched_products = random.sample(products, min(3, len(products)))

    # Add fake similarity score and fix image URLs for frontend consumption
    for prod in matched_products:
        prod["similarity"] = random.randint(80, 99)
        if not prod["image"].startswith("/images/"):
            prod["image"] = "/images/" + prod["image"]

    return jsonify(matched_products)

if __name__ == "_main_":
    app.run(debug=True)