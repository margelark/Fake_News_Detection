"""
"""
from pathlib import Path

import bs4
import requests
import flask
import re
import news
from tensorflow import keras
import tensorflow as tf
import numpy as np
import h5py


@news.app.route("/")
def show_index():
    return flask.render_template("index.html")



@news.app.route("/evaluation", methods=["POST"])
def show_evaluation():

    #json_file = open('news/views/shrink_model.json', 'r')
    #loaded_model_json = json_file.read()
    #json_file.close()
    #loaded_model = tf.keras.models.model_from_json(loaded_model_json)
    #loaded_model.load_weights("news/views/shrink_model.weights.h5")
    print(tf.__version__)
    #model = tf.keras.models.load_model("news/views/shrink_model.keras")
    #print(model.summary())
    snippet = flask.request.form["snippet"]
    # numeric_labels = {'pants-fire':0, 'false':1, 'barely-true':2, 'half-true':3, 'mostly-true':4, 'true':5}
    #prediction = model.predict(snippet)
    

    context = {"prediction": "prediction"}

    return flask.render_template("evaluation.html", **context)


@news.app.route("/result", methods=["POST"])
def show_result():
    link = flask.request.form["link"]
    try:
        result = requests.get(link)
        content = result.text
    
        soup = bs4.BeautifulSoup(content,'html.parser')
        text = soup.text
        text =  text = re.sub(r"[^a-zA-Z0-9 ]+", "", text).casefold().split()
        print(text)
        return flask.render_template("result.html")
    except Exception as e:
        return flask.redirect(flask.url_for("show_index"))