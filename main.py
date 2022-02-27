import os

text = open("ntplog.txt")
new_file = open("new_file.txt", "w")
r = text.readlines()

for line in r:
    new_file.write(line)
new_file.close()






