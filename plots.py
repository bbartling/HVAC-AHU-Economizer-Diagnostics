import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time




df = pd.read_csv('static/dataProcessed.csv', index_col='Date', parse_dates=True)

OAT = pd.Series(df['OAT'])
RAT = pd.Series(df['RAT'])
MAT = pd.Series(df['MAT'])
df_OATrat = (OAT - RAT)
df_MATrat = (MAT - RAT)
plt.scatter(df_OATrat,df_MATrat, color='grey', marker='+')
plt.xlabel('OAT-RAT')
plt.ylabel('MAT-RAT')
plt.title('Economizer Diagnostics')
plt.plot([0,-18],[0,-18], color='green', label='100% OSA during ideal conditions')
plt.plot([0,20],[0,5], color='red', label='Minimum OSA in cooling mode')
plt.plot([0,-38],[0,-9.5], color='blue', label='Minimum OSA in heating mode')
plt.plot([0,0],[-20,10], color='black')
plt.plot([-30,20],[0,0], color='black')
plt.legend()
plt.text(-3, -28, time.ctime(), fontsize=9)

plt.savefig('static/plot.png')












