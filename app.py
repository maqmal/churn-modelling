import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

#Helper Function
def get_df():
    df = pd.read_csv('dataset/Churn_Modelling.csv')
    remove_col = ['RowNumber','CustomerId','Surname']
    return df.drop(columns=remove_col, axis=1)

df = pd.read_csv('dataset/Clean_data.csv')
#Remove index column
df = df.drop(df.columns[0], axis=1)
label_y = df['Exited']
feature = df.drop(columns=['Exited'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(feature, label_y, test_size=0.3)

scale_x = StandardScaler()
X_train = scale_x.fit_transform(X_train)
X_test = scale_x.fit_transform(X_test)

#SVM
support_vector_classifier = SVC(kernel='rbf')
support_vector_classifier.fit(X_train, y_train)
y_prediction = support_vector_classifier.predict(X_test)

#Confusion Matrix
confusion = confusion_matrix(y_test,y_prediction)
print("=======================================")
print("Confusion Matrix:")
print(confusion)
numerator = confusion[0][0] + confusion[1][1]
denominator = sum(confusion[0]) + sum(confusion[1])
acc_svc = (numerator/denominator) * 100
print("Accuracy : ",round(acc_svc,2),"%")
print("=======================================\n")

#Cross Validation
cross_val_svc = cross_val_score(estimator = SVC(kernel = 'rbf'), X = X_train, y = y_train, cv = 10, n_jobs = -1)
print("Cross Validation Accuracy : ",round(cross_val_svc.mean() * 100 , 2),"%")