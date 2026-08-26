from flask import Flask, jsonify, request

from flask_cors import CORS

from services.product_service import ProductService
from services.cart_service import CartService

app = Flask(__name__)
CORS(app)

product_service = ProductService()
cart_service = CartService()


@app.route("/api/products", methods=["GET"])
def get_products():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 4, type=int)
    result = product_service.get_products(page=page, per_page=per_page)
    return jsonify(result)


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = product_service.get_product_by_id(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)


@app.route("/api/cart", methods=["GET"])
def get_cart():
    return jsonify(cart_service.get_cart())


@app.route("/api/cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    product = cart_service.add_item(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": f"Added {product['name']} to cart"}), 200


@app.route("/api/cart/<int:product_id>", methods=["DELETE"])
def remove_from_cart(product_id):
    cart_service.remove_item(product_id)
    return jsonify({"message": "Item removed"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
