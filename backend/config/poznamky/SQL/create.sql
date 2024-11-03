CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    employee_id INT,
    CONSTRAINT fk_employee_id
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
);


CREATE INDEX transaction_id ON transaction(name);
CREATE INDEX transaction_id_2 ON transaction(name, payment_type);


