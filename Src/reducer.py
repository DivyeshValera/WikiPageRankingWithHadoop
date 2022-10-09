import sys
import datetime
data = []
word_data = []
title_data = []
total_word = []
day = []
month = []
year = []
wd = []
wd1 = []
forCal = []
total = 0
lstOfmon = []
lstOfwc = []
query7_output = []
for line in sys.stdin:
    line = line.strip()
    temp = line.split(",")
    try:
        title = temp[0]
        pageid = temp[1]
        size = int(temp[2])
        wordcount = int(temp[3])
        word_data.append(wordcount)
        ts = temp[4]
        timestamp = temp[4].split("/")
        Day = int(timestamp[0])
        Month = int(timestamp[1])
        Year = int(timestamp[2])
    except ValueError:
        continue
    data.append((title,pageid,size,wordcount,ts))
    title_data.append(title)
    day.append(Day)
    month.append(Month)
    year.append(Year)
    
    if(title == "Linux kernel"):
    	ddmmyy = datetime.date(Year,Month,Day)
    	query7_output.append((wordcount,ddmmyy))
    	    
    if(wordcount > 7000 and Month >= 3 and Month <= 9 and Day >= 1 and Day <= 30):
        print(title,wordcount,Day,Month,Year)
    
    if(Year == 2022):
            wd.append(wordcount)
    
    if(Month >= 2 and Month <= 7 and Year == 2022):
        wd1.append(wordcount)
        
    if(Month >= 3 and Month <= 7 and Year == 2022):
        if(wordcount <= 6000):
        	forCal.append(wordcount)
    
    if(Year == 2022): 	
    	lstOfmon.append(Month)
    	lstOfwc.append(wordcount)
        
print("\nQ-2 Output\nThe average of wordcounts where year in timestamp is equals to 2022 : ","\nAverage Is:",sum(wd)/len(wd),"\n")

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

#6
print("\nQ-6\nDisplay the titles having wordcount greater then 55000 and size greater then 50000.")
for i in data:
	if(i[2] > 50000 and i[3] > 12000):
		print(i[0])
		
#7
print("\nQ-7\nDisplay the wordcount and timestamp in YYYY-MM-DD format of title ‘Linux kernel’.")
for i in query7_output:
	print(i[0],i[1])

#8
print("\nQ-8\nDisplay the wordcount and timestamp of title ‘Travel website’.")
for k in data:
	if(k[0]=="Travel website"):
		print(k[0],k[3],k[4])

#9	
print("\nQ-9\nCalculate the sum and average of wordcounts where wordcount is less than or equal to 6000 and timestamp is in between 2022-04-01 to 2022-08-01.","\nSum is:",sum(forCal),"\nAverage Is:",sum(forCal)/len(forCal))

#10
print("\nQ-10\nDisplay the month of year 2022(in timestamp) having maximum and minimum wordcount.")
print("Maximum wordcount is ",max(lstOfwc), "in month no." ,lstOfmon[lstOfwc.index(max(lstOfwc))])
print("Minimum wordcount is ",min(lstOfwc), "in month no." ,lstOfmon[lstOfwc.index(min(lstOfwc))]) 
		
