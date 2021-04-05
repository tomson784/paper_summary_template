from flask import Flask, request, render_template,\
                  redirect, url_for, jsonify

import glob
import os

from utils.category import Category
from utils.md_parser import markdown2html, set_categories

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

articles_dir = "../_posts/"

@app.route('/')
def home():
    articles_paths = glob.glob(articles_dir + "/*.md")
    category_names = set_categories(articles_paths)
    categories_class = [Category(category_name) for category_name in category_names]
    for i in range(len(category_names)):
        categories_class[i].meta_categorize(articles_paths)
    return render_template("index.html", categories=categories_class)

@app.route('/<category>/<article>.html')
def show_article(category, article):
    path = articles_dir + "/" + article + ".md"
    html_, meta = markdown2html(path)
    editor = meta["editor"]
    html = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>論文</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    </head>
    <body>
    """
    html += "<h2>" + "編集者 : " + editor[0] + "</h2>"
    html += html_
    html += """
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    </body>
    </html>
    """
    # return render_template("article.html", contents=html)
    return html


if __name__ == "__main__":
    app.run()