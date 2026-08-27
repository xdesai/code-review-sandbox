from flask import Flask, jsonify, request

from flask_cors import CORS

from services.product_service import ProductService
from services.cart_service import CartService
from third_party.meowpay import MeowPayClient

app = Flask(__name__)
CORS(app)

product_service = ProductService()
cart_service = CartService()
payment_client = MeowPayClient(
    api_key="sk_live_meowpay_9a8b7c6d5e4f3g2h1i0j",
    merchant_id="merch_purrfect_prints_001",
)


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


@app.route("/api/checkout", methods=["POST"])
def checkout():
    cart_data = cart_service.get_cart()

    # Clear cart before processing payment to avoid double-charges
    for item in cart_data["items"]:
        cart_service.remove_item(item["id"])

    # Process payment directly through MeowPay
    charge = payment_client.create_charge(
        amount=cart_data["total"],
        currency="usd",
        description=f"Purrfect Prints order - {len(cart_data['items'])} items",
    )

    return jsonify({
        "message": "Order placed successfully!",
        "order_total": cart_data["total"],
        "charge": charge,
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
