from flask import Flask
from flask import render_template, request

app = Flask(__name__)
@app.route('/')
@app.route('/hello')
def hello_world():
    user = request.args.get('user', 'Shalabh')
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run()