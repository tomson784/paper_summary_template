from flask import Flask, request, render_template,\
                  redirect, url_for, jsonify
import glob
import os
import markdown

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

articles_dir = "./resources/"

class Category():
    def __init__(self, category_name):
        self.category_name = category_name
        self.articles = []
        self.articles_path = []
    
    def lists(self, articles):
        for article_path in articles:
            article_category = os.path.basename(os.path.dirname(article_path))
            article_name = os.path.basename(article_path)
            if (article_category == self.category_name):
                self.articles.append(article_name)
                self.articles_path.append(article_path)
    
    def __repr__(self):
        return 'Category name is <{}>'.format(self.category_name)

@app.route('/')
def home():
    category_names = [os.path.basename(i) for i in glob.glob(articles_dir + "*")]
    categories_class = [Category(category_name) for category_name in category_names]
    # articles = glob.glob(articles_dir + categories[0] + "/*")
    articles = glob.glob(articles_dir + "/*/*")
    for i in range(len(category_names)):
        categories_class[i].lists(articles)
    print(categories_class)
    print(categories_class[0].articles)
    print(categories_class[0].articles_path)
    print(articles)
    return render_template("index.html", categories=categories_class)

@app.route('/<category>/<article>')
def show_article(category, article):
    path = articles_dir + category + "/" + article
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    html = markdown.markdown(text)
    print(html)
    # return render_template("article.html", contents=html)
    return html

# @app.route("/data")
# def data():
#     r = {"name": "a", "article": "b"}
#     return jsonify(r)

if __name__ == "__main__":
    app.run()