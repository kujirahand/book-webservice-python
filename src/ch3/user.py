from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return "test" 

@app.route('/users/<user_id>')
def users(user_id):
    return "ユーザー {0} のページ".format(user_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

