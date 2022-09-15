DROP TABLE IF EXISTS item, orders CASCADE;

CREATE TABLE item (
	id BIGSERIAL PRIMARY KEY ,
	name VARCHAR(100) NOT NULL UNIQUE,
	description TEXT,
	price NUMERIC(10,2) NOT NULL
);

INSERT INTO item 
	(name, price)
VALUES 
	('one', '100.10'),
	('two', '200.20'),
	('three', '300.30'),
	('four', '400.40')
;


CREATE TABLE orders (
	id BIGSERIAL PRIMARY KEY,
	item_id INT UNIQUE,
	amount INT NOT NULL CHECK(amount > 0),
	price NUMERIC(10,2) ,
    FOREIGN KEY(item_id) REFERENCES item(id)
);




