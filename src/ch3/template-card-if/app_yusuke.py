from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # テンプレートエンジンにデータを指定
    return render_template(
            'card-age.html',
            username='ユウスケ',
            age=20,
            email='yusuke@example.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

