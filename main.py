from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

tweets = {
    '1': {
        'content': 'hola'
    },
    '2': {
        'content': 'chau'
    },
    '3': {
        'content': 'aprobo?'
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(tweets=tweets)
    if request.method == 'POST':
        return 'Hola2'

if __name__ == "__main__":
    app.run(debug=True)