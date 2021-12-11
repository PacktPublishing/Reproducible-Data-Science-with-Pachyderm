from textblob import TextBlob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from contextlib import redirect_stdout

data = pd.read_csv('/pfs/data-clean/cleaned-data.csv', delimiter=',')

data = data[['text']]
data["polarity_score"] = data["text"].apply(lambda data: TextBlob(data).sentiment.polarity)
data['sentiment'] = data['polarity_score'].apply(lambda x: 'Positive' if x >= 0.1 else ('Negative' if x <= -0.1 else 'Neutral'))
print(data.head(10))
data.to_csv('/pfs/out/polarity.csv', index=True)

positive = [ data for index, t in enumerate(data['text']) if data['polarity_score'][index] > 0]
neutral = [ data for index, tweet in enumerate(data['text']) if data['polarity_score'][index] == 0]
negative = [ data for index, t in enumerate(data['text']) if data['polarity_score'][index] < 0]

with open('/pfs/out/number_of_tweets.txt', 'w') as file:
      with redirect_stdout(file):
          print("Number of Positive tweets:", len(positive))
          print("Number of Neutral tweets:", len(neutral))
          print("Number of Negative tweets:", len(negative))

colors = ['#9b5de5','#f15bb5','#fee440']
figure = pd.DataFrame({'percentage': [len(positive), len(negative), len(neutral)]},
                      index=['Positive', 'Negative', 'Neutral'])
plot = figure.plot.pie(y='percentage', figsize=(5, 5), autopct='%1.1f%%', colors=colors)

circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(circle)
plot.axis('equal')
plt.tight_layout()
plot.figure.savefig("/pfs/out/plot.png")
