
DELIMITER //

CREATE FUNCTION fn_update_employee_state() 
RETURNS INT DETERMINISTIC
BEGIN
    UPDATE sales_person
    SET state = 'PA'
    WHERE state IS NULL;
    
    RETURN ROW_COUNT(); -- Returns the number of rows affected
END //

DELIMITER ;
