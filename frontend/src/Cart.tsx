import React, { useState } from "react";
import { Cart as CartType } from "./types";

interface Props {
  cart: CartType;
  onRemove: (productId: number) => void;
  onBack: () => void;
  onCheckout: () => Promise<void>;
}

function Cart({ cart, onRemove, onBack, onCheckout }: Props) {
  const [orderMessage, setOrderMessage] = useState<string>("");

  if (cart.items.length === 0) {
    return (
      <div className="cart">
        <h2>Your Cart</h2>
        <button className="back-btn" onClick={onBack}>&larr; Back to Shop</button>
        {orderMessage && <p className="order-success">{orderMessage}</p>}
        <p className="empty-cart">No items yet. Go find some cats!</p>
      </div>
    );
  }

  const handleCheckout = async () => {
    await onCheckout();
    setOrderMessage("Order placed successfully! Your cat pictures are on the way.");
  };

  return (
    <div className="cart">
      <button className="back-btn" onClick={onBack}>&larr; Back to Shop</button>
      <h2>Your Cart</h2>
      <ul className="cart-items">
        {cart.items.map((item) => (
          <li key={item.id} className="cart-item">
            <div>
              <strong>{item.name}</strong>
              <span className="quantity"> x{item.quantity}</span>
            </div>
            <div>
              <span>${(item.price * item.quantity).toFixed(2)}</span>
              <button className="remove-btn" onClick={() => onRemove(item.id)}>
                Remove
              </button>
            </div>
          </li>
        ))}
      </ul>
      <div className="cart-total">
        <strong>Total: ${cart.total.toFixed(2)}</strong>
      </div>
      <button className="checkout-btn" onClick={handleCheckout}>
        Checkout
      </button>
    </div>
  );
}

export default Cart;
