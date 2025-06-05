CREATE TABLE Banks (
    bank_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    bank_name VARCHAR2(100) NOT NULL
);

CREATE TABLE Reviews (
    review_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    review_text CLOB NOT NULL,
    rating NUMBER NOT NULL,
    sentiment_label VARCHAR2(20),
    sentiment_score FLOAT,
    review_date DATE,
    bank_id NUMBER,
    FOREIGN KEY (bank_id) REFERENCES Banks(bank_id)
);