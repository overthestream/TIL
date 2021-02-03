import seaborn as sns
import glob
import os
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing, svm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_validate, TimeSeriesSplit, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, mean_squared_error, r2_score, accuracy_score, confusion_matrix, precision_score, recall_score, roc_auc_score
from xgboost import XGBClassifier, plot_importance
import warnings
warnings.filterwarnings('ignore')
sns.set()

dataFrame = pd.read_csv(
    'MachineLearning/퀀트전략을위한_인공지능트레이딩/Chapter6/ETFs_main.csv')


def getMA(dataFrame, n):
    MA = pd.Series(dataFrame['CLOSE_SPY'].rolling(
        n, min_periods=n).mean(), name='MA_'+str(n))
    dataFrame = dataFrame.join(MA)
    return dataFrame


def getVMA(dataFrame, n):
    VMA = pd.Series(dataFrame['VOLUME'].rolling(
        n, min_periods=n).mean(), name='VMA_'+str(n))
    dataFrame = dataFrame.join(VMA)
    return dataFrame


def getRSI(dataFrame, n):
    i = 0
    UpI = [0]
    DoI = [0]
    while i+1 <= dataFrame.index[-1]:
        UpMove = dataFrame.loc[i+1, 'HIGH']-dataFrame.loc[i, 'HIGH']
        DoMove = dataFrame.loc[i, 'LOW']-dataFrame.loc[i+1, 'LOW']

        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)

        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)

        i = i+1
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(UpI.ewm(span=n, min_periods=n).mean())
    NegDI = pd.Series(DoI.ewm(span=n, min_periods=n).mean())
    RSI = pd.Series(PosDI / (PosDI + NegDI), name='RSI_' + str(n))
    dataFrame = dataFrame.join(RSI)
    return dataFrame


def getConfusionMatrix(y_test, pred):
    confusion = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    roc_score = roc_auc_score(y_test, pred)
    print('confusion matrix')
    print('accuracy{0:.4f},precision:{1:.4f},recall:{2:.4f},F1:{3:.4f},ROC AUC:{4:.4f}'.format(
        accuracy, precision, recall, f1, roc_score))


dataFrame = getMA(dataFrame, 45)
dataFrame = getVMA(dataFrame, 45)
dataFrame = getRSI(dataFrame, 14)

dataFrame = dataFrame.set_index('Dates')
dataFrame = dataFrame.dropna()

dataFrame['target'] = dataFrame['CLOSE_SPY'].pct_change()
dataFrame['target'] = np.where(dataFrame['target'] > 0, 1, -1)

dataFrame['target'] = dataFrame['target'].shift(-1)
dataFrame = dataFrame.dropna()

dataFrame['target'] = dataFrame['target'].astype(np.int64)
y_var = dataFrame['target']
x_var = dataFrame.drop(
    ['target', 'OPEN', 'HIGH', 'LOW', 'VOLUME', 'CLOSE_SPY'], axis=1)

up = dataFrame[dataFrame['target'] == 1].target.count()
total = dataFrame.target.count()

x_train, x_test, y_train, y_test = train_test_split(
    x_var, y_var, test_size=0.3, shuffle=False, random_state=3)

train_count = y_train.count()
test_count = y_test.count()

xgb_dis = XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=3)
xgb_dis.fit(x_train, y_train)
xgb_pred = xgb_dis.predict(x_test)
print(xgb_dis.score(x_train, y_train))
getConfusionMatrix(y_test, xgb_pred)

n_estimators = range(10, 200, 10)

params = {
    'bootstrap': [True],
    'n_estimators': n_estimators,
    'max_depth': [4, 6, 8, 10, 12],
    'min_samples_leaf': [2, 3, 4, 5],
    'min_samples_split': [2, 4, 6, 8, 10],
    'max_features': [4]
}
my_cv = TimeSeriesSplit(n_splits=5).split(x_train)
clf = GridSearchCV(RandomForestClassifier(), params, cv=my_cv, n_jobs=-1)
clf.fit(x_train, y_train)

pred_con = clf.predict(x_test)
accuracy_con = accuracy_score(y_test, pred_con)
getConfusionMatrix(y_test, pred_con)
