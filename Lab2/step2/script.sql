drop table Authors;
drop table Books;
CREATE TABLE Authors (
    author_id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    date_of_birth DATE,
    place_of_birth VARCHAR2(100)
);
INSERT INTO Authors (author_id, name, date_of_birth, place_of_birth)
VALUES (1, 'Alexander Pushkin', TO_DATE('1799-06-06', 'YYYY-MM-DD'), 'Moscow');
INSERT INTO Authors (author_id, name, date_of_birth, place_of_birth)
VALUES (2, 'Lev Tolstoy', TO_DATE('1828-09-09', 'YYYY-MM-DD'), 'Yasnsaya Polyana');
INSERT INTO Authors (author_id, name, date_of_birth, place_of_birth)
VALUES (3, 'Stephen King', TO_DATE('1947-09-21', 'YYYY-MM-DD'), 'Portland');
INSERT INTO Authors (author_id, name, date_of_birth, place_of_birth)
VALUES (4, 'Charles Dickens', TO_DATE('1812-02-07', 'YYYY-MM-DD'), 'Portsmouth');
INSERT INTO Authors (author_id, name, date_of_birth, place_of_birth)
VALUES (5, 'Jane Austen', TO_DATE('1775-12-16', 'YYYY-MM-DD'), 'Steventon');
SELECT * FROM Authors;

CREATE TABLE Books (
    book_id NUMBER PRIMARY KEY,
    name varchar2(100),
    author_id NUMBER,
    rating numeric(2,1),
    CONSTRAINT fk_books FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

INSERT INTO Books (book_id, name, author_id, rating) VALUES (1, 'Evgeniy Onegin', 1, 4.1);
INSERT INTO Books (book_id, name, author_id, rating) VALUES (2, 'It', 3, 4.2);
INSERT INTO Books (book_id, name, author_id, rating) VALUES (3, 'Great Expectations', 4, 4.3);
INSERT INTO Books (book_id, name, author_id, rating) VALUES (4, 'Garry Potter', null, 4.8);
INSERT INTO Books (book_id, name, author_id, rating) VALUES (5, 'Pride and Prejudice', 5, 4.3);
SELECT * FROM Books;