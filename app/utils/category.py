import glob
import os
from .md_parser import get_meta, read_article

class Category():
    def __init__(self, category_name):
        self.category_name = category_name
        self.articles = []
        self.articles_path = []

    def meta_categorize(self, articles):
        for article_path in articles:
            article_category = os.path.basename(os.path.dirname(article_path))
            article_name = os.path.basename(article_path)
            meta = get_meta(read_article(article_path))
            categories = meta["categories"][0].split()
            for n in categories:
                if n == self.category_name:
                    self.articles.append(article_name)
                    self.articles_path.append(article_path)

    def __repr__(self):
        return 'Category name is <{}>'.format(self.category_name)
