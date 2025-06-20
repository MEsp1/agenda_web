.headers on
.mode column
PRAGMA foreign_keys = ON;

CREATE TABLE personas (
    id_persona INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre varchar(50),
    email varchar(50)

);

INSERT INTO personas (nombre, email) 
VALUES
('Dejah', 'dejah@gmail.com'),
('Jonh', 'jonh@gmail.com');

SELECT * FROM personas;

