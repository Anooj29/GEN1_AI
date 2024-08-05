import numpy as np
import pandas as pd
import matplotlib.pyplot as mlt

df = pd.read_csv("C:\GEN1_Artificial_Intelligence\Dataset\Trade dateset\commodity_trade_statistics_data.csv")

df.head()

df.describe()

df

list(df.columns)

df.head(10)

cdf = df[['country_or_area', 'year', 'comm_code', 'commodity', 'flow', 'trade_usd','weight_kg','quantity_name','quantity','category']]

mlt.scatter(cdf.year, cdf.trade_usd)
mlt.plot(cdf.year, cdf.trade_usd)