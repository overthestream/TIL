# 파이썬 가상환경 만들기

```sh
# 만들기 (경로에는 가상환경 이름 폴더 추가)
# ex: python3 -m venv ./MachineLearning/퀀트전략을위한_인공지능트레이딩/myvenv -> myvenv라는 가상환경 생성
python3 -m venv 경로
# 또는 
pip3 install virtualenv # 설치 후 
virtualenv 가상환경명 --python=python3.8 # 가상환경 디렉토리가 있길 원하는 디렉토리 내에서 / 버전 지정 가능
# 가상환경 실행
source 경로/bin/activate
# 가상환경 비활성화
deactivate
```

## 주피터 노트북 연결

```sh
# 가상환경 활성화 이후
pip3 install jupyter notebook
python -m ipykernel install --user --name 가상환경이름 --display-name "표시할이름"
```

이후 주피터 노트북에서 커널 연결

## vscode에서 사용하기

command(control)+shift+p 이후 Jupyter: Create New Blank Jupyter Notebook
이후 커널 연결하기
