# text_cleaner.py

import re

def clean_text(text):
    # Remove newline characters
    text = text.replace('\n', ' ')
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters and digits (if not relevant)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip()
