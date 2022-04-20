from cmath import pi
import json
from flask import Flask, request, render_template
import string
import pickle
import numpy as np

app = Flask(__name__)

def remove_stop_words(comment):
    eng_stops = pickle.load(open('./pickles/eng_stops.pkl', 'rb'))
    new_comment = []
    for word in comment.split():
        if word not in eng_stops:
            new_comment.append(word)
        
    return " ".join(new_comment)

def stem_and_lem(comment):
    stemmer = pickle.load(open('./pickles/stemmer.pkl', 'rb'))
    lemmatiser = pickle.load(open('./pickles/lemmatiser.pkl', 'rb'))
    new_comment = []
    for word in comment.split():
        new_comment.append(stemmer.stem(lemmatiser.lemmatize(word, pos='v')))
    return " ".join(new_comment)

def vectorize(comment):
    hasher = pickle.load(open('./pickles/hash_vect.pkl', 'rb'))
    return hasher.transform(comment)

def get_pred(comment):
    best_sgd = pickle.load(open('./pickles/trained_sgd.pkl', 'rb'))
    return best_sgd.predict(comment)


@app.route('/')
def my_form():
    return render_template('my-form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form.to_dict()
        print(form_data['InputVal'])

        data = remove_stop_words(form_data['InputVal'])
        data = data.translate(str.maketrans('', '', string.punctuation + "1234567890")).lower()
        data = stem_and_lem(data)
        data = vectorize([data])

        prediction = get_pred(data)

        # 1 is a toxic
        # 0 is non-toxic
        form_data['result'] = prediction;
        return render_template('data.html', form_data= form_data)