import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
weeks = []
sne = []
nvda = []
dis = []
msft = []
aapl = []

with open("WeeklyStocksLow.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        weeks.append(row[0])
        sne.append(int(row[1]))
        nvda.append(int(row[2]))
        dis.append(int(row[3]))
        msft.append(int(row[4]))
        aapl.append(int(row[5]))

plt.plot(weeks, sne, color='#0074FF', marker='o', linestyle='solid', label='Sony (SNE)')
plt.plot(weeks, nvda, color='#12C100', marker='o', linestyle='solid', label='Nvidia (NVDA)')
plt.plot(weeks, dis, color='#00FFF7', marker='o', linestyle='solid', label='Disney (DIS)')
plt.plot(weeks, msft, color='#CE0404', marker='o', linestyle='solid', label='Microsoft (MSFT)')
plt.plot(weeks, aapl, color='#9700FF', marker='o', linestyle='solid', label='Apple (AAPL)')
plt.legend(loc='best')
plt.ylabel("Weekly Stock Price Low")
plt.xlabel("Week Of")
plt.xticks(rotation=45, ha="right")
plt.show()
