from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


stations = pd.read_csv('data-small/stations.txt', skiprows=17)
stations = stations[['STAID', 'STANAME                                 ']]
#connect html pages to the flask object
@app.route('/')
def home():
    return render_template('home.html', data=stations.to_html())


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    main_files = "data-small/TG_STAID" + str(station).zfill(6) + '.txt'
    data = pd.read_csv(main_files, skiprows=20, parse_dates=['    DATE'])
    temperature = data.loc[data['    DATE'] == date]['   TG'].squeeze()/10
    return {
        'station': station,
        'date': date,
        'temperature': temperature

    }


app.run(debug=True)
