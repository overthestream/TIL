# CHAPTER 2 금융 데이터 분석을 위한 파이썬 활용법

## 2.1 날짜와 시간

datetime, numpy의 날짜 시간, numpy 기반의 pandas의 날짜와 시간

### 2.1.1 파이썬 라이브러리

STL인 datetime

datetime -> date, datetime, datetime_CAPI, MAXYEAR, MINYEAR, sys, time, timedelta, timezone, tzinfo

date, time이 각각 모듈 형식

### 2.1.2 넘파이 라이브러리

날짜와 시간을 datetime64 객체로 표현 :10 ^ -18 단위까지 관리

### 2.1.3 판다스 라이브러리

테이블 데이터 및 시계열 데이터 구조를 조작하는 탁월한 기능을 제공

넘파이의 datetime64 기반으로 이루어짐. 날짜 범위 생성, 날짜 변환, 날짜 이동 등이 있고, 객체 인덱싱을 통해 데이터 필터링, 인덱싱, 피벗팅, 정렬, 슬라이싱 등 다양한 활용 가능

## 2.2 금융 데이터 전처리와 분석을 위한 판다스 사용법

### 2.2.1 가장 중요한 준비 과정 - 데이터 불러오기

pandas.read\_[파일 종류] 함수 이용

#### 예시

```py
import pandas as pd
df = pd.read_csv('../data/us_etf_data/AAPL.csv')
df.head() # head는 상위 5개 행만 호출하는 함수
```

판다스는 두 개의 객체로 데이터 구조를 이룸

- Series: 1차원 구성, 배열과 비슷한 형태
- DataFrame: 2차원 테이블 형식, row와 column으로 구성
  - row는 index를, column은 Series 객체로 변수 의미

데이터 read 시 다양한 매개 변수로 옵션을 줄 수 있음 .

```py
aapl_dp = pd.read_csv('./data/us_etf_data\AAPLS.csv', index_col='Date', parse_dates=['Date']) # index로 설정할 colmun 명, Date가 index로 됨 | parse_date로 Date column의 값을 timestamp로 변환
print(aapl_df.head())
print(type(aapl_df.index))
print(type(aapl_df.index[0]))
```

### 2.2.2 에러의 주된 원인 제거 - 결측치와 이상치 다루기

데이터 수집 과정에서 사람의 실수나 전산 오류 등 여러 가지 이유로 결측치(missing value)가 발생한다.

결측치 발생 시 아무리 좋은 알고리즘이어도 성능이 안좋아질 우려가 있음

#### 결측치 존재하는지 확인하기

판다스에서 결측치 데이터는 NaN으로 표시됨.

무한값 때문에 에러가 발생하는 일도 잦으므로 무한값 또한 결측치로 간주

NaN을 확인하는 함수는 isna(), isnull(), isin() 세 가지가 있다.

```py
df['S1'].isna()
df.isna()
```

이런 식으로 호출 가능

```py
df.isna().sum()
```

이렇게 하면 결측치가 몇 개 존재하는지도 알 수 있다~

```py
df.isin([np.nan])
```

df에 np.nan (NaN) 존재 여부 반환

#### 결측치 처리

걀측치 처리 방법에는 다른 값으로 채우는 방법과 그 부분을 제거하는 방법 2가지가 있다.

데이터가 적다면 제거하는 것보다는 대체 값을 고안하는 것이 낫다.

```py
df.fillna(다른 값) # NaN을 다른 값으로 채움
df.fillna(method='bfill') # 이전 행의 값으로 채움 (사전관찰편향 back-ahead-bias 우려) -> forward fill 많이 사용
df.dropna() # 결측치가 발생한 행이나 열 제거 (axis='rows'|'columns') 이런 식
```

### 2.2.3 데이터 선택 방법 - 슬라이싱, 인덱싱, 서브셋 데이터 추출

indexing은 위치 정보의 개념, slicing은 인덱스를 기반으로 어떤 부분을 잘라내는 것

pandas의 인덱싱은 파이선의 그것과 비슷.

#### column 선택 :

```py
df[['Open', 'High']]
```

이런 식으로 column을 리스트 형태로 인덱스에 전달

#### row 선택 :

```py
df[0:3]
```

#### indexer

loc indexer : 인덱스 라벨 값 기반 인덱싱

iloc indexer : 정수형 값 기반 인덱싱

```py
df.loc['2018-10-10':'2018-10-20', ['Open','Close', 'High','Low']]
```

이런 식으로 행 열 동시 접근 가능

### 2.2.4 금융 시계열 데이터 분석에 유용한 판다스 함수

#### shift() 함수

인덱스에 연결된 데이터를 일정 간격으로 이동시키는 함수

인자로 넣어준 수만큼 날짜가 이동 (양수, 음수 둘다 가능)

#### pct_change() 함수

현재 값과 이전 요소 값의 백분율 변화량을 연산하는 함수

#### diff() 함수

변화율이 아닌 변화량 계산 날짜수, 행 렬 변환 인자로 가능

#### rolling() 함수

이동 평균선 계산

#### resample() 함수

시간 간격으 재조정

resampling

## 2.3 금융 데이터 분석을 위한 오픈 API 활용

금융 및 주가 데이터를 가져오는 방법 네가지

- 데이터 구매
- 증권사 API 이용
- 금융 웹 페이지 크롤링
- 금융 데이터 제공 오픈 API 사용

### 2.3.1 API

### 2.3.2 FinanceDataReader

```sh
pip install -U finance-datereader
```

```py
import FinanceDataReader as fdr
df_krx = fdr.StockListing('KRX')
print(len(df_krx))
df_krx.head()
```
한국의 모든 종목 리스트 가져옴 