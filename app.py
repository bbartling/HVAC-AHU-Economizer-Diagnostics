from flask import Flask, make_response, request, render_template
from werkzeug.utils import secure_filename
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import os

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
econProcess_path = os.path.join(dir_path,'econProcess.py')
econPlots_path = os.path.join(dir_path,'econPlots.py')
removeFiles_path = os.path.join(dir_path,'removeFiles.py')


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

@app.route('/econ', methods=["POST"])
def econ_process():
    #get data file from HTML
    f = request.files['data_file']
    filename = secure_filename(f.filename)
    f.save(filename)
    #get data into Pandas and save to static
    df = pd.read_csv(filename, index_col='Date', parse_dates=True)
    df.to_csv('static/econRawData.csv')
    #run .py files to process, plot data, and remove uploaded files
    os.system(f'py {econProcess_path}')
    os.system(f'py {econPlots_path}')
    os.system(f'py {removeFiles_path}')
    #read data.csv in Pandas to show in Pandas to HTML
    df2 = pd.read_csv('static/econDataProcessed.csv', index_col='Date', parse_dates=True)
    resp = add_header(make_response(render_template('table.html', tables=[df2.to_html(classes='data')], titles=df.columns.values)))
    return resp



if __name__ == '__main__':
    app.run(debug=True)

