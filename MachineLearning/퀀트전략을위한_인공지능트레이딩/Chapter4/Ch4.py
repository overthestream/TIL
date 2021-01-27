import pandas as pd

df = pd.read_csv('MachineLearning/퀀트전략을위한_인공지능트레이딩/data/AMZN.csv')

price_df = df.loc[:, ['Date', 'Adj Close']].copy()
price_df.set_index(['Date'], inplace=True)
price_df['center'] = price_df['Adj Close'].rolling(window=20).mean()
price_df['ub'] = price_df['center'] + 2 * \
    price_df['Adj Close'].rolling(window=20).std()
price_df['lb'] = price_df['center'] - 2 * \
    price_df['Adj Close'].rolling(window=20).std()
print(price_df.iloc[18:25])
