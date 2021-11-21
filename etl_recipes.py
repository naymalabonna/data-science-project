import json
import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

def json_to_list(filename): # reads json file into list
    with open(filename) as jsondata:    
        data = json.load(jsondata)
    id  = [] # initializing empty list for id number 
    cuisine = [] # initializing empty list for cuisine 
    ingredients = [] # initializing empty list for ingredient list
    if 'cuisine' in data[0].keys(): # appending the empty lists with data from their keys 
        for i in range(len(data)): # for train.json where all 3 keys are available 
            id.append(data[i]['id']) 
            cuisine.append(data[i]['cuisine'])
            ingredients.append(data[i]['ingredients'])
    else:
        for i in range(len(data)): # for test.json where cuisine is unavailable 
            id.append(data[i]['id'])
            ingredients.append(data[i]['ingredients'])    
    return id, cuisine, ingredients

def lowercase(ingredient): # making the data uniform by making all letters lowercase for the ingredients
    return [[x.lower() for x in y] for y in ingredient]

def remove_digits(ingredient): # removes any numbers from ingredients list
   return [[re.sub("\d+","", x) for x in y] for y in ingredient]

def remove_special_characters(ingredient): # removes any special characters from ingredients list
    ingredient = [[x.replace("-", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace("&", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace("'", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace("''", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace("%", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace("!", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace("(", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace(")", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace("/", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace("?", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace(",", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace(".", " ") for x in y] for y in ingredient] 
    ingredient = [[x.replace(u"\u2122", " ") for x in y] for y in ingredient] # trademark sign
    ingredient = [[x.replace(u"\u00AE", " ") for x in y] for y in ingredient] # registered sign
    ingredient = [[x.replace(u"\u2019", " ") for x in y] for y in ingredient] # right single quotation mark
    return ingredient

def remove_whitespaces(ingredient): # removes extra whitespaces
    return [[re.sub('\s+',' ', x).strip() for x in y] for y in ingredient]

def remove_letters(ingredient): # removes units and other letters from ingredients 
    letters = ['g', 'lb', 's', 'n']   
    def check(string): 
        s = string.split()
        remove  = [word for word in s if word.lower() not in letters]
        return ' '.join(remove)
    return [[check(x) for x in y] for y in ingredient]

def lemmatization(ingredient): # applying lemmatization to ingredients list
    lemma = WordNetLemmatizer()
    def words(string):
        return " ".join(["".join(lemma.lemmatize(w)) for w in string.split()])
    return [[words(x) for x in y] for y in ingredient]

train_ids, train_cuisines, train_ingredients = json_to_list('train.json') # cleaning training data
train_ingredients = lowercase(train_ingredients)
train_ingredients = remove_digits(train_ingredients)
train_ingredients = remove_special_characters(train_ingredients)
train_ingredients = remove_whitespaces(train_ingredients)
train_ingredients = remove_letters(train_ingredients)
train_ingredients = lemmatization(train_ingredients)

test_ids, test_cuisines, test_ingredients = json_to_list('test.json') # cleaning test data
test_ingredients = lowercase(test_ingredients)
test_ingredients = remove_digits(test_ingredients)
test_ingredients = remove_special_characters(test_ingredients)
test_ingredients = remove_whitespaces(test_ingredients)
test_ingredients = remove_letters(test_ingredients)
test_ingredients = lemmatization(test_ingredients)


for ingredient in train_ingredients: # list of train ingredients for each recipe after cleaning
    print(ingredient)
    
for ingredient in test_ingredients: # list of test ingredients for each recipe after cleaning
    print (ingredient)
