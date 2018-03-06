# Default imports
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

data = pd.read_csv('data/house_prices_multivariate.csv')


# Your solution code here
def select_from_model(df):

    X = df.iloc[:, :-1]
    y = df['SalePrice']
    model = RandomForestClassifier()
    model.fit(X, y)
    b = SelectFromModel(model, prefit = True)

    eleminate_k =X.columns[b.get_support() == True]
    return eleminate_k.tolist()


print select_from_model(data)
