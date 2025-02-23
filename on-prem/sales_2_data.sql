CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    store_id INT NOT NULL,  -- Unique Store Identifier
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    quantity_sold INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) GENERATED ALWAYS AS (quantity_sold * unit_price) STORED,
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
