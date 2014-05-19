from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from til import factsChecker, sanitizeFacts

@app.route('/')
def facts(posts=None):
	return render_template('facts.html', posts=sanitizeFacts(), title = 'index')

if __name__ == '__main__':
    app.run(debug=True)