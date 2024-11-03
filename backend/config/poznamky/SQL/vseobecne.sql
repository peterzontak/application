
/* CURRENT_TIMESTAMP */

-- MariaDB
CREATE TABLE orders (
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- MySQL
CREATE TABLE orders (
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


-- PostgreSQL
CREATE TABLE orders (
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



`<>` is more compatible than `!=`

WHERE col_name IS NULL

WHERE col_name IS NOT NULL

-- LIKE
WHERE col_name LIKE '%M___'     -- 3 underscores means 3 required characters

-- REGEXP (or RLIKE as an alias). MariaDB + MySQL only, PostgreSQL uses `~`
REGEXP '^M.*';  -- Matches any string starting with M



-- CONCAT
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;

-- EXTRACT
EXTRACT(field FROM source)
SELECT EXTRACT(YEAR FROM CURRENT_DATE);
SELECT EXTRACT(MONTH FROM TIMESTAMP '2023-01-01 12:00:00');

SELECT first_name, last_name
FROM customer
WHERE EXTRACT(YEAR FROM date) = 2020
UNION
SELECT first_name, last_name
FROM sales_person
WHERE EXTRACT(YEAR FROM date) = 2020
ORDER BY birth_date ASC;

SELECT EXTRACT(MONTH FROM date) AS month, COUNT(*) AS count
FROM sales_item
GROUP BY month
HAVING COUNT(*) > 10
ORDER BY month DESC;
