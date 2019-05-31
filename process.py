import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time


df = pd.read_csv('static/data.csv',index_col='Date')




noFanData = set(['OAT', 'MAT', 'RAT'])
fanData = set(['SFS'])
staticData = set(['DUCTP'])


#make plot of data with no fan status
if noFanData.issubset(df.columns):
    if df.empty:
        df = df.fillna(method = 'ffill').fillna(method = 'bfill')
        
    if df.isnull().values.any():
        df = df.fillna(method = 'ffill').fillna(method = 'bfill')

    #save processed data
    df.to_csv('static/dataProcessed.csv')




#make plot of data with fan status
if fanData.issubset(df.columns):
    if df.empty:
        df = df.fillna(method = 'ffill').fillna(method = 'bfill')

    if df.isnull().values.any():
        df = df.fillna(method = 'ffill').fillna(method = 'bfill')

    #save processed data   
    df = df[df['SFS'] == 'On']

    df.to_csv('static/dataProcessed.csv')
        







