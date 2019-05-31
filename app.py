#https://realpython.com/run-python-scripts/

from flask import Flask, make_response, request, render_template
from werkzeug.utils import secure_filename
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import os

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
process_path = os.path.join(dir_path,'process.py')
plot_path = os.path.join(dir_path,'plots.py')


#cache buster function
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/transform', methods=["POST"])
def transform_view():

    #get data file from HTML
    f = request.files['data_file']
    filename = secure_filename(f.filename)
    f.save(filename)

    #get data into Pandas and save to static
    df = pd.read_csv(filename, index_col='Date', parse_dates=True)
    df.to_csv('static/data.csv')

    #run .py files to process & plot data
    os.system(f'py {process_path}')
    time.sleep(2)
    os.system(f'py {plot_path}')

    #read data.csv in Pandas to show in Pandas to HTML
    df2 = pd.read_csv('static/dataProcessed.csv', index_col='Date', parse_dates=True)

    resp = add_header(make_response(render_template('table.html', tables=[df2.to_html(classes='data')], titles=df.columns.values)))
    return resp



if __name__ == '__main__':
    app.run(debug=True)
