import os
text = open("ntplog.txt","rt")
out = open("out.txt","wt")
for i in text:
    out.write(' '.join(i.split()))
    if(i == "="):
        print("\n")
text.close()
out.close()
print(out)

# new