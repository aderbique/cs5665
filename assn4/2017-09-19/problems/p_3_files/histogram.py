######################
# p3.py
######################
import sys, csv
dictionary = {}

with open("data.csv") as file:
    for line in file:
        time, temp = line.split(",")
        if temp in dictionary:
            dictionary[temp] += 1
        else:
            dictionary[temp] = 1

file.close()

w = csv.writer(open("histogram.csv", "w"))
for key, val in sorted(dictionary.items()):
    w.writerow([key, val])
