from flask import current_app as app
from flask import render_template

TITLE = "Flask MySQL Template"

@app.route("/")
@app.route("/index")
def home():
    page_title = TITLE
    return render_template("index.html", title=title)
