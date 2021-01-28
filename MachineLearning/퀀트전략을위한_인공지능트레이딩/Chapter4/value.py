import FinanceDataReader as fdr
import pandas as pd
import numpy as np
import csv


def sort_value(s_value, asc=True, standard=0):

    s_value_mask = s_value.mask(s_value < standard, np.nan)
    s_value_mask_rank = s_value_mask.rank(
        ascending=asc, na_option="bottom")

    return s_value_mask_rank


def MagicFormula(PER, ROA):

    PER_rank = sort_value(PER, asc=True)
    ROA_rank = sort_value(ROA, asc=False)

    result_rank = PER_rank + ROA_rank

    result = result_rank.rank(axis=1, ascending=True)

    result = result.where(result <= 10, 0)
    result = result.mask(result > 0, 1)

    return result


krx_df = fdr.StockListing('KRX')
df = pd.read_csv('../data/ch04/PER_ROA.csv', engine='python', encoding='cp949')
df = df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]

line_list = []
with open('../data/ch04/PER_ROA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if '' in row:
            pass
        else:
            line_list.append(row)

df = pd.DataFrame(data=line_list[1:], columns=line_list[0])
per = pd.to_numeric(df['PER'])
roa = pd.to_numeric(df['ROA'])

per_rank = sort_value(per, asc=True, standard=0)

roa_rank = sort_value(roa, asc=False, standard=0)

result_rank = per_rank + roa_rank
result_rank = sort_value(result_rank, asc=True)
result_rank = result_rank.where(result_rank <= 10, 0)
result_rank = result_rank.mask(result_rank > 0, 1)

mf_df = df.loc[result_rank > 0, ['종목명', '시가총액']].copy()
mf_stock_list = df.loc[result_rank > 0, '종목명'].values

mf_df['종목코드'] = ''
for stock in mf_stock_list:
    mf_df.loc[mf_df['종목명'] == stock,
              '종목코드'] = krx_df[krx_df['Name'] == stock]['Symbol'].values

mf_df['2019_수익률'] = ''
for x in mf_df['종목코드'].values:
    df = fdr.DataReader(x, '2019-01-01', '2019-12-31')
    cum_ret = df.loc[df.index[-1], 'Close'] / \
        df.loc[df.index[0], 'Close'] - 1
    mf_df.loc[mf_df['종목코드'] == x, '2019_수익률'] = cum_ret
    df = None

mf_df_rtn = pd.DataFrame()
for x in mf_df['종목코드'].values:
    df = fdr.DataReader(x, '2019-01-01', '2019-12-31')
    df['daily_rtn'] = df['Close'].pct_change(periods=1)
    df['cum_rtn'] = (1+df['daily_rtn']).cumprod()
    cum_ret = df.loc[df.index[-1], 'cum_rtn']
    mf_df.loc[mf_df['종목코드'] == x, '2019_수익률'] = cum_ret
    df = None

mf_df_rtn = pd.DataFrame()

for x in mf_df['종목코드'].values:
    df = fdr.DataReader(x, '2019-01-01', '2019-12-31') 
    df['daily_rtn'] = df['Close'].pct_change(periods=1)
    df['cum_rtn'] = (1+df['daily_rtn']).cumprod()
    cum_ret = df.loc[df.index[-1], 'cum_rtn']
    mf_df.loc[mf_df['종목코드'] == x, '2019_수익률'] = cum_ret 
    df = None
