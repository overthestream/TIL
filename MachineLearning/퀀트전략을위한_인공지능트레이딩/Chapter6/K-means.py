import seaborn as sns
import pandas as pd
import pandas_datareader as dr
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import ssl

context = ssl._create_unverified_context()

sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
data_table = pd.read_html(sp500_url)
tickers = data_table[0]['Symbol'].tolist()

security = data_table[0]['Security'].tolist()
sector = data_table[0]['GICS Sector'].tolist()

tickers = tickers[0:60]
security = security[0:60]
sector = sector[0:60]
prices_list = []

for ticker in tickers:
    try:
        prices = dr.DataReader(ticker, 'yahoo', '01/01/2017')['Adj Close']
        prices = pd.DataFrame(prices)
        prices.columns = [ticker]
        prices_list.append(prices)
    except:
        pass
    prices_df = pd.concat(prices_list, axis=1)

prices_df.sort_index(inplace=True)

df = prices_df.pct_change().iloc[1:].T


companies = list(df.index)
movements = df.values

normalize = Normalizer()
array_norm = normalize.fit_transform(df)
df_norm = pd.DataFrame(array_norm, columns=df.columns)
final_df = df_norm.set_index(df.index)

col_mask = df.isnull().any(axis=0)
row_mask = df.isnull().any(axis=1)
df.loc[row_mask, col_mask]

num_of_clusters = range(2, 12)
error = []
for num_clusters in num_of_clusters:
    clusters = KMeans(num_clusters)
    clusters.fit(final_df)
    error.append(clusters.inertia_/100)
table = pd.DataFrame({"Cluster_Numbers": num_of_clusters, "Error_Term": error})

clusters = KMeans(7)
clusters.fit(final_df)

labels = clusters.predict(movements)

clustered_result = pd.DataFrame(
    {'labels': labels, 'tickers': companies, 'full-name': security, 'sector': sector})
clustered_result.sort_values('labels')

final_df['Cluster'] = clusters.labels_


print(final_df)
