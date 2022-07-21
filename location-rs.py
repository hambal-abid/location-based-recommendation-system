from statistics import mean
from unicodedata import name
import numpy as np
import pandas as pd
import geocoder

g = geocoder.ip("me")
print(g.city)

df1=pd.read_csv("volunteers-data.csv")


df2=pd.read_csv("ratings-data.csv")

col = list(df2.columns)

mean_col = df2[col[1:]].mean(axis=1,skipna=True)

df3 = df1
df3['ratings'] = list(mean_col)

print(df3)
print(df3.sort_values(by=['ratings'],ascending=False).loc[(df1['city'] == g.city)])
