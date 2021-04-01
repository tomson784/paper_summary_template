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

def category_classification(meta):
    pass
