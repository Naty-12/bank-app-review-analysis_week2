import pandas as pd
import re

df = pd.read_csv('data/raw_reviews.csv')
df.drop_duplicates(subset=['review', 'bank'], inplace=True)
df.dropna(subset=['review', 'rating'], inplace=True)
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.strip()
    text = re.sub('\s+', ' ', text)
    return text

df['review'] = df['review'].apply(clean_text)

df.to_csv('data/cleaned_reviews.csv', index=False)