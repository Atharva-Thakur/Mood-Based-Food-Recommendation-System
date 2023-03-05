import pandas as pd
from wordcloud import STOPWORDS

stopwords = set(STOPWORDS)
from plotly.offline import init_notebook_mode

init_notebook_mode()
import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
stop = set(stopwords)
stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', ''])
from nltk.stem import WordNetLemmatizer

food_data = pd.read_csv('food_choices - food_choices.csv')


def search_comfort(mood):
    lemmatizer = WordNetLemmatizer()
    foodcount = {}
    for i in range(148):
        temp = [temps.strip().replace('.', '').replace(',', '').lower() for temps in
                str(food_data["comfort_food_reasons"][i]).split(' ') if temps.strip() not in stop]
        if mood in temp:
            foodtemp = [lemmatizer.lemmatize(temps.strip().replace('.', '').replace(',', '').lower()) for temps in
                        str(food_data["comfort_food"][i]).split(',') if temps.strip() not in stop]
            for a in foodtemp:
                if a not in foodcount.keys():
                    foodcount[a] = 1
                else:
                    foodcount[a] += 1
    sorted_food = sorted(foodcount, key=foodcount.get, reverse=True)
    return sorted_food


def find_my_comfort_food(mood):
    topn = search_comfort(mood)  # function create dictionary only for particular mood
    print("3 popular comfort foods in %s are:" % (mood))
    print(topn)
    return topn
