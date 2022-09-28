from functools import total_ordering
from operator import le
from re import T
import sys
data = []
word_data = []
title_data = []
total_word = []
day = []
month = []
year = []
wd = []
wd1 = []
total = 0
for line in sys.stdin:
    line = line.strip()
    temp = line.split(",")
    try:
        title = temp[0]
        pageid = temp[1]
        size = temp[2]
        wordcount = int(temp[3])
        word_data.append(wordcount)
        timestamp = temp[4].split("/")
        Day = int(timestamp[0])
        Month = int(timestamp[1])
        Year = int(timestamp[2])
    except ValueError:
        continue
    data.append((title,pageid,size,wordcount))
    title_data.append(title)
    day.append(Day)
    month.append(Month)
    year.append(Year)
    
    if(wordcount > 7000 and Month >= 3 and Month <= 9 and Day >= 1 and Day <= 30):
        print(title,wordcount,Day,Month,Year)
    
    if(Year == 2022):
            wd.append(wordcount)
    
    if(Month >= 2 and Month <= 7 and Year == 2022):
        wd1.append(wordcount)
print("\nQ-2 Output\nThe average of wordcounts where year in timestamp is equals to 2022 : ","\nSum Is",sum(wd),"\nAverage Is:",sum(wd)/len(wd),"\n")

# Q-3 Finished
print("\nQ-3 Output")
for i in data:
    if(i[3]>1000 and i[3]<5000):
        print(i[0],i[1],i[2],i[3])

# Q-4 Finished
print("\nQ-4 Output\nCalculate the sum of wordcounts where year and month in timestamp is in between 2022-02 to 2022-07.")
# for i in data:
    
print("sum of wordcounts where year and month in timestamp is in between 2022-02 to 2022-07 : ",sum(wd1))

# Q-5 Finished
print("\nQ-5 Output\nDisplay the titles having maximum and minimum wordcounts")
word_count_max = max(word_data)
#print(word_count_max)
print("Maximum Word Count Is : ",word_count_max,"\nMaximum Word Count Title Is : ",title_data[word_data.index(max(word_data))])
word_count_min = min(word_data)
#print(word_count_min)
print("Minimum Word Count Is : ",word_count_min,"\nMinimum Word Count Title Is : ",title_data[word_data.index(min(word_data))])