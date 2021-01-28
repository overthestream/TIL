import os
import glob
import pandas as pd
import numpy as np
import datetime

DATE = 'Date'
CODE = 'CODE'
MONTHRET = '1M_RET'
CLOSE = 'Adj Close'
BASE_DATE = '2016-01-27'
STD_YM = 'STD_YM'
YMD = '%Y-%m-%d'
YM = '%Y-%m'
ACC = 'acc_rtn'


def dataPreprocess(sample, ticker, baseDate):
    sample[CODE] = ticker
    sample = sample[sample[DATE] >= baseDate][[DATE, CODE, CLOSE]].copy()

    sample.reset_index(inplace=True, drop=True)
    sample[STD_YM] = sample[DATE].map(
        lambda x: datetime.datetime.strptime(x, YMD).strftime(YM))
    sample[MONTHRET] = 0.0
    ymKeys = list(sample[STD_YM].unique())
    return sample, ymKeys


def createTradeBook(sample, sampleCodes):
    book = pd.DataFrame()
    book = sample[sampleCodes].copy()
    book[STD_YM] = book.index.map(
        lambda x: datetime.datetime.strptime(x, YMD).strftime(YM))
    for code in sampleCodes:
        book['p '+code] = ''
        book['r '+code] = ''
    return book


def trade(book, stockCodes):
    stdYm = ''
    isBuyPhase = False
    for stock in stockCodes:
        print(stock)
        for i in book.index:
            if book.loc[i, 'p '+stock] == '' and book.shift(1).loc[i, 'p '+stock] == 'ready ' + stock:
                stdYm = book.loc[i, STD_YM]
                isBuyPhase = True
            if book.loc[i, 'p '+stock] == '' and book.loc[i, STD_YM] == stdYm and isBuyPhase == True:
                book.loc[i, 'p '+stock] = 'buy '+stock
            if book.loc[i, 'p '+stock] == '':
                stdYm = None
                isBuyPhase = False
    return book


def computeReturn(book, stockCodes):
    rtn = 1.0
    buyDict = {}
    sellDict = {}
    num = len(stockCodes)

    for i in book.index:
        for stock in stockCodes:
            if book.loc[i, 'p '+stock] == 'buy ' + stock and book.shift(1).loc[i, 'p '+stock] == 'ready '+stock and book.shift(2).loc[i, 'p '+stock] == '':
                buyDict[stock] = book.loc[i, stock]
            elif book.loc[i, 'p '+stock] == '' and book.shift(1).loc[i, 'p '+stock] == 'buy '+stock:
                sellDict[stock] = book.loc[i, stock]
                rtn = (sellDict[stock]/buyDict[stock]) - 1
                book.loc[i, 'r '+stock] = rtn
                print('개별 청산일: ', i, '종목 코드: ', stock, '롱 진입 가격: ',
                      buyDict[stock], ' | 롱 청산 가격: ', sellDict[stock], ' | return: ', round(rtn*100, 2), '%')
            if book.loc[i, 'p '+stock] == '':
                buyDict[stock] = 0.0
                sellDict[stock] = 0.0
    accumulatedRtn = 1.0
    for i in book.index:
        rtn = 0.0
        count = 0
        for stock in stockCodes:
            if book.loc[i, 'p '+stock] == '' and book.shift(1).loc[i, 'p '+stock] == 'buy ' + stock:
                count += 1
                rtn += book.loc[i, 'r '+stock]
            if (rtn != 0.0) and (count != 0):
                accumulatedRtn *= (rtn/count)+1
                print('누적 청산일: ', i, '청산 종목 수: ', count, '청산 수익률: ', round(
                    (rtn/count), 4), '누적 수익률: ', round(accumulatedRtn, 4))
        book.loc[i, ACC] = accumulatedRtn
    print('누적 수익률: ', round(accumulatedRtn, 4))


route = 'MachineLearning/퀀트전략을위한_인공지능트레이딩/data/us_etf_data/*.csv'
files = glob.glob(route)

monthlyLastDataFrame = pd.DataFrame(columns=[DATE, CODE, MONTHRET])
stockDataFrame = pd.DataFrame(columns=[DATE, CODE, CLOSE])

for file in files:
    if os.path.isdir(file):
        print('%s <DIR> ' % file)
    else:
        folder, name = os.path.split(file)
        head, tail = os.path.splitext(name)
        print(file)
        readDataFrame = pd.read_csv(file)
        priceDataFrame, ymKeys = dataPreprocess(readDataFrame, head, BASE_DATE)
        stockDataFrame = stockDataFrame.append(
            priceDataFrame.loc[:, [DATE, CODE, CLOSE]], sort=False)
        for ym in ymKeys:
            mRet = priceDataFrame.loc[priceDataFrame[priceDataFrame[STD_YM] == ym].index[-1], CLOSE] / \
                priceDataFrame.loc[priceDataFrame[priceDataFrame[STD_YM]
                                                  == ym].index[0], CLOSE]
            priceDataFrame.loc[priceDataFrame[STD_YM]
                               == ym, [MONTHRET]] == mRet
            monthlyLastDataFrame = monthlyLastDataFrame.append(
                priceDataFrame.loc[priceDataFrame[priceDataFrame[STD_YM] == ym].index[-1], [DATE, CODE, MONTHRET]])

monthlyRetDataFrame = monthlyLastDataFrame.pivot(DATE, CODE, MONTHRET).copy()
monthlyRetDataFrame = monthlyRetDataFrame.rank(
    axis=1, ascending=False, method='max', pct=True)

monthlyRetDataFrame = monthlyRetDataFrame.where(
    monthlyRetDataFrame < 0.4, np.nan)
monthlyRetDataFrame.fillna(0, inplace=True)
monthlyRetDataFrame[monthlyRetDataFrame != 0] = 1
stockCodes = list(stockDataFrame[CODE].unique())

signalDict = dict()
for date in monthlyRetDataFrame.index:
    tickerList = list(
        monthlyRetDataFrame.loc[date, monthlyRetDataFrame.loc[date, :] >= 1.0].index)
    signalDict[date] = tickerList

stockCMatrix = stockDataFrame.pivot(DATE, CODE, CLOSE).copy()
book = createTradeBook(stockCMatrix, list(stockDataFrame[CODE].unique()))

for date, values in signalDict.items():
    for stock in values:
        book.loc[date, 'p '+stock] = 'ready '+stock

book = trade(book, stockCodes)

computeReturn(book, stockCodes)
