CATALOG = [
    {
        "id": 1,
        "name": "Whiskers in the Sun",
        "price": 12.99,
        "image": "https://placecats.com/400/300",
        "description": "A majestic tabby basking in golden hour light.",
    },
    {
        "id": 2,
        "name": "Midnight Loaf",
        "price": 9.99,
        "image": "https://placecats.com/401/300",
        "description": "A perfectly formed loaf of pure darkness.",
    },
    {
        "id": 3,
        "name": "The Judging",
        "price": 14.99,
        "image": "https://placecats.com/400/301",
        "description": "This cat is not impressed with your life choices.",
    },
    {
        "id": 4,
        "name": "Box Inspector",
        "price": 11.99,
        "image": "https://placecats.com/402/300",
        "description": "Quality assurance at its finest.",
    },
    {
        "id": 5,
        "name": "Zoomies Blur",
        "price": 7.99,
        "image": "https://placecats.com/400/302",
        "description": "Artistic motion blur of a cat at full speed.",
    },
    {
        "id": 6,
        "name": "Window Philosopher",
        "price": 13.99,
        "image": "https://placecats.com/403/300",
        "description": "Deep in thought about birds, probably.",
    },
]


class ProductService:
    def get_products(self, page: int = 1, per_page: int = 4) -> dict:
        total = len(CATALOG)
        start = (page - 1) * per_page
        end = start + per_page
        items = CATALOG[start:end]

        return {
            "products": items,
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": (total + per_page - 1) // per_page,
        }

    def get_product_by_id(self, product_id: int) -> dict | None:
        return next((p for p in CATALOG if p["id"] == product_id), None)
