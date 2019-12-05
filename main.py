import random
import string
from datetime import datetime

from flask import Flask
from flask import jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

tweets = {}

def generate_key():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))


@api.resource('/')
class TweetResource(Resource):

    def get(self):
        return jsonify(tweets=tweets)
    
    def post(self):
        key = generate_key()
        content = request.json['content']
        tweets[key] = dict(
            content=content,
            created_at=str(datetime.now())
        )
        return jsonify(status='Success', id=key, tweet=tweets[key])


@api.resource('/<string:tweet_id>')
class TweetIdResource(Resource):

    def delete(self, tweet_id):
        del tweets[tweet_id]
        return jsonify(status='Success', id=tweet_id)

    def get(self, tweet_id):
        return tweets[str(tweet_id)]


if __name__ == "__main__":
    app.run(debug=True)
