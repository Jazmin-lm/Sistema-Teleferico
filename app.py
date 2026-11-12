
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/detencion")
def detencion():
    return render_template("detencion.html")


@app.route("/deterioro")
def deterioro():
    return render_template("deterioro.html")


@app.route("/oscilaciones")
def oscilaciones():
    return render_template("oscilaciones.html")


@app.route("/sensores")
def sensores():
    return render_template("sensores.html")


@app.route("/historial")
def historial():
    return render_template("historial.html")


if __name__ == "__main__":
    app.run(debug=True)
