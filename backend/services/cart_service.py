from services.product_service import ProductService


class CartService:
    def __init__(self):
        self._items: list[dict] = []
        self._product_service = ProductService()

    def get_cart(self) -> dict:
        total = sum(item["price"] * item["quantity"] for item in self._items)
        return {"items": self._items, "total": round(total, 2)}

    def add_item(self, product_id: int) -> dict | None:
        product = self._product_service.get_product_by_id(product_id)
        if product is None:
            return None

        existing = next(
            (item for item in self._items if item["id"] == product_id), None
        )
        if existing:
            existing["quantity"] += 1
        else:
            self._items.append(
                {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": 1,
                }
            )

        return product

    def remove_item(self, product_id: int) -> None:
        self._items = [item for item in self._items if item["id"] != product_id]
