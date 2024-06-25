

   First Normal Form (1NF)- 1NF requires that the table has a primary key and that each column contains only atomic (indivisible) values. Additionally, each column should contain values of a single type.
 
   
   OrderID	       CustomerName	     OrderDate	      ProductName	      Quantity
     1	             John Doe	    2023-06-01   	      Apple	             5
     2	            Jane Smith	    2023-06-02	      Orange, Banana	    3, 2

This table is not in 1NF because the ProductName and Quantity columns contain multiple values.*/

-- 1NF Conversion: 

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    ProductName VARCHAR(100),
    Quantity INT
);

INSERT INTO Orders (OrderID, CustomerName, OrderDate, ProductName, Quantity)
VALUES
(1, 'John Doe', '2023-06-01', 'Apple', 5),
(2, 'Jane Smith', '2023-06-02', 'Orange', 3),
(3, 'Jane Smith', '2023-06-02', 'Banana', 2);

select * from Orders;
drop table Orders;

/* Second Normal Form (2NF) -> 2NF requires that the table is in 1NF and that all non-key columns are fully dependent on the primary key. 
                               This means removing partial dependencies on a composite key.


OrderID	        CustomerName	        OrderDate	        ProductName	        Quantity	   CustomerAddress
  1	              John Doe	            2023-06-01	            Apple	           5	         123 Main St
  2	             Jane Smith	            2023-06-02	            Orange	           3             456 Oak Ave
  3	             Jane Smith	            2023-06-02	            Banana	           2	         456 Oak Ave

The CustomerAddress is not fully dependent on the primary key OrderID but rather on CustomerName. */

-- 2NF Conversion:

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    CustomerAddress VARCHAR(255)
);

INSERT INTO Customers (CustomerID, CustomerName, CustomerAddress)
VALUES
(11, 'John Doe', '123 Main St'),
(22, 'Jane Smith', '456 Oak Ave');

CREATE TABLE Orders(
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductName VARCHAR(100),
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

INSERT INTO Orders(OrderID, CustomerID, OrderDate)
VALUES
(1, 11, '2023-06-01'),
(2, 22, '2023-06-02');

INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductName, Quantity)
VALUES
(101, 1, 'Apple', 5),
(102, 2, 'Orange', 3),
(103, 2, 'Banana', 2);

 select*  from Customers;
 select * from Orders;
 select * from OrderDetails;

 drop table Customers;
 drop table OrderDetails;


/* Third Normal Form (3NF) -> 3NF requires that the table is in 2NF and that all non-key columns are not only fully dependent
                              on the primary key but also that there are no transitive dependencies.

OrderID	           CustomerID	        OrderDate	        ProductName	        Quantity	    SupplierName	    SupplierAddress
  1	                   1	            2023-06-01	          Apple	               5	         FreshFarms           789 Pine Rd
  2	                   2	            2023-06-02	          Orange	           3	         CitrusWorld	      890 Elm St
  3	                   2	            2023-06-02	          Banana	           2	         TropicFruits	      901 Maple St

The SupplierAddress is dependent on SupplierName, not directly on the primary key OrderID. */

-- 3NF Conversion:

CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(100),
    SupplierAddress VARCHAR(255)
);

INSERT INTO Suppliers (SupplierID, SupplierName, SupplierAddress)
VALUES
(1, 'FreshFarms', '789 Pine Rd'),
(2, 'CitrusWorld', '890 Elm St'),
(3, 'TropicFruits', '901 Maple St');

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    SupplierID INT,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

INSERT INTO Products (ProductID, ProductName, SupplierID)
VALUES
(1, 'Apple', 1),
(2, 'Orange', 2),
(3, 'Banana', 3);

CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity)
VALUES
(1, 1, 1, 5),
(2, 2, 2, 3),
(3, 2, 3, 2);

select * from suppliers;
select *  from products;
select * from OrderDetails;


