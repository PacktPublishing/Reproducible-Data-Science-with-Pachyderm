import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.subplots(figsize=(20,15))
data = pd.read_csv("/pfs/data/housing-train.csv", delimiter=',')
dataset = data.corr().round(2)

plt.subplots(figsize=(20,15))
my_plot = sns.heatmap(dataset, annot=True,cmap='YlGnBu', linecolor='white')
fig = my_plot.get_figure()
fig.savefig('/pfs/out/heatmap.png', dpi=400)

data_types = data.dtypes.to_frame('dtypes').reset_index()
data_types.to_csv('/pfs/out/data-types.csv', index=False)

cols_no_data = data.isnull().sum() / data.shape[0] * 100.00
no_data = pd.DataFrame({'Column': data.columns, 'Percentage Missing': cols_no_data})
no_data.sort_values(by=['Percentage Missing'], inplace=True, ascending=False)
header = ["Column", "Percentage Missing"]
no_data.to_csv('/pfs/out/no-data.csv', columns = header, index=False)

