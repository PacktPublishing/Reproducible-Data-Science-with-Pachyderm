import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("/pfs/data-clean/cleaned-data.csv", delimiter=',', encoding='utf-8')
my_plot=sns.boxplot(x=data['SalePrice'])
fig = my_plot.get_figure()
fig.savefig('/pfs/out/histogram.png', dpi=400)

q1 = data['SalePrice'].quantile(0.25)
q3 = data['SalePrice'].quantile(0.75)
iqr = q3-q1
lw = q1 - 1.5*iqr
uw = q3 + 1.5*iqr
dataset = data[(data['SalePrice']>lw)&(data['SalePrice']<uw)]
plt.figure(figsize=(20,10))
my_plot2 = sns.histplot(data=dataset, x="SalePrice", color="orange", element="poly")
fig = my_plot2.get_figure()
fig.savefig('/pfs/out/histogram-outliers.png', dpi=400)
dataset.to_csv('/pfs/out/removed-outliers-data.csv', index=True)

