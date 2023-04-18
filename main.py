from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

data = pd.read_csv('/data-small/*')
print(data)
#connect html pages to the flask object
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    temperature = 23
    return {
        'station': station,
        'date': date,
        'temperature': temperature

    }


app.run(debug=True)
