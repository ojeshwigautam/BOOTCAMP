Ques 1. Write a query to create a function that calculates the total revenue from the 'orders' and 'payment' tables for completed orders, and call the function to get the total revenue.


-- Create function to calculate total revenue from completed orders
CREATE FUNCTION CalculateTotalRevenue()
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE total_amount DECIMAL(10, 2);
    
    SELECT SUM(o.total_amount)
    INTO total_amount
    FROM orders o
    JOIN payment p ON o.order_id = p.order_id
    WHERE o.status = 'completed';
    
    RETURN total_amount;
END;

-- Call the function to get the total revenue
SELECT CalculateTotalRevenue() AS total_revenue;


Ques 3. Write a query to create a procedure with an IN parameter to retrieve details of a specific product based on the product ID passed as a parameter. Call the procedure for product ID 5.


-- Create procedure with an IN parameter to retrieve product details
DELIMITER //

CREATE PROCEDURE GetProductDetails(IN productId INT)
BEGIN
    SELECT *
    FROM products
    WHERE product_id = productId;
END //

DELIMITER ;

-- Call the procedure for product ID 5
CALL GetProductDetails(5);


Ques 4. Write a query to create a procedure with an OUT parameter to get the count of products in the 'products' table, store it in a variable, and select the variable to display the count.


-- Create procedure with an OUT parameter to get product count
DELIMITER 

CREATE PROCEDURE GetProductCount(OUT productCount INT)
BEGIN
    SELECT COUNT(*)
    INTO productCount
    FROM products;
END 

DELIMITER ;

-- Declare variable to hold product count
SET @count := 0;

-- Call the procedure to populate the variable
CALL GetProductCount(@count);

-- Select and display the product count
SELECT @count AS product_count;


Ques 5. Write a query to use the predefined SUM() cursor to calculate the total price of all products in the 'products' table where the product category is 'Electronics'.


-- Declare variables for cursor and sum
DECLARE total_price DECIMAL(10, 2) DEFAULT 0.00;
DECLARE product_price DECIMAL(10, 2);

-- Declare cursor for sum calculation
DECLARE product_cursor CURSOR FOR
    SELECT price
    FROM products
    WHERE category = 'Electronics';

-- Define handler for cursor
DECLARE CONTINUE HANDLER FOR NOT FOUND SET product_price = NULL;

-- Open and fetch values from cursor
OPEN product_cursor;

get_price: LOOP
    FETCH product_cursor INTO product_price;
    IF product_price IS NULL THEN
        LEAVE get_price;
    END IF;
    
    SET total_price := total_price + product_price;
END LOOP;

-- Close cursor
CLOSE product_cursor;

-- Display total price of electronics products
SELECT total_price AS total_electronics_price;


Ques 6. Write a query to declare and use a cursor to iterate through the 'products' table and print the product name for each product.


-- Declare variables for cursor and product name
DECLARE product_name VARCHAR(255);

-- Declare cursor to iterate through products table
DECLARE product_cursor CURSOR FOR
    SELECT name
    FROM products;

-- Define handler for cursor
DECLARE CONTINUE HANDLER FOR NOT FOUND SET product_name = NULL;

-- Open and fetch values from cursor
OPEN product_cursor;

print_names: LOOP
    FETCH product_cursor INTO product_name;
    IF product_name IS NULL THEN
        LEAVE print_names;
    END IF;
    
    -- Print product name
    SELECT CONCAT('Product Name: ', product_name) AS product_details;
END LOOP;

-- Close cursor
CLOSE product_cursor;
