
SELECT DISTINCT state
FROM customer
WHERE state IN ('CA', 'NY', 'TX')
ORDER BY state ASC;

