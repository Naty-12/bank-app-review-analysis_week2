import cx_Oracle

# Connect to Oracle DB
dsn = cx_Oracle.makedsn('DESKTOP-I1S9JBO', 1521, service_name='XE')
conn = cx_Oracle.connect(user='SYSTEM', password='Adey', dsn=dsn)
cursor = conn.cursor()

print("\n1️⃣ Banks Table:")
cursor.execute("SELECT bank_id, bank_name FROM Banks")
for row in cursor.fetchall():
    print(row)

print("\n2️⃣ Sample Reviews:")
cursor.execute("""
    SELECT review_id, bank_id, SUBSTR(review_text, 1, 150) AS snippet, rating, review_date
    FROM Reviews WHERE ROWNUM <= 5
""")
for row in cursor.fetchall():
    print(row)

print("\n3️⃣ Total Reviews:")
cursor.execute("SELECT COUNT(*) FROM Reviews")
print("Total Reviews:", cursor.fetchone()[0])

print("\n4️⃣ Reviews per Bank:")
cursor.execute("""
    SELECT b.bank_name, COUNT(r.review_id) AS NumberOfReviews
    FROM Banks b
    JOIN Reviews r ON b.bank_id = r.bank_id
    GROUP BY b.bank_name
    ORDER BY NumberOfReviews DESC
""")
for row in cursor.fetchall():
    print(row)

print("\n5️⃣ Average Rating per Bank:")
cursor.execute("""
    SELECT b.bank_name, ROUND(AVG(r.rating), 2) AS AverageRating
    FROM Banks b
    JOIN Reviews r ON b.bank_id = r.bank_id
    GROUP BY b.bank_name
    ORDER BY AverageRating DESC
""")
for row in cursor.fetchall():
    print(row)

print("\n6️⃣ Sentiment Counts by Bank:")
cursor.execute("""
    SELECT b.bank_name, r.sentiment_textblob_label, COUNT(*) AS count
    FROM Banks b
    JOIN Reviews r ON b.bank_id = r.bank_id
    GROUP BY b.bank_name, r.sentiment_textblob_label
    ORDER BY b.bank_name, r.sentiment_textblob_label
""")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()