from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # テンプレートエンジンにデータを指定
    return render_template(
            'card-age.html',
            username='ケイジ',
            age=19,
            email='keiji@example.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

