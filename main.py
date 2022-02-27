import os
import pandas as pd

# method that removes  char '=' from file
# and converts .txt to .csv
def format_csv():
    ntp = "ntplog.txt"
    new_ntp = "new_file.txt"
    text = open(ntp,"r")
    new_file = open(new_ntp,"w")
    r = text.readlines()

    for line in r:
        new_file.write(line.replace("=",""))
    new_file.close()

    new_file = pd.read_csv("new_file.txt")
    new_file.to_csv("new_file.csv")
    print(new_file)
    return 0

format = format_csv()







