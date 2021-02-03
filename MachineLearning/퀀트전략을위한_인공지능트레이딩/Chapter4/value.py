import FinanceDataReader as fdr
import numpy as np
import pandas as pd
import csv

from pandas.core.frame import DataFrame

route = 'MachineLearning/퀀트전략을위한_인공지능트레이딩/data/ch04/PER_ROA.csv'
krxDataFrame = fdr.StockListing('KRX')

lineList = []
with open(route) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        if '' in row:
            pass
        else:
            lineList.append(row)
dataFrame = pd.DataFrame(data=lineList[1:], columns=lineList[0])
dataFrame = dataFrame[~dataFrame.isin([np.nan, np.inf, -np.inf]).any(1)]


def sortVal(series, asc=True, standard=0):
    '''
    특정 지표를 정렬 
    series: pandas Series
        정렬할 데이터 
    asc: bool 
        True: 오름차순
        False: 내림차순
    standard: number
        조건에 맞는 값을 True로 대체하기 위한 기준 값
    returns: 
        rankedSeries: pandas Series 
            정렬된 순위 
    '''
    maskedSeries = series.mask(series < standard, np.nan)
    rankedSeries = maskedSeries.rank(ascending=asc, na_option="bottom")
    return rankedSeries


PER = pd.to_numeric(dataFrame['PER'])
ROA = pd.to_numeric(dataFrame['ROA'])

rankedPER = sortVal(PER, asc=True, standard=0)
rankedROA = sortVal(ROA, asc=False, standard=0)

resultRank = rankedPER + rankedROA
resultRank = sortVal(resultRank, asc=True)
resultRank = resultRank.where(resultRank <= 10, 0)
resultRank = resultRank.mask(resultRank > 0, 1)


mfDataFrame = dataFrame.loc[resultRank > 0, ['종목명', '시가총액']].copy()
mfStockList = dataFrame.loc[resultRank > 0, '종목명'].values

mfDataFrame['종목 코드'] = ''
for stock in mfStockList:
    mfDataFrame.loc[mfDataFrame['종목명'] == stock,
                    '종목 코드'] = krxDataFrame[krxDataFrame['Name'] == stock]['Symbol'].values

mfDataFrame['2019 수익률'] = ''
for x in mfDataFrame['종목 코드'].values:
    dataFrame = fdr.DataReader(x, '2019-01-01', '2019-12-31')
    cumRet = dataFrame.loc[dataFrame.index[-1], 'Close'] / \
        dataFrame.loc[dataFrame.index[0], 'Close'] - 1
    mfDataFrame.loc[mfDataFrame['종목 코드'] == x, '2019 수익률'] = cumRet
    dataFrame = None

for ind, val in enumerate(mfDataFrame['종목 코드'].values):
    codeName = mfDataFrame.loc[mfDataFrame['종목 코드'] == val, '종목명'].values[0]
    dataFrame = fdr.DataReader(val, '2019-01-01', '2019-12-31')
    if ind == 0:
        mfDataFrameReturn = pd.DataFrame(index=dataFrame.index)
    dataFrame['daily return'] = dataFrame['Close'].pct_change(periods=1)
    dataFrame['accumulated return'] = (1+dataFrame['daily return']).cumprod()
    tmp = dataFrame.loc[:, ['accumulated return']].rename(
        columns={'accumulated return': codeName})
    mfDataFrameReturn = mfDataFrameReturn.join(tmp, how='left')
    dataFrame = None
print(mfDataFrameReturn)
