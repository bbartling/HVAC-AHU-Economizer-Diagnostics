import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('C:\\Economizer Diagnostics\\AHU4 data CSV.csv', index_col='Date', parse_dates=True)
#print(df)

OAT = pd.Series(df[df.columns[0]])
RAT = pd.Series(df[df.columns[1]])
MAT = pd.Series(df[df.columns[2]])

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

plt.show()











