import React from "react";
import { Product } from "./types";

interface Props {
  products: Product[];
  onAdd: (productId: number) => void;
}

function ProductList({ products, onAdd }: Props) {
  return (
    <div className="product-grid">
      {products.map((product) => (
        <div key={product.id} className="product-card">
          <img src={product.image} alt={product.name} />
          <h3>{product.name}</h3>
          <p className="description">{product.description}</p>
          <div className="product-footer">
            <span className="price">${product.price.toFixed(2)}</span>
            <button onClick={() => onAdd(product.id)}>Add to Cart</button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default ProductList;
