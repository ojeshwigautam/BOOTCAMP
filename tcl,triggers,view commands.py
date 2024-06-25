
### TCL Commands

1. **Saving the command permanently after running successfully:**
   In MySQL, commands are automatically committed unless you're in a transaction. To save changes permanently after a successful execution, you typically just execute the commands directly without starting a transaction.

2. **Going to the previous command:**
   In MySQL command-line interface or tools like MySQL Workbench, you can use the arrow keys (up and down) to navigate through the command history to access previous commands.

3. **Going to a checkpoint where you want to go after saving the checkpoint:**
   MySQL supports savepoints within transactions. You can create a savepoint and later roll back to that specific point if needed, using `SAVEPOINT` and `ROLLBACK TO` commands.


sql
-- Start a transaction
START TRANSACTION;

-- Inserting values with a savepoint
INSERT INTO products (pid, pname, price, stock, location) VALUES (8, 'iPhone 12', 79900, 10, 'Delhi');
SAVEPOINT A;



-- Roll back to savepoint A if needed
ROLLBACK TO A;

-- Commit the transaction
COMMIT;
```

### Triggers

1. **Trigger to update status in the payment table after an order is completed:**
   
   DELIMITER //
   CREATE TRIGGER update_payment_status
   AFTER UPDATE ON orders
   FOR EACH ROW
   BEGIN
       IF NEW.status = 'completed' THEN
           UPDATE payment
           SET status = 'completed'
           WHERE oid = NEW.oid;
       END IF;
   END //
   DELIMITER ;
   ```

2. **Trigger to check stock availability before inserting an order:**
   
   DELIMITER //
   CREATE TRIGGER check_stock_before_order
   BEFORE INSERT ON orders
   FOR EACH ROW
   BEGIN
       DECLARE available_stock INT;
       SELECT stock INTO available_stock FROM products WHERE pid = NEW.pid;
       IF available_stock < NEW.amt THEN
           SIGNAL SQLSTATE '45000'
           SET MESSAGE_TEXT = 'Insufficient stock for this product';
       END IF;
   END //
   DELIMITER ;
   ```

3. **Trigger to update stock after an order is placed:**
   
   DELIMITER //
   CREATE TRIGGER update_stock_after_order
   AFTER INSERT ON orders
   FOR EACH ROW
   BEGIN
       UPDATE products
       SET stock = stock - NEW.amt
       WHERE pid = NEW.pid;
   END //
   DELIMITER ;
   ```

### Views

1. **Create a view that displays the customers with their corresponding orders:**
  
   CREATE VIEW CustomerOrders AS
   SELECT c.cid, c.cname, o.oid, o.amt, p.pname
   FROM customer c
   JOIN orders o ON c.cid = o.cid
   JOIN products p ON o.pid = p.pid;
   ```

2. **Create or Replace View to show payment details with order and customer information:**
   
   CREATE OR REPLACE VIEW payment_order_customer_details AS
   SELECT p.pay_id, p.oid, o.cid, c.cname, c.age, c.addr, p.amount, p.mode, p.status
   FROM payment p
   JOIN orders o ON p.oid = o.oid
   JOIN customer c ON o.cid = c.cid;
   ```

3. **Drop View if it exists:**
   ```sql
   DROP VIEW IF EXISTS payment_order_customer_details;
   ```

