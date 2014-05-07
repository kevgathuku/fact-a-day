from flask import Flask, render_template
app = Flask(__name__)

from til import factsChecker

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/facts')
def facts(posts=None):
	return render_template('facts.html', posts=factsChecker())

if __name__ == '__main__':
    app.run(debug=True)