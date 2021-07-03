from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, make_scorer
from sklearn.linear_model import Ridge
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from contextlib import redirect_stdout

data = pd.read_csv("/pfs/remove-outliers/removed-outliers-data.csv", delimiter=',')
X=data.drop('SalePrice', axis=1)
y=data['SalePrice']
train_X, test_X, train_y, test_y = train_test_split(X,y,test_size=0.4, random_state=0)

estimator = Ridge(alpha=1).fit(train_X, train_y)
prediction = estimator.predict(test_X)
with open('/pfs/out/r_squared_mse.txt', 'w', encoding='utf-8') as f:
     with redirect_stdout(f):
         print('R-squared:', metrics.r2_score(test_y, prediction))
         print('MSE:', np.sqrt(metrics.mean_squared_error(test_y, prediction)))

plt.figure(figsize=(20,10))
myplot1 = sns.distplot(test_y, hist=True, kde=False)
myplot2 = sns.distplot(prediction, hist=True, kde=False)
plt.legend(labels=['Real Price', 'Predicted Price'])
plt.xlim(0,)
fig1 = myplot1.get_figure()
fig1.savefig('/pfs/out/prediction.png', dpi=400)
