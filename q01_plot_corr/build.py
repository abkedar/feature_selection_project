# Default imports
import pandas as pd
from matplotlib.pyplot import yticks, xticks, subplots, set_cmap
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your solution here:
def plot_corr(df, size=11):
    df1=data.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(size, size))
    sns.heatmap(df.corr(), cmap= 'YlOrRd')

    #xticks(range(len(df1)), df1.columns)
    #yticks(range(df1.shape[0]), df1.columns)
    return plt.show()
#print plot_corr(df=data, size=11)
