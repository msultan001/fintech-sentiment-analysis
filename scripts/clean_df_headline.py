"""
This module provides utility functions for text preprocessing and data loading.

Functions:
- clean_text(text): Cleans and normalizes input text by removing non-alphabetic characters,
  converting to lowercase, and removing English stopwords.
- load_data(path): Loads a CSV file into a pandas DataFrame and parses the 'date' column
  as datetime objects.
"""

import re
import pandas as pd
from nltk.corpus import stopwords

# Set of English stopwords to remove from text
stop_words = set(stopwords.words("english"))

def clean_text(text):
    """
    Clean and normalize input text.
    
    This function:
    - Converts text to lowercase
    - Removes all non-alphabetic characters
    - Replaces multiple whitespace characters with a single space
    - Removes English stopwords
    
    Parameters:
        text (str): The text string to be cleaned.
    
    Returns:
        str: The cleaned and normalized text.
    
    Example:
        >>> clean_text("Hello World! This is a test.")
        'hello world test'
    """
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return ' '.join([word for word in text.split() if word not in stop_words])

def load_data(path):
    """
    Load CSV data into a pandas DataFrame and parse dates.
    
    This function:
    - Reads a CSV file from the given path
    - Converts the 'date' column to datetime objects (invalid dates are set as NaT)
    
    Parameters:
        path (str): Path to the CSV file.
    
    Returns:
        pandas.DataFrame: DataFrame containing the loaded data with 'date' column as datetime.
    
    Example:
        >>> df = load_data("data.csv")
        >>> type(df['date'].iloc[0])
        <class 'pandas._libs.tslibs.timestamps.Timestamp'>
    """
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df
