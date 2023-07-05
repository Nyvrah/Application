import os
from datetime import datetime as dt

def open_file():
    data_folder = "data/" + os.listdir('data')[0] + "/"
    nir_file = open(data_folder + [f for f in os.listdir(data_folder) if f.endswith('.nir')][0], "r")
    for _ in range(15): line = next_line(nir_file)
    return line, nir_file

def next_line(file):
    return file.readline().split()

def get_avg(line):
    n = len(line) - 2
    avg = [0,0,0]
    for i in range(1, n+1):
        avg[i%3-1] += int(float(line[i])/(n/3))
    return avg