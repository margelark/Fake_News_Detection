"""
"""
from pathlib import Path

import bs4
import requests
import flask
import re
import news


@news.app.route("/")
def show_index():
    return flask.render_template("index.html")

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