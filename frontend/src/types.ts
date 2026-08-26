export interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
  description: string;
}

export interface CartItem {
  id: number;
  name: string;
  price: number;
  quantity: number;
}

export interface Cart {
  items: CartItem[];
  total: number;
}

export interface PaginatedProducts {
  products: Product[];
  page: number;
  per_page: number;
  total: number;
  total_pages: number;
}
