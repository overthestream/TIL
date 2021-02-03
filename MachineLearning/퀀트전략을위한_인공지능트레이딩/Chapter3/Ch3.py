import pandas as pd
import numpy as np

df = pd.read_csv('MachineLearning/퀀트전략을위한_인공지능트레이딩/data/AMZN.csv',
                 index_col='Date', parse_dates=['Date'])
print(df.head())

print(df[df.isin([np.nan, np.inf, -np.inf]).any(1)])

price_df = df.loc[:, ['Adj Close']].copy()
# price_df.plot(figsize=(16, 9))

from_date = '1997-01-03'
to_date = '2003-01-03'

price_df.loc[form_date:to_date].plot(figsize=(16, 9))

price_df['daily_rtn'] = price_df['Adj Close'].pct_change()
price_df.head(10)

price_df['st_rtn'] = (1+price_df['daily_rtn']).cumprod()
price_df.head(10)

price_df['st_rtn'].plot(figsize=(16, 9))
