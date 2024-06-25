USE myntra;

-- SINGLE ROW SUBQUERIES

-- Example 1: Find the customer who placed the order with the highest amount
SELECT customer_name
FROM customers 
WHERE customer_id = (
    SELECT customer_id   
    FROM orders 
    ORDER BY amount DESC 
    LIMIT 1
);

-- Example 2: Find the product with the highest price
SELECT product_name
FROM products 
WHERE price = (
    SELECT MAX(price) 
    FROM products
);

-- MULTIPLE-ROW SUBQUERIES

-- Example 1: Find all customers who have placed an order
SELECT customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
);

-- Example 2: Find all customers who have placed an order for a product from a specific city
SELECT customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id FROM orders
    WHERE product_id IN (
        SELECT product_id FROM products WHERE location = 'CityName'
    )
);

-- CORRELATED SUBQUERIES

-- Example 1: Products with Price Higher than Location Average
SELECT product_name, price
FROM products p
WHERE price > (
    SELECT AVG(price)
    FROM products
    WHERE location = p.location
);

-- Example 2: Customers with Orders Exceeding Average Order Amount
SELECT customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
    GROUP BY o.customer_id
    HAVING AVG(o.amount) > (
        SELECT AVG(amount)
        FROM orders
    )
);

-- Using JOINs for scenarios

-- INNER JOIN with subquery: Retrieve products with orders where price is greater than 1000
SELECT p.product_name, o.order_id, o.amount
FROM products p
INNER JOIN (
    SELECT *
    FROM orders
) o ON p.product_id = o.product_id
WHERE p.price > 1000;

-- LEFT JOIN with aggregate functions: Retrieve all products and their total orders' amounts, even with no orders
SELECT p.product_name, COALESCE(SUM(o.amount), 0) AS total_orders_amount
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id
GROUP BY p.product_name;

-- Advanced queries using analytical functions

-- RANK: Rank products based on price
SELECT product_id, product_name, price, RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

-- DENSE_RANK: Dense rank products based on price
SELECT product_id, product_name, price, DENSE_RANK() OVER (ORDER BY price DESC) AS dense_price_rank
FROM products;

-- ROW_NUMBER: Assign unique row number to customers based on age
SELECT ROW_NUMBER() OVER (ORDER BY age DESC) AS row_num, customer_id, customer_name, age, address
FROM customers;

-- CUME_DIST: Calculate cumulative distribution of payment amounts
SELECT order_id, amount,
       CUME_DIST() OVER (ORDER BY amount) AS cumulative_distribution
FROM payments;

-- LAG: Find previous price of products within each location
SELECT product_name, price, location, LAG(price) OVER (PARTITION BY location ORDER BY price) AS lag_price
FROM products;

-- LEAD: Find next price of products within each location
SELECT product_name, price, location, LEAD(price) OVER (PARTITION BY location ORDER BY price) AS lead_price
FROM products;
