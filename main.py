import os
import pandas as pd
text = open("ntplog.txt")
new_file = open("new_file.txt", "w")
r = text.readlines()

for line in r:
    new_file.write(line)
new_file.close()

new_file = pd.read_csv("new_file.txt")
new_file.to_csv("new_file.csv")






