from flask import Flask, render_template, request, redirect, url_for, flash
from models import *
import datetime
today = datetime.date.today()

app = Flask(__name__,
            static_folder='static',
            static_url_path='/static')

app.secret_key = "mykey"


@app.route('/')
def calc():
    """
    Realiza el render del home
    """
    return render_template("home.html", today=today)


@app.route('/contact', strict_slashes=False)
def error():
    """
    Realiza el render de la informacion de los contactos
    """
    return render_template("contact.html")


@app.route("/information", strict_slashes=False)
def info():
    return render_template("information.html")


@app.route('/cloud', methods=["POST"])
def values():
    """
    Renderiza la apertura de la seccion de condiciones de cielo
    """
    if request.method == "POST":
        results = Data_TES(request)
    return render_template("cloud.html", results=results)


@app.route("/recommend", methods=["POST"])
def cont():
    """
    Renderiza la pagina de recomendaciones
    """
    if request.method == "POST":
        results = Data_TES(request)
        results.get_final_data()
    return render_template("results.html", results=results)


if __name__ == '__main__':
    app.run(debug=True)
