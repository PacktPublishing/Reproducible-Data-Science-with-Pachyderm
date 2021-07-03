from sklearn.model_selection import GridSearchCV
import joblib
import pickle
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_squared_error, make_scorer
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from contextlib import redirect_stdout
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("/pfs/remove-outliers/removed-outliers-data.csv", delimiter=',')
X=data.drop('SalePrice', axis=1)
y=data['SalePrice']
train_X, test_X, train_y, test_y = train_test_split(X,y,test_size=0.4, random_state=0)

estimator = Ridge(alpha=10)
scoring={'R_squared':'r2','MSE':'neg_mean_squared_error'}
params = {'alpha':[1,0.1,0.01,0.001,0.0001,0,10,100,1000]}

with open('/pfs/out/best_score.txt', 'w', encoding='utf-8') as f:
      with redirect_stdout(f):
          for i, v in scoring.items():
             grid = GridSearchCV(estimator, params, cv=10, scoring="r2", return_train_score=True)
             grid.fit(train_X, train_y)
             print(i)
             print('Best params:', grid.best_params_)
             if grid.best_score_ > 0:
                 print('Best score:', grid.best_score_)
             else:
                 print('Best score:', np.sqrt(abs(grid.best_score_)))
             print()

joblib.dump(estimator, '/pfs/out/my_model.pkl', compress =1)

alphas=[1,0.1,0.01,0.001,0.0001,0,10,100,1000]

plt.plot(alphas, grid.cv_results_['mean_train_score'], label='Train', marker='o', color='Green', linestyle='dashed')
plt.plot(alphas, grid.cv_results_['mean_test_score'], label='Test', marker='x', color='Orange', linestyle='solid')
plt.ylabel('R-squared')
plt.xlabel('alpha')
plt.legend()
plt.savefig('/pfs/out/performance-plot.png', dpi=400)
