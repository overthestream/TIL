import matplotlib.pylab as plt
import pandas as pd

period = 20
sigmaWeight = 2
baseDate = '2020-02-19'

route = 'MachineLearning/퀀트전략을위한_인공지능트레이딩/data/AMZN.csv'

df = pd.read_csv(route)
price_df = df.loc[:, ['Date', 'Adj Close']].copy()
price_df.set_index(['Date'], inplace=True)


def bollingerBand(price_df, period, sigmaWeight, baseDate):
    bollinger = price_df.copy()
    bollinger['center'] = bollinger['Adj Close'].rolling(window=period).mean()
    bollinger['upper'] = bollinger['center'] + sigmaWeight * \
        bollinger['Adj Close'].rolling(window=period).std()
    bollinger['lower'] = bollinger['center'] - sigmaWeight * \
        bollinger['Adj Close'].rolling(window=period).std()
    sliced = bollinger.loc[baseDate:]

    return sliced


def createTradeBook(sample):
    book = sample[['Adj Close']].copy()
    book['trade'] = ''
    return book


def tradings(sample, book):
    for i in sample.index:
        if sample.loc[i, 'Adj Close'] > sample.loc[i, 'upper']:
            book.loc[i, 'trade'] = ''
        elif sample.loc[i, 'lower'] > sample.loc[i, 'Adj Close']:
            # if book.shift(1).loc[i, 'trade'] == 'buy':
            book.loc[i, 'trade'] = 'buy'
            # else:
            #    book.loc[i, 'trade'] = 'buy'
        elif sample.loc[i, 'upper'] >= sample.loc[i, 'Adj Close'] and sample.loc[i, 'Adj Close'] >= sample.loc[i, 'lower']:
            if book.shift(1).loc[i, 'trade'] == 'buy':
                book.loc[i, 'trade'] = 'buy'
            else:
                book.loc[i, 'trade'] = ''
    return book


def returns(book):
    rtn = 1.0
    book['return'] = 1
    buy = 0.0
    sell = 0.0

    for i in book.index:
        if book.loc[i, 'trade'] == 'buy' and book.shift(1).loc[i, 'trade'] == '':
            buy = book.loc[i, 'Adj Close']
            print('진입일: ', i, 'long 진입 가격: ', buy)
        elif book.loc[i, 'trade'] == '' and book.shift(1).loc[i, 'trade'] == 'buy':
            sell = book.loc[i, 'Adj Close']
            rtn = (sell - buy) / buy + 1
            book.loc[i, 'return'] = rtn
            print('청산일: ', i, 'long 진입 가격: ', buy,
                  ' | long 청산 가격: ', sell, '| 수익률: ', round(rtn, 4))

        if book.loc[i, 'trade'] == '':
            buy = 0.0
            sell = 0.0

    acc_rtn = 1.0
    for i in book.index:
        rtn = book.loc[i, 'return']
        acc_rtn = acc_rtn * rtn
        book.loc[i, 'acc return'] = acc_rtn
    print('Accumulated return: ', round(acc_rtn, 4))
    return (round(acc_rtn, 4))


bollinger = bollingerBand(price_df, period, sigmaWeight, baseDate)
book = createTradeBook(bollinger)
book = tradings(bollinger, book)
returns(book)
print(book['acc return'].plot())
