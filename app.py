from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('cont.html')

if __name__ == '__main__':
    app.run()