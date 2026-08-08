from flask import Flask

app = Flask(__name__)

@app.route("/")
def gabigol():
    return "double biceps"

@app.route("/about")
def about():
    return "pagina sobre"

if __name__ == "__main__":
    app.run(debug=True)
