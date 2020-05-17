from flask import Flask, jsonify, request, render_template
#from flask_restful import Api, Resource
from bot import chat

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    reply = chat(userText)
    return str(reply)


if __name__=="__main__":
    app.run(debug=True)
