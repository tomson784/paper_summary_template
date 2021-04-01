import markdown

def markdown2html(path):
    # path = articles_dir + category + "/" + article + ".md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    md = markdown.Markdown(extensions = ['meta'])
    html = md.convert(text)
    return html, md.Meta

def read_article(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def get_meta(article):
    md = markdown.Markdown(extensions = ['meta'])
    md.convert(article)
    return md.Meta

def set_categories(paths):
    category_names = []
    for path in paths:
        article = read_article(path)
        meta = get_meta(article)
        print(meta["categories"])
        categories = meta["categories"][0].split()
        for category in categories:
            category_names.append(category)
    return set(category_names)

def category_classification(meta):
    pass
