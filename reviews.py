import pandas as pd

reviews = pd.read_csv('data/winemag-data-130k-v2.csv', index_col=0)

dict = {'variety': 'count', 'points': 'mean'}

new = reviews.groupby('country').aggregate(dict).sort_values(by='variety', ascending=False)

new = pd.DataFrame(new).rename(columns={'variety': 'count'})

new['points'] = new['points'].round(1)

print(new)

new.to_csv('data/reviews-per-country.csv')

#counts = reviews[['country', 'points']].value_counts()

#counts_reviews = counts.to_frame().reset_index()
#counts_reviews.columns = ['country', 'count', 'points']
#average_points = reviews[['points']].mean(axis=1)

#print(counts_reviews, average_points)


