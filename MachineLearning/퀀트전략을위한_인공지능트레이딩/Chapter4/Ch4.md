# CHAPTER 4 전통 퀀트 투자 전략

퀀트 투자 전략은 데이터 기반 전략

## 4.1 전통 퀀트 방법론 소개

정량적 방법론(모든 것을 수치화)을 기반으로 투자 의사를 결정

머신 러닝 관점에서는 input data가 몹시 중요

데이터 종류에 따라 주가를 사용해 기술 지표를 만들어 사용하는 **기술 지표 투자 전략**, 기업 재무제표를 사용하는 **가치 투자 전략** 으로 나눌 수 있음.

**기술 지표 투자 전략** 으로는 모멘텀, 평균회귀 두가지를 대표적으로 들 수 있는데,

오르는 주식은 계속 오른다 vs 떨어진다 임. 이것을 예시로 구현해볼 것.

## 4.2 평균 회귀 전략

**regression to mean** 많은 자료를 토대로 결과를 예측할 때 평균에 가까워지려는 경향

단순 선형 회귀 문제와 비슷하다

### 4.2.1 볼린저 밴드

현재 주가가 상대적으로 높은지 낮은지를 판단할 때 사용하는 보조 지표

중심선인 이동 평균선(moving average), 상단, 하단선인 표준 편차 밴드(standard deviation) 세 가지 선으로 이루어짐

보통 중심선ㅇ닌 이동 평균선을 계산할 땐 20일을 사용하고, 상하위 밴드는 20일 이동 평균선 +- 20일간의 이동 표준편차 \* 2 를 사용함

### 4.2.2 데이터 프레임

pandas로 불린저 밴드 공식을 간단히 구현 가능

### 4.2.3 데이터 가공

### 4.2.4 불린저 밴드 만들기

### 4.2.5 거래 전략

### 4.2.6 전략 수익률

### 4.2.7 변화 추이

## 4.3 듀얼 모멘텀 전략

상대 모멘텀 + 절대 모멘텀 전략

- 절대 모멘텀: 최근 수익률이 양수이면 매수, 음수이면 공매도

- 상대 모멘텀: 종목 중 최근 모멘텀이 상대적으로 높은 종목을 매수, 낮은 종목은 공매도

### 4.3.1 듀얼 모멘텀 전략 구현을 위한 절대 모멘텀 전략

### 4.3.2 듀얼 모멘텀 전략 구현을 위한 상대 모멘텀 전략

## 4.4 가치 투자 퀀트 전략

자본 수익률과 이익 수익률 순위를 매겨 상위 종목의 기업 선택

일정 금액 이상의 종목만, 이상치가 있는 종목은 제외