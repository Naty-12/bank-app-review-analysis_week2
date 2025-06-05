import pandas as pd
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

df = pd.read_csv('data/raw_reviews.csv')
df.drop_duplicates(subset=['review', 'bank'], inplace=True)
df.dropna(subset=['review', 'rating'], inplace=True)
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(tokens)

# Apply preprocessing
df['review'] = df['review'].apply(preprocess_text)

# Replace empty strings with NaN (safe assignment)
df['review'] = df['review'].replace('', np.nan)

# Drop rows where review or rating is NaN
df.dropna(subset=['review', 'rating'], inplace=True)

df.to_csv('data/cleaned_reviews.csv', index=False)