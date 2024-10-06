from flask import  Flask, render_template, jsonify, request

carros=[
    {
        "id":"1",
        "marca":"mazda",
        "modelo":1983
    },{
        "id":"2",
        "marca":"honda",
        "modelo":193
    }
]

app = Flask(__name__)

@app.route("/")
def homme():
    return render_template("index.html")

@app.route("/carros", methods=["GET"])
def getcarros():
    return jsonify(carros)

@app.route("/carros", methods=["POST"])
def postcarros():
    nuevoCarro = request.json
    carros.append(nuevoCarro)
    return "nuevo carro creado"

@app.route("/carros/<id>", methods=["DELETE"])
def deletecarro (id):
    for car in carros:
        if car["id"] == id:
           carros.remove(car)
        
    return f"carro con id {id} a sido eliminado "
    return "id no econtrado"

@app.route("/carros/<id>", methods=["PUT"])
def putcarro (id):
    nuevocarro = request.json
    for carr in carros:
        if carr["id"] == id:
            ca = carros.index(carr)
            carros[ca] = nuevocarro
            return "carro actualizado"
    return "carro no econtrado"


app.run()