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

class Number:
"""
general representation of a number being even or odd
"""

    def __init__(self, number):
    """
    define number
    """
      self.number = number
    
    def odd_or_even(self)
	return 'odd' if number%2 !==0 else 'even'


ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))
