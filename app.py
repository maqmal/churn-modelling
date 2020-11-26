import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_df():
    df = pd.read_csv('dataset/Churn_Modelling.csv')
    remove_col = ['RowNumber','CustomerId','Surname']
    return df.drop(columns=remove_col, axis=1)

df = get_df()





