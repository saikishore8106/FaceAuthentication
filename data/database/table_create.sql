CREATE DATABASE authticationdb;

CREATE TABLE authentication_logs (
    id SERIAL PRIMARY KEY,
    person_name VARCHAR(255),
    date DATE,
    time TIME,
    captured_image_path TEXT,
    auth_image_path TEXT
);


select * from authentication_logs;