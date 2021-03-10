from flask import Flask, request, render_template,\
                  redirect, url_for, jsonify
import glob
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

articles_dir = "./resources/"

class Category():
    def __init__(self, category_name):
        self.category_name = category_name
        self.articles = []
    
    def lists(self, articles):
        for art in articles:
            if (os.path.basename(os.path.dirname(art)) == self.category_name):
                self.articles.append(art)
    
    def __repr__(self):
        return 'Category name is <{}>'.format(self.category_name)

@app.route('/')
def hello():
    # categories = glob.glob(articles_dir + "*")
    categories = [os.path.basename(i) for i in glob.glob(articles_dir + "*")]
    # articles = glob.glob(articles_dir + categories[0] + "/*")
    articles = glob.glob(articles_dir + "/*/*")
    print(categories)
    print(articles)
    return render_template("index.html", categories=categories, articles=articles)

@app.route("/data")
def data():
    r = {"name": "a", "article": "b"}
    return jsonify(r)

if __name__ == "__main__":
    app.run()