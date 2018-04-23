from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Congrats!\n<img src=http://cultofthepartyparrot.com/parrots/hd/partyparrot.gif >'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
