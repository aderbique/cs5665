import os, sys, csv, re
import matplotlib.pyplot as plt
import numpy as np

import pandas
data = pandas.DataFrame()

df = pandas.read_csv('results.csv', sep=',')
data = pandas.concat([data, df])


LABELS = ["real", "user", "sys"]

plt.title('Time Taken by Classifier')
plt.xlabel('Time_Types')
plt.ylabel('Time_Value in (sec)')


data.boxplot(by='file')

plt.show()
