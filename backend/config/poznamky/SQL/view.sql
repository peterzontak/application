CREATE VIEW view_name AS
SELECT table_1.column1, table_2.column2, table_3.column3
FROM table_1
JOIN table_2 ON table_1.id = table_2.foreign_id
JOIN table_3 ON table_2.id = table_3.foreign_id;
