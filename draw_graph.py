import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from app import get_df

df = get_df()
# Gender
def get_graph_gender():
    persentase = []
    for gender in list(df['Gender'].unique()):
        persen = round((df["Exited"][df["Gender"]==gender].value_counts()[1]/df["Exited"][df["Gender"]==gender].value_counts().sum())*100, 2)
        persentase.append(persen)
        print(gender,": ", persen,"% to Exit Job")

    plt.bar(0, persentase[0])
    plt.bar(1, persentase[1])
    plt.xticks((0,1), ('Female','Male'))
    plt.xlabel("Gender")
    plt.ylabel("Percentage")
    plt.title("Percentage of gender to Exit")
    plt.savefig("feature graph/Gender.png")

# Geografi
def get_graph_geo():
    persentase = []
    for geo in list(df['Geography'].unique()):
        persen = round((df["Exited"][df["Geography"]==geo].value_counts()[1]/df["Exited"][df["Geography"]==geo].value_counts().sum())*100, 2)
        persentase.append(persen)
        print(geo,": ", persen,"% to Exit Job")

    for i in range(len(persentase)):
        plt.bar(i, persentase[i])
    plt.xticks((0,1,2), ('France', 'Spain', 'Germany'))
    plt.xlabel("Country")
    plt.ylabel("Percentage")
    plt.title("Percentage of Country to Exit")
    plt.savefig("feature graph/Geography.png")

def get_graph_age():
    plt.hist(df['Age'],bins=20)
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.savefig("feature graph/Age.png")

def scatter_age_not_exit():
    plt.scatter(x=range(len(list(df["Age"][df["Exited"]==0]))),y=df["Age"][df["Exited"]==0],s=1)
    plt.ylabel("Age")
    plt.xlabel("People (rows)")
    plt.title("People who did not Exit (Exited = 0)")
    plt.savefig("scatter graph/AgeScatterNotExit.png")

def scatter_age_exit():
    plt.scatter(x=range(len(list(df["Age"][df["Exited"]==1]))),y=df["Age"][df["Exited"]==1],s=1)
    plt.ylabel("Age")
    plt.xlabel("People (rows)")
    plt.title("People who Exited (Exited = 1)")
    plt.savefig("scatter graph/AgeScatterExit.png")

def age_percentage():
    age_bucket = df.groupby(pd.cut(df["Age"],bins=[10,20,30,40,50,60,70,80,90]))
    age_bucket = round((age_bucket.sum()["Exited"] / age_bucket.size())*100 , 2)

    x = [str(i)+"-"+str(i+10) for i in range(10,81,10)]

    plt.plot(x,age_bucket.values)
    plt.xlabel("Age Group")
    plt.ylabel("Percentage exited")
    plt.title("Percentage of people in different Age Groups that exited")
    plt.savefig("feature graph/AgePercentage.png")

age_percentage()