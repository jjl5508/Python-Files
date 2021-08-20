USE mydb;
INSERT INTO dojos (name) VALUES ('Meat Pie');
INSERT INTO dojos (name) VALUES ('American Pie');
INSERT INTO dojos (name) VALUES ('Korean Pie');

SELECT * FROM dojos;

DELETE FROM dojos WHERE id = 1;
DELETE FROM dojos WHERE id = 2;
DELETE FROM dojos WHERE id = 3;

INSERT INTO dojos (name) VALUES ('Peach Pie');
INSERT INTO dojos (name) VALUES ('Viet Pie');
INSERT INTO dojos (name) VALUES ('Strawberry Pie');

INSERT INTO ninjas (first_name,last_name, dojos_id) VALUES ('Chicken', 'McTender', 7);
INSERT INTO ninjas (first_name,last_name, dojos_id) VALUES ('Beef', 'McTender', 7);
INSERT INTO ninjas (first_name,last_name, dojos_id) VALUES ('Filet', 'McTender', 7);

INSERT INTO ninjas (first_name,last_name, dojos_id) VALUES ('Chicken', 'McTender', 8);
INSERT INTO ninjas (first_name,last_name, dojos_id) VALUES ('Beef', 'McTender', 8);
INSERT INTO ninjas (first_name,last_name, dojos_id) VALUES ('Filet', 'McTender', 8);

INSERT INTO ninjas (first_name,last_name, dojos_id) VALUES ('Chicken', 'McTender', 9);
INSERT INTO ninjas (first_name,last_name, dojos_id) VALUES ('Beef', 'McTender', 9);
INSERT INTO ninjas (first_name,last_name, dojos_id) VALUES ('Filet', 'McTender', 9);

SELECT * FROM ninjas;


SELECT * FROM ninjas WHERE ninjas.dojos_id = 7;
SELECT * FROM ninjas WHERE ninjas.dojos_id = 8;
SELECT * FROM ninjas WHERE ninjas.dojos_id = 9;

ALTER TABLE ninjas
DROP COLUMN dojo_id;

