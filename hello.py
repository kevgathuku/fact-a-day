from flask import Flask, render_template
app = Flask(__name__)

from til import factsChecker, sanitizeFacts

@app.route('/')
def facts(posts=None):
	return render_template('facts.html', posts=sanitizeFacts())

if __name__ == '__main__':
    app.run(debug=True)