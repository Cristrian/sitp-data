-- Create database postgres with utf-8
CREATE DATABASE sitp_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;