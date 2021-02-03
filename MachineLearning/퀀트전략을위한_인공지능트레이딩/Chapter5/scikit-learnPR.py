import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

boston_data = load_boston()
x_values = boston_data['data']
y_values = boston_data['target']

model = LinearRegression()
model.fit(x_values, y_values)

sample_house = [[2.2969000e-01, 0.00000000e+00,
                 1.05900000e+01, 0.00000000e+00, 4.89000000e-01, 6.32600000e+00, 5.25000000e+01, 4.35490000e+00, 4.00000000e+00, 2.77000000e+02, 1.86000000e+01, 3.9487000e+02, 1.09700000e+01]]

print(model.predict(sample_house))
