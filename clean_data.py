from app import get_df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = get_df()
numeric_columns = [col for col in df.columns if ((df[col].dtype=='int64' or df[col].dtype=='float64') and col!='Exited')]
#min = df[df['EstimatedSalary'] == df['EstimatedSalary'].min()]

#Dummy Encoding
df["Age"] = pd.cut(df["Age"],bins=[10,20,30,40,50,60,70,80])
df = pd.get_dummies(df)

#Remove Dummy Variable Trap
df = df.drop(columns=["Geography_France","Gender_Female"],axis=1)
df.to_csv('dataset/Clean_data.csv')
print(df.head())