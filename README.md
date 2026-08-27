# Purrfect Prints

A simple cat photo storefront with a React (TypeScript) frontend and Flask API backend.

## Project Structure

```
├── backend/
│   ├── app.py                 # Flask routes
│   ├── requirements.txt
│   └── services/
│       ├── product_service.py # Product catalog + pagination
│       └── cart_service.py    # Cart state management
└── frontend/
    ├── package.json
    ├── tsconfig.json
    └── src/
        ├── App.tsx
        ├── ProductList.tsx
        ├── Cart.tsx
        ├── types.ts
        └── App.css
```

## Running the Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API runs on http://localhost:5000.

## Running the Frontend

```bash
cd frontend
npm install
npm start
```

The app runs on http://localhost:3000 and proxies API requests to the backend.

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/products?page=1&per_page=4 | List products (paginated) |
| GET | /api/products/:id | Get a single product |
| GET | /api/cart | Get current cart |
| POST | /api/cart/:product_id | Add item to cart |
| DELETE | /api/cart/:product_id | Remove item from cart |
