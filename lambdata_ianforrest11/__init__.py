"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np

def train_test_split(df, col):
    target = 'col'
    X = df.drop(columns=target)
    y = df[target]
    return X, y

def NaN(df):
    return df.isna().sum()

ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))
