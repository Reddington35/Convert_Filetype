import os
import pandas as pd

file_read = "ntplog.txt"
file_write = "new_gile.txt"
text = open(file_read,"r")
data = text.read()
text.close()

with open(file_write,"a") as file:
    text.write(data)
print("done")





