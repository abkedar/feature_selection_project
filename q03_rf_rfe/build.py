# Default imports
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier


# Your solution code here
def rf_rfe(df):
    X = data.iloc[:, :-1]
    y = data['SalePrice']
    Rf = RandomForestClassifier()
    rfe = RFE(Rf)
    rfe1 = rfe.fit(X, y)
    top_feat = X.columns[rfe.ranking_ == 1]
    return top_feat.tolist()

print rf_rfe(data)
