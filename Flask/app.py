from flask import Flask, abort, render_template, redirect, url_for


app = Flask(__name__)

list_food = [
    {
        "tittle": "з малиною",
        "color": "Червоний",
        "description": "Смачний пиріг з малиною",
    },
    {
        "tittle": "з персиком",
        "color": "Жовтий",
        "description": "Смачний пиріг з персиком",
    },
]


@app.route("/")
def home():
    return render_template("home.html", my_variables=list_food)


@app.route("/index")
def index():
    return render_template("index.html", my_variables=list_food)


@app.route("/get_food/<int:id>")
def get_food(id: int):
    if id >= len(list_food):
        return redirect(url_for(index.__name__))
    return render_template("foo.html", foo=list_food[id])


@app.route("/foo/<int:id>/edit")
def edit_food(id: int):
    if id >= len(list_food):
        abort(404)
    return render_template("foo_edit.html", foo=list_food[id])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404