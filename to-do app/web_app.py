from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    with open("tasks.txt","r") as file:
        tasks= file.read().splitlines()
    
    html ="<h1>My tasks</h1><ol>"

    for i in tasks:
        html+= f"<li>{i}</li>"
    html += "</ol>"
    return html

app.run(debug=True)