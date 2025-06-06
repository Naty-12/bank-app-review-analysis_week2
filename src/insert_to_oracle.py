# 1. Import Libraries
import cx_Oracle
import pandas as pd

# 2. Load Cleaned Data
df = pd.read_csv('data/cleaned_reviews.csv')

# 3. Connect to Oracle DB
dsn_tns = cx_Oracle.makedsn('DESKTOP-I1S9JBO', 1521, service_name='XE')
conn = cx_Oracle.connect(user='BEL', password='Adey793010!@', dsn=dsn_tns)
cursor = conn.cursor()

# 4. Insert Banks and Map to IDs
banks = df['bank'].unique()
bank_id_map = {}

for bank in banks:
    cursor.execute("INSERT INTO Banks (bank_name) VALUES (:1)", [bank])
    cursor.execute("SELECT bank_id FROM Banks WHERE bank_name = :1", [bank])
    bank_id = cursor.fetchone()[0]
    bank_id_map[bank] = bank_id

# 5. Insert Reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Reviews (
            review_text, rating, sentiment_label,
            sentiment_score, review_date, bank_id
        ) VALUES (
            :1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6
        )
    """, [
        row['review'], row['rating'], row['sentiment_label'],
        row.get('sentiment_score', None), row['date'],
        bank_id_map[row['bank']]
    ])

# 6. Commit and Close
conn.commit()
cursor.close()
conn.close()