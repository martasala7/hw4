import os
import pandas as pd

def load_data():
    """Load the dataset from the given file path."""
    file_path = os.path.join(os.path.dirname(__file__), 'sample_diabetes_mellitus_data.csv')
    return pd.read_csv(file_path, delimiter=';')

def clean_data(df):
    """Remove rows with NaN in 'age', 'gender', 'ethnicity' and fill NaN in 'height' and 'weight'."""
    df = df.dropna(subset=['age', 'gender', 'ethnicity'])
    df.loc[:, 'height'] = df['height'].fillna(df['height'].mean())
    df.loc[:, 'weight'] = df['weight'].fillna(df['weight'].mean())
    return df

def encode_ethnicity(df):
    """Generate dummies for 'ethnicity'."""
    df = pd.get_dummies(df, columns=['ethnicity'], prefix='ethnicity')
    return df

def binary_variables_gender(df):
    """Create binary variable for 'gender'."""
    df['gender_binary'] = df['gender'].map({'M': 1, 'F': 0})
    return df