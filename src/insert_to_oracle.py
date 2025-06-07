import cx_Oracle
import pandas as pd
import os

# Load full sentiment data
df = pd.read_csv('data/cleaned_reviews_sentiment.csv')

# Connect to Oracle
dsn_tns = cx_Oracle.makedsn('DESKTOP-I1S9JBO', 1521, service_name='XE')
conn = cx_Oracle.connect(user='SYSTEM', password='Adey', dsn=dsn_tns)
cursor = conn.cursor()

# Run schema.sql
schema_path = os.path.join('sql', 'schema.sql')
with open(schema_path, 'r') as f:
    sql_commands = f.read().split(';')
for command in sql_commands:
    cmd = command.strip()
    if cmd:
        try:
            cursor.execute(cmd)
        except cx_Oracle.DatabaseError as e:
            print(f"Warning: {e}")  # skip errors like "table already exists"

# Insert banks
banks = df['bank'].unique()
bank_id_map = {}

for bank in banks:
    cursor.execute("SELECT bank_id FROM Banks WHERE bank_name = :1", [bank])
    result = cursor.fetchone()
    if result:
        # Bank already exists, get id
        bank_id_map[bank] = result[0]
    else:
        # Insert new bank
        cursor.execute("INSERT INTO Banks (bank_name) VALUES (:1)", [bank])
        cursor.execute("SELECT bank_id FROM Banks WHERE bank_name = :1", [bank])
        bank_id_map[bank] = cursor.fetchone()[0]

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Reviews (
            review_text, rating, review_date, bank_id, source,
            sentiment_textblob_score, sentiment_textblob_label,
            compound_score, sentiments_vader,
            label, predicted_sentiment
        ) VALUES (
            :1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5,
            :6, :7, :8, :9, :10, :11
        )
    """, [
        row['review'],
        row['rating'],
        row['date'],
        bank_id_map[row['bank']],
        row.get('source', None),
        row.get('sentiment_textblob_score', None),
        row.get('sentiment_textblob_label', None),
        row.get('compound_score', None),
        row.get('sentiments_vader', None),
        row.get('label', None),
        row.get('predicted_sentiment', None),
    ])

# Commit and close
conn.commit()
cursor.close()
conn.close()