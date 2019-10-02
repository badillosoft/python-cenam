from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route("/registrar")
def registrar():
    nombre = request.args.get("nombre", "Anónimo")
    edad = request.args.get("edad", "18")
    genero = request.args.get("genero", "Otro")
    sueldo = request.args.get("sueldo", "0")
    escolaridad = request.args.get("escolaridad", "ND")
    carro = request.args.get("carro", "No")
    equipo = request.args.get("equipo", "ND")

    personas = pd.read_excel("personas.xlsx", sheet_name="Hoja 1")

    personas.loc[len(personas)] = pd.Series({
        "Nombre": nombre,
        "Edad": edad,
        "Genero": genero,
        "Sueldo": sueldo,
        "Escolaridad": escolaridad,
        "Carro": carro,
        "Equipo": equipo,
    })

    personas.to_excel("personas.xlsx", sheet_name="Hoja 1", index=False)

    return redirect("/?alert=Correcto")

from flask import Response
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

@app.route("/plot/edad")
def plot_edad():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    
    # Creamos la gráfica
    personas = pd.read_excel("personas.xlsx", sheet_name="Hoja 1")
    edades = personas["Edad"].map(int)
    axis.hist(edades, bins=20)
    
    output = BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/plot/genero")
def plot_genero():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    
    # Creamos la gráfica
    personas = pd.read_excel("personas.xlsx", sheet_name="Hoja 1")
    total_hombres = personas.query("Genero=='Hombre'").shape[0]
    total_mujeres = personas.query("Genero=='Mujer'").shape[0]
    total_otros = personas.query("Genero=='Otro'").shape[0]
    axis.pie([total_hombres, total_mujeres, total_otros], 
        labels=["Hombres", "Mujeres", "Otros"],
        colors=["cornflowerblue", "hotpink", "gray"])
    axis.axis("equal")
    
    output = BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/plot/sueldo")
def plot_sueldo():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    
    # Creamos la gráfica
    personas = pd.read_excel("personas.xlsx", sheet_name="Hoja 1")
    r1 = personas.query("Sueldo < 5000").shape[0]
    r2 = personas.query("Sueldo >= 5000 and Sueldo < 10000").shape[0]
    r3 = personas.query("Sueldo >= 10000 and Sueldo < 20000").shape[0]
    r4 = personas.query("Sueldo > 20000").shape[0]
    axis.bar(["0-5k", "5k-10k", "10k-20k", "20k+"], [r1, r2, r3, r4])
    axis.axis("equal")
    for tick in axis.get_xticklabels():
        tick.set_rotation(30)
    
    output = BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/")
def home():
    return render_template("index.html")

app.run()