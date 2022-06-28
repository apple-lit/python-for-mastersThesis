# %%
import datetime as dt
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# def plt_edr(ymd):
#     df = pd.read_csv('../python_data/csv2/' + str(ymd) + '.csv', delimiter=',', encoding="shift_jis")
#     # 先頭行を削除
#     df = df.drop(df.index[0])

df = pd.read_csv('../../研究/python_data/csv2/20170910.csv',
                 delimiter=',', encoding="shift_jis")
# 先頭行を削除
df = df.drop(df.index[0])
df = df.astype(float)

df['Time'] = df['Time'].replace(' ', '', regex=True)
df['Time'] = pd.to_datetime(df['Time'], format="%H:%M:%S")
df = df.fillna(0)

fig = plt.figure(dpi=300)
ax = fig.add_subplot()

data_X = df['Time']
data_Y = df['WINDSPEED']
df = df.fillna(0)

# plt.xlabel(df['Time'])
new_xticks = date2num(
    [df['Time'].iloc[0] + dt.timedelta(minutes=60*x) for x in range(len(df)//1800)])
ax.xaxis.set_major_locator(ticker.FixedLocator(new_xticks))
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
ax.tick_params(axis='x', rotation=30)
plt.ylabel(df['WINDSPEED'])

plt.plot(data_Y, linestyle="solid", color="red", label="WINDSPEED")
plt.show()


# print(df)
