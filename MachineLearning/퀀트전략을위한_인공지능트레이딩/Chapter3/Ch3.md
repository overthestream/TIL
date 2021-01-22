# CHAPTER 3 파이썬으로 만드는 투자 전략과 주요 지표

## 3.1 바이앤홀드 전략

바이앤홀드는 주식을 매수한 후 장기 보유하는 투자 전략

### 3.1.1 데이터 불러오기

```py
import pandas as pd
import numpy as np
df = pd.read_csv('../data/us_etf_data/AMZN.csv', index_col='Date', parse_dates=['Date'])
df.head()
```

### 3.1.2 결측치

df[df.isin([np.nan, np.inf, -np.inf]).any(1)]

### 3.1.3 데이터 슬라이싱

```py
price_df = df.loc[:, ['Adj Close']].copy()
# price_df.plot(figsize=(16, 9))

from_date = '1997-01-03'
to_date = '2003-01-03'

price_df.loc[form_date:to_date].plot(figsize=(16, 9))
```

### 3.1.4 일별 수익률 계산

```py
price_df['daily_rtn'] = price_df['Adj Close'].pct_change()
price_df.head(10)
```

```py
price_df['st_rtn'] = (1+price_df['daily_rtn']).cumprod()
price_df.head(10)
```

```py
price_df['st_rtn'].plot(figsize=(16,9))
```

## 3.2 투자 성과 분석 지표

- 연평균 복리 수익률 CAGR
- 최대 낙폭 MDD
- 변동성 Vol(Valaility)
- 샤프 지수 Sharpe ratio

### 3.2.1 CAGR

```py
CAGR = price_df.loc['2019-06-24', 'st_rtn'] ** (252./len(price_df.index)) -1
```

### 3.2.2 MDD

```py
historical_max = price_df['Adj Close'].cummax()
daily_drawdown = price_df['Adj Close'] / historical_max -1.0
historical_ dd = daily_drawdown.cummin()
historical_dd.plot()
```

### 3.2.3 Vol

```py
VOL = np.std(price_df['daily_rtn']) * np.sqrt(252.)
```

### Sharpe ratio

```py
Sharpe = np.mean(price_df['daily_rtn']) / np.std(price_df['daily_rtn']) * np.sqrt(252.)
```
