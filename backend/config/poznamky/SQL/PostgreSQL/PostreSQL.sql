
CREATE TYPE sex_type as ENUM ('male', 'female');

ALTER TABLE customer
ALTER COLUMN sex TYPE sex_type USING sex::sex_type;


CREATE TABLE product(
    id SERIAL PRIMARY KEY,
    type_id INTEGER REFERENCES product_type(id),
    price INTEGER
)


-- SIMILIAR TO
In addition to % and _, SIMILAR TO supports:
    |: Represents alternation (logical OR).
    *: Matches zero or more occurrences of the preceding element.
    +: Matches one or more occurrences of the preceding element.
    {m,n}: Matches between m and n occurrences of the preceding element.

WHERE col_name SIMILIAR TO 'M%'  -- any number of characters following it, including none
WHERE col_name SIMILIAR TO '%M'  -- anything before M
SELECT * FROM table_name WHERE column_name SIMILAR TO 'M{1,3}'; -- Matches strings starting with 'M' followed by one to three characters.
WHERE col_name SIMILIAR TO 'M%' OR col_name SIMILIAR TO '%M';

-- Regular Expressions
~ '^M.*';  -- Matches any string starting with M
WHERE some_column ~ '^Ma';    --  ~ means case sensitive regular expression
WHERE some_column ~* '^Ma';   --  ~* means case insensitive regular expression

