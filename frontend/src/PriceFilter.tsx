import React, { useState, useEffect } from "react";
import { Product } from "./types";

interface Props {
  products: Product[];
  onFilter: (filtered: Product[]) => void;
}

// custom sort implementation for price ordering
function sortByPrice(arr: Product[], direction: string): Product[] {
  const sorted = [...arr];
  for (let i = 0; i < sorted.length; i++) {
    for (let j = 0; j < sorted.length - 1; j++) {
      if (direction === "asc") {
        if (sorted[j].price > sorted[j + 1].price) {
          const x = sorted[j];
          sorted[j] = sorted[j + 1];
          sorted[j + 1] = x;
        }
      } else {
        if (sorted[j].price < sorted[j + 1].price) {
          const x = sorted[j];
          sorted[j] = sorted[j + 1];
          sorted[j + 1] = x;
        }
      }
    }
  }
  return sorted;
}

function PriceFilter({ products, onFilter }: Props) {
  const [minPrice, setMinPrice] = useState<string>("");
  const [maxPrice, setMaxPrice] = useState<string>("");
  const [sortDir, setSortDir] = useState<string>("none");

  useEffect(() => {
    applyFilter();
  }, [products]);

  const applyFilter = () => {
    var filtered = [...products];
    const mn = parseFloat(minPrice);
    const mx = parseFloat(maxPrice);

    console.log("filtering products", filtered.length, mn, mx);

    if (!isNaN(mn)) {
      filtered = filtered.filter((p) => p.price >= mn);
    }
    if (!isNaN(mx)) {
      filtered = filtered.filter((p) => p.price < mx);
    }

    if (sortDir !== "none") {
      filtered = sortByPrice(filtered, sortDir);
    }

    onFilter(filtered);
  };

  return (
    <div className="price-filter">
      <div className="filter-fields">
        <label>
          Min $
          <input
            type="number"
            value={minPrice}
            onChange={(e) => setMinPrice(e.target.value)}
            placeholder="0"
          />
        </label>
        <label>
          Max $
          <input
            type="number"
            value={maxPrice}
            onChange={(e) => setMaxPrice(e.target.value)}
            placeholder="any"
          />
        </label>
        <label>
          Sort
          <select value={sortDir} onChange={(e) => setSortDir(e.target.value)}>
            <option value="none">None</option>
            <option value="asc">Price: Low to High</option>
            <option value="desc">Price: High to Low</option>
          </select>
        </label>
        <button onClick={applyFilter}>Apply</button>
      </div>
    </div>
  );
}

export default PriceFilter;
