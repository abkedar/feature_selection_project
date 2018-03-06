# Default imports

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_regression


# Write your solution here:
def percentile_k_features(df, k=20):
    X=df.iloc[:,:-1]
    y=df['SalePrice']
    fs = SelectPercentile(f_regression, percentile=k)
    fs1 = fs.fit_transform(X, y)
    k1 = list(fs.scores_)
    best_kindex = sorted(range(len(k1)), key=lambda i : k1[i], reverse=True)[:fs1.shape[1]]
    best_k = [X.columns[i] for i in best_kindex]
    return best_k
print percentile_k_features(data, k=20)
