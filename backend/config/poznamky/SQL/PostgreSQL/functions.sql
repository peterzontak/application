-- Functions
RETURNS (INTEGER, VARCHAR, TEXT, FLOAT, BOOLEAN)    -- scalar

-- single row
CREATE OR REPLACE FUNCTION get_employee() 
RETURNS emp AS $$
SELECT (name, salary, age) FROM employee WHERE id = 1;
$$ LANGUAGE SQL;

-- multi row
CREATE OR REPLACE FUNCTION get_all_employees() 
RETURNS SETOF employee AS $$
SELECT * FROM employee;
$$ LANGUAGE SQL;

-- table
CREATE OR REPLACE FUNCTION get_employee_details() 
RETURNS TABLE(name TEXT, salary NUMERIC) AS $$
SELECT name, salary FROM employee;
$$ LANGUAGE SQL;


-- Output Parameters:
CREATE OR REPLACE FUNCTION calculate(a INTEGER, b INTEGER, OUT sum INTEGER, OUT product INTEGER) AS $$
BEGIN
    sum := a + b;
    product := a * b;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION fn_update_employee_state(state_code char(2))
RETURNS void AS
$$
    UPDATE sales_person
    SET state = state_code
    WHERE state IS NULL;
$$
LANGUAGE SQL;



CREATE OR REPLACE FUNCTION fn_sales_person_by_state(state_code char(2))
RETURNS SETOF sales_person AS
$$
    SELECT * FROM sales_person
    WHERE state = state_code;
$$

LANGUAGE SQL;



CREATE OR REPLACE FUNCTION fn_get_sum(val1 int, val2 int)
RETURNS int AS
$$
DECLARE
    sum int;
BEGIN
    sum := val1 + val2;
    RETURN sum;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION fn_get_random_number(min_val int, max_val int)
RETURNS int AS
$$
DECLARE
    rand int;
BEGIN
    SELECT random() * (max_val - min_val + 1) + min_val INTO rand;
    RETURN sum;
END;
$$
LANGUAGE plpgsql;
