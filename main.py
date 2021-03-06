from flask import Flask, send_from_directory
import random
import requests

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('svelte/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('svelte/public', path)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

@app.route("/pokemon/<string:name>", methods=['GET'])
def get_pokemon(name):
    res = requests.get("https://pokeapi.co/api/v2/pokemon/" + name).json()
    return res


if __name__ == "__main__":
    app.run(debug=True)