from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

if __name__ == "__main__":
    # Ejecutar en todas las interfaces disponibles, en el puerto 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
