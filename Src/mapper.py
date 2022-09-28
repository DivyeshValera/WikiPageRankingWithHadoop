import sys
from time import time

pageid=""
ns=""
title=""
size=""
snippet = ""
timestamp = ""
wordcount = ""
count = 1

for line in sys.stdin:
    line = line.strip()
    columns = line.split(",")
    if count==1:
        count = 0
        continue
    else:
        title=columns[1]
        pageid = columns[2]
        size=columns[3]
        wordcount = columns[4]
        timestamp = columns[5]
        print(title+","+pageid+","+size+","+wordcount+","+timestamp)