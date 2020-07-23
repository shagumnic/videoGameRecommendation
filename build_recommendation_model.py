import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import re

data_df = pd.read_csv('dataForRecommendation.csv')

data_df = data_df[['name', 'genres', 'tags', 'developers', 'description']]

data_df['genres'] = data_df['genres'].map(lambda x: x[1:len(x)-1].lower().replace("'", "").split(', '))

data_df['tags'] = data_df['tags'].map(lambda x: x[1:len(x)-1].lower().replace("'", "").split(', '))

data_df['name_features'] = data_df['name'].map(lambda x: str(x).lower())

data_df['developers'] = data_df['developers'].map(lambda x: x[1:len(x)-1].replace("'", "").split(', '))

regex = re.compile(r'[\n\r\t\xa0]')

data_df['description'] = data_df['description'].map(lambda x: regex.sub(" ", x)[16:])

data_df.set_index('name', inplace=True)

data_df['Key_words'] = ""

for index, row in data_df.iterrows():
    description = row['description']

    # instantiating Rake, by default is uses english stopwords from NLTK
    # and discard all puntuation characters
    r = Rake()

    # extracting the words by passing the text
    r.extract_keywords_from_text(description)

    # getting the dictionary with key words and their scores
    key_words_dict_scores = r.get_word_degrees()

    # assigning the key words to the new column
    row['Key_words'] = list(key_words_dict_scores.keys())

print(data_df['Key_words'])
data_df.drop(columns=['description'], inplace=True)

data_df['bags_of_words'] = ''

for index, row in data_df.iterrows():
    row['developers'] = [x.lower().replace(' ', '') for x in row['developers']]

columns = data_df.columns
for index, row in data_df.iterrows():
    words = ''
    for col in columns:
        if col != 'name_features':
            words = words + ' '.join(row[col]) + ' '
        else:
            words = words + row[col] + ' '
    row['bags_of_words'] = words

data_df.drop(columns=[col for col in data_df.columns if col != 'bags_of_words'], inplace=True)

count = CountVectorizer()
count_matrix = count.fit_transform(data_df['bags_of_words'])

indices = pd.Series(data_df.index)

cosine_sim = cosine_similarity(count_matrix, count_matrix)


def recommendation(name, cosine_sim, indices):

    recommendation_games = []

    idx = indices[indices == name].index[0]

    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)

    top_10_indices = list(score_series.iloc[1:11].index)

    for i in top_10_indices:
        recommendation_games.append(list(data_df.index)[i])
    return recommendation_games


indices.to_csv('recommend_indices.csv', index=False)

np.save('recommend_cosine', cosine_sim)
