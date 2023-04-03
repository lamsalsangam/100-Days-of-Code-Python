from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def coffee():
    response = requests.get("https://api.example.com/coffee") # Your Api address here
    data = response.json()
    coffee_stores = data["coffee_stores"]
    return render_template("coffee.html", coffee_stores=coffee_stores)


if __name__ == "__main__":
    app.run()
