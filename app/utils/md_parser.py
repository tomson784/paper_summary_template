import markdown

def text2markdown(path):
    # path = articles_dir + category + "/" + article + ".md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    md = markdown.Markdown(extensions = ['meta'])
    html = md.convert(text)
    return html, md.Meta
