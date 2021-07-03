import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series

data = pd.read_csv("/pfs/data/housing-train.csv", delimiter=',')
col_drop = set(data.count()[data.count()<0.60*max(data.count())].index.tolist())
pd.Series(list(col_drop)).to_csv('/pfs/out/col_drop.csv', index=False)

data = data.drop((col_drop), axis=1)
corr = data.corr()
r_var = corr.SalePrice[(corr.SalePrice > 0.5)]
r_col = list(r_var.index.values)
new_corr = data[r_col].corr()
plt.subplots(figsize=(20,15))
my_plot2 = sns.heatmap(new_corr, annot=True,cmap='YlGnBu', linecolor='white')
fig = my_plot2.get_figure()
fig.savefig('/pfs/out/heatmap2.png', dpi=400)

new_data = data.loc[:, data.columns.intersection(r_col)]
new_data.to_csv('/pfs/out/cleaned-data.csv', index=True)

