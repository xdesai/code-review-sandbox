import React, { useState, useEffect } from "react";
import ProductList from "./ProductList";
import Cart from "./Cart";
import { Product, Cart as CartType, PaginatedProducts } from "./types";
import "./App.css";

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [cart, setCart] = useState<CartType>({ items: [], total: 0 });
  const [showCart, setShowCart] = useState(false);

  const fetchProducts = (p: number) => {
    fetch(`/api/products?page=${p}`)
      .then((res) => res.json())
      .then((data: PaginatedProducts) => {
        setProducts(data.products);
        setPage(data.page);
        setTotalPages(data.total_pages);
      });
  };

  useEffect(() => {
    fetchProducts(1);
  }, []);

  const fetchCart = () => {
    fetch("/api/cart")
      .then((res) => res.json())
      .then(setCart);
  };

  useEffect(() => {
    fetchCart();
  }, []);

  const addToCart = (productId: number) => {
    fetch(`/api/cart/${productId}`, { method: "POST" })
      .then((res) => res.json())
      .then(() => fetchCart());
  };

  const removeFromCart = (productId: number) => {
    fetch(`/api/cart/${productId}`, { method: "DELETE" })
      .then((res) => res.json())
      .then(() => fetchCart());
  };

  return (
    <div className="app">
      <header className="header">
        <h1>Purrfect Prints</h1>
        <p className="subtitle">Fine art photography, by cats, of cats, for cats.</p>
        <button className="cart-toggle" onClick={() => setShowCart(!showCart)}>
          Cart ({cart.items.reduce((sum, item) => sum + item.quantity, 0)})
        </button>
      </header>

      {showCart ? (
        <Cart cart={cart} onRemove={removeFromCart} onBack={() => setShowCart(false)} />
      ) : (
        <>
          <ProductList products={products} onAdd={addToCart} />
          <div className="pagination">
            <button
              disabled={page <= 1}
              onClick={() => fetchProducts(page - 1)}
            >
              Previous
            </button>
            <span>Page {page} of {totalPages}</span>
            <button
              disabled={page >= totalPages}
              onClick={() => fetchProducts(page + 1)}
            >
              Next
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
