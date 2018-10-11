import matplotlib.pyplot as plt
import numpy as np
import csv

AAP_high = []
MSFT_high = []
DKS_high = []
timestamp = []
F_high = []
AMZN_high = []

with open("monthly_AAP.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        timestamp.append(row[0])
        AAP_high.append(int(row[2]))

plt.bar(timestamp, AAP_high)
plt.xticks(rotation=90)
plt.show()

with open("monthly_DKS.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        timestamp.append(row[0])
        DKS_high.append(int(row[2]))

plt.bar(timestamp, DKS_high)
plt.xticks(rotation=90)
plt.show()

with open("monthly_MSFT.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        timestamp.append(row[0])
        MSFT_high.append(int(row[2]))

plt.bar(timestamp, MSFT_high)
plt.xticks(rotation=90)
plt.show()

with open("monthly_F.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        timestamp.append(row[0])
        F_high.append(int(row[2]))

plt.bar(timestamp, F_high)
plt.xticks(rotation=90)
plt.show()

with open("monthly_AMZN.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        timestamp.append(row[0])
        AMZN_high.append(int(row[2]))

plt.bar(timestamp, AMZN_high)
plt.xticks(rotation=90)
plt.show()
