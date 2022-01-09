from flask import Flask, flash, jsonify, redirect, render_template, request, session


import os

import random

import base64
from io import BytesIO

from pathlib import Path
from shutil import rmtree

class Person(object):
    img: ""
    height: ""
    weight: ""


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    
    score = 0
    round = 1

    if request.method == "POST":
        score = int(request.form['score'])
        round += int(request.form['round'])

    person = getPerson()
    return render_template("game.html", height=person.height, weight=person.weight, img=person.img, score=score, round=round)


def getPerson():
    id = random.randint(0,600)
    f = open("data/meta/" + str(id) + ".txt", "r").read().split(",")
    height = f[0]
    weight = f[1]
    img = "data:image/jpg;base64, "
    f = open("data/img/" + str(id) + ".jpg", "rb")
    img += str(base64.b64encode(f.read()).decode('utf-8'))

    person = Person()
    person.height = height
    person.weight = weight
    person.img = img

    return person


if __name__ == '__main__':
    app.run()