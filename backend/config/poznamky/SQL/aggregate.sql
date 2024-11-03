-- Aggregating Data
SELECT COUNT(*) FROM table_name;

-- This will return the number of employees in each department.
SELECT department, COUNT(*) FROM employees GROUP BY department;


-- This will return only those departments that have more than 10 employees.
SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 10;




-- Select total sales for product with highest sales
SELECT product_id, product_type, SUM(price) AS Total
FROM sales_item
WHERE product_type IN ('shoes', 'electronics', 'books')
GROUP BY product_id, product_type
ORDER BY Total DESC
LIMIT 1;




SELECT
    COUNT(*) AS count,
    SUM(price) AS value,
    ROUND(AVG(price),2) AS avg,
    MAX(price) AS max,
    MIN(price) AS min
FROM sales_item;
