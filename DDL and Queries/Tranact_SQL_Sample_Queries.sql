--1.Write a SQL query to get the ProductID and Price for products with a Price of $100 or higher ?

SELECT product_id, price 
FROM product 
WHERE price >=100;

--2.Write a SQL query to get the ProductID, SupplierName, SupplierAddress for products whose price is below the average price of all products?


select p.product_id, sr.supplier_name, sr.supplier_address,p.price
from product p inner join supplies ss on p.product_id = ss.product_id
inner join supplier sr on sr.supplier_id = ss.supplier_id 
where p.price < (select AVG (price) from product)
order by price 

--3.Write a SQL query to get the customer and their corresponding online account?

select c.cust_id,oc.username 
from customer c,online_cust oc,online_acc oa
where c.cust_id = oc.cust_id and oc.username = oa.username

--5.Write a SQL query to list top 10 most expensive product?


SELECT TOP 10 product_id, price 
FROM PRODUCT
ORDER BY price DESC;

--6.List the products with product_id beginning with the letter “C” and that cost at least $250 ?


SELECT product_id
FROM product
WHERE product_id LIKE 'C%'
AND price >249;


--11. Write a SQL query to retrieve the product id, price of products
--that belong to the store located in Connecticut ?


SELECT p.product_id, p.price
FROM product p, store s, [contains] c
WHERE p.product_id = c.product_id
AND s.store_id = c.store_id
AND s.s_address like '%Jackson Lane%'

--20. Write a SQL query that shows productID for items that have an item cost between $500 and $1000 ?

SELECT product_id
FROM product
WHERE price between 500 and 1000;