import torch
import csv
import matplotlib.pyplot as plt

data = []


with open("Base_data.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:
        data.append([float(item) for item in row[1:]])


plt.plot(range(len(data[0])),data[0])
plt.show()


