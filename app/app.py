from flask import Flask, request, render_template,\
                  redirect, url_for, jsonify
import glob
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

articles_dir = "./resources"

@app.route('/')
def hello():
    # articles =glob.glob(articles_dir)
    articles = os.listdir(path=articles_dir)
    print(articles)
    return render_template("index.html", articles=articles)

@app.route("/data")
def data():
    r = {"name": "a", "article": "b"}
    return jsonify(r)

if __name__ == "__main__":
    app.run()