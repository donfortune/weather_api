from flask import Flask, render_template

app = Flask(__name__)


#connect html pages to the flask object
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def about():
    return render_template('about.html')


app.run(debug=True)
