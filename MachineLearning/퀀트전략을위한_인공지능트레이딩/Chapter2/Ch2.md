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