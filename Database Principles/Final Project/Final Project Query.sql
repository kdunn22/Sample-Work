IF  DB_ID('MyRetailStore') IS NOT NULL
	DROP DATABASE MyRetailStore;
GO

-- Create the MyRetailStore database
CREATE DATABASE MyRetailStore
GO

-- use the database just created 
USE MyRetailStore
GO

--creating 6 tables for MyRetailStore

Create TABLE Offices
(
	OfficeID int NOT NULL PRIMARY KEY IDENTITY,
	Address varchar(50) NOT NULL,
	City varchar(50) NOT NULL,
	State varchar(50) NOT NULL,
	ZipCode varchar(50) NOT NULL,
	Phone varchar(50) NOT NULL
);

CREATE TABLE Products
(
	ProductID int NOT NULL PRIMARY KEY IDENTITY,
	ProductName varchar(50) NOT NULL,
	ProductPrice varchar(50) NOT NULL
);

CREATE TABLE Customers
(
	CustomerID int NOT NULL PRIMARY KEY IDENTITY,
	CustomerFName varchar(50) NULL,
	CustomerLName varchar(50) NULL,
	CustomerPhone varchar(50) NULL,
	CustomerAddress varchar(50) NULL,
	CustomerCity varchar(50) NULL,
	CustomerState varchar(50) NULL,
	CustomerZipCode varchar(50) NULL
);

CREATE TABLE Orders
(
	OrderID int NOT NULL PRIMARY KEY IDENTITY,
	OrderDate DATE NOT NULL,
	ShippedDate DATE NOT NULL,
	CustomerID int NOT NULL	REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderDetails
(
	OrderDetailID int NOT NULL PRIMARY KEY IDENTITY,
	AmountOrdered int null,
	OrderID int NOT NULL  REFERENCES Orders(OrderID),
	ProductID int NOT NULL REFERENCES Products(ProductID)
);

CREATE TABLE Employees
(
	EmployeeID int NOT NULL PRIMARY KEY IDENTITY,
	FirstName varchar(50) NOT NULL,
	LastName Varchar(50) NOT NULL,
	EmailEmployee varchar(50) NOT NULL,
	OfficeID int NOT NULL  REFERENCES Offices(OfficeID),
	CustomerID int NOT NULL  REFERENCES Customers(CustomerID),
);
GO

--Inserting values into the 6 tables that were just created

INSERT INTO Customers VALUES('sean','dunn','3306082900','6973','mentor', 'ohio','44060');

INSERT into offices values('1234','Beachwood', 'Ohio', '44124','555-345-7890');

INSERT INTO Employees VALUES('Bill', 'Smith','bills@yahoo.com',1,1);

INSERT into orders values('11/24/2019','11/24/2019',1);

INSERT into products values('Yankee Candle', '34.99');

INSERT into OrderDetails values(123,1,1);


--Creating Views for each of the 6 tables 

--Customer Table View
	CREATE VIEW CustomerAddressID
	AS
	SELECT CustomerID, CustomerAddress, CustomerCity, CustomerState, CustomerZipCode
	FROM Customers;

--Employee Table View
	CREATE VIEW EmployeeInfo
	AS
	SELECT EmployeeID, FirstName, LastName
	FROM Employees;
 
--Offices Table View
	CREATE VIEW OfficeAddress
	AS
	SELECT Address, City, State, ZipCode
	FROM Offices;


--Order Details Table View
	CREATE VIEW OrderSpecifications
	AS
	SELECT OrderDetailID, AmountOrdered
	FROM OrderDetails; 

--Orders Table View
	CREATE VIEW OrderInfo
	AS
	SELECT OrderID, OrderDate, ShippedDate
	FROM Orders;

--Products Table View
	CREATE VIEW ProductInfo
	AS
	SELECT ProductName, ProductPrice
	FROM Products;



--Creating a JOIN View with the Orders and OrderDetails table 

CREATE VIEW OrderSpecInfo
AS
SELECT AmountOrdered, OrderDate, ShippedDate
FROM Orders JOIN OrderDetails
	ON Orders.OrderID = OrderDetails.OrderID;

--Creating a Procedure
	CREATE PROCEDURE CustomerInfo
	AS
	BEGIN
	SELECT CustomerID, CustomerFName, CustomerLName,CustomerAddress 
	FROM Customers
	Order By CustomerLName
	END;

--Creating two Queries
--Uses data from Orders and OrderDetails, SUM of AmountOrdered is called TotalAmount, ShippedDate and OrderDate listed.
--GroupBy OrderDetailID

	SELECT OrderDetailID, SUM(AmountOrdered) AS TotalAmount, ShippedDate, OrderDate
	FROM Orders JOIN OrderDetails
		ON Orders.OrderID = OrderDetails.OrderID
	GROUP BY OrderDetailID, ShippedDate, OrderDate;

--Uses Data from Products and OrderDetails, counting all as the LineItemCount, AmountOrdered is listed
--GroupBy ProductName

	SELECT ProductName, COUNT(*) AS LineItemCount, AmountOrdered
	FROM Products JOIN OrderDetails
		ON Products.ProductID = OrderDetails.ProductID
	GROUP BY ProductName, AmountOrdered;