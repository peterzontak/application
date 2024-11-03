
-- Inner Join
SELECT columns FROM table1 JOIN table2 ON table1.column = table2.column;
SELECT columns FROM table1 INNER JOIN table2 ON table1.column = table2.column;

-- Left Join
SELECT columns FROM table1 LEFT JOIN table2 ON table1.column = table2.column;

-- Right Join
SELECT columns FROM table1 RIGHT JOIN table2 ON table1.column = table2.column;



-- A CROSS JOIN is suitable when you need to generate all possible combinations of rows from two tables without any specific conditions.
It is valuable for generating Cartesian products, exploring combinations, and creating test datasets.

SELECT * FROM table1 CROSS JOIN table2;



JOIN / INNER JOIN
    Defaults to INNER JOIN
    Returns only rows with matches in both tables.
    Only matching rows from both tables.
LEFT JOIN
    Returns all rows from the left table, and matched rows from the right table; NULL if no match.
    All rows from left, matched or NULL from right.

RIGHT JOIN
    Returns all rows from the right table and matched rows from the left; NULL if no match.
    All rows from right, matched or NULL from left.
FULL JOIN / FULL OUTER JOIN (MySQL does not support FULL OUTER JOIN)
    Returns all records when there is a match in either left or right table; NULLs for non-matching records.
    All records from both tables with NULLs where there are no matches.


-- UNION / UNION ALL
Duplicate Rows:
    JOIN: Retains duplicate rows unless specified otherwise (e.g., using DISTINCT).
    UNION: Removes duplicate rows by default. If you want to keep duplicates, you can use UNION ALL.

NATURAL JOIN
    A type of INNER JOIN that automatically joins tables based on all columns with the same name and data type.
    `SELECT *
    FROM tableA
    NATURAL JOIN tableB;`

SELF JOIN
    A regular join where a table is joined with itself. This is useful for comparing rows within the same table.
    `SELECT a.column1, b.column2
    FROM table1 a, table1 b
    WHERE a.id = b.parent_id;`

INTERSECT (MySQL does not support)
    Similar to UNION, but it returns only the rows that are present in both result sets.
    `SELECT column_name FROM tableA
    INTERSECT
    SELECT column_name FROM tableB;`


EXCEPT (or MINUS) (MySQL does not support)
    Similar to UNION, but it returns only the rows that are present in the first result set but not in the second result set.
    `SELECT column_name FROM tableA
    EXCEPT
    SELECT column_name FROM tableB;`


-- Those two queries produce the same result
SELECT col1, col2 FROM TableA
INTERSECT
SELECT col1, col2 FROM TableB;

SELECT DISTINCT A.col1, A.col2
FROM TableA A
JOIN TableB B 
ON A.col1 = B.col1 AND A.col2 = B.col2;




INNER JOIN	Returns records with matching values in both tables.
LEFT JOIN	Returns all records from the left table, with matched records from the right; NULL if no match.
RIGHT JOIN	Returns all records from the right table, with matched records from the left; NULL if no match.
FULL OUTER JOIN	Combines results of both left and right joins, including unmatched rows from both tables.
CROSS JOIN	Returns the Cartesian product of two tables (every combination of rows).
UNION	Combines results of two or more queries into a single result set, removing duplicates.
UNION ALL	Combines results while retaining duplicates.
NATURAL JOIN	Joins tables based on columns with the same name and data type automatically.
SELF JOIN	Joins a table with itself to compare rows within the same table.
INTERSECT	Returns only rows present in both result sets.
EXCEPT (MINUS)	Returns rows from the first query that are not present in the second query.
