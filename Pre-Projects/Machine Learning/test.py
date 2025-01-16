import numpy as np 
import pandas as pd 
import matplotlib.pyplot as mlt 
import sklearn as sk
import seaborn as sb



dgfhbjnklm

df = pd.read_csv("C:\\GEN1_Artificial_Intelligence\\Dataset\\Breast Cancer\\breast_cancer_dataset_data.csv")

df.head(10)

df.shape

df['diagnosis'].value_counts()   #B(Benign = NO cancer) and M(Malignant = YES)

# Questions 

df.shape

df.isnull().value_counts()
df.isnull().sum()

df.duplicated().sum()

df.info()

df.corr()

df.corr  #used to find pairwise correlation of all coloums (Any NAN value is automatically excluded) 

df.describe()

# df.drop('coloum name', axis=1, inplace=true)       --- to drop any coloum

df['diagnosis'].value_counts() 

#labbel encoding    ans: we use when we need to convert cargorical value into numerial value