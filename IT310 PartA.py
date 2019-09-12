from random import *

def dateArray(x):
    dates = []
    for i in range(0,x):
        dates.append(randint(1,365))
    return dates

countArray = []

for i in range(5,51):
    count = 0;
    for k in range(0,1000):
        dateList = dateArray(i)
        dateList.sort()
        for j in range(0,len(dateList)-1):
            if dateList[j] == dateList[j+1]:
                count += 1
                break
    countArray.append(count)
print(countArray)
print('N | Frequency')
for i in range(5,51):
    print(i,'|',countArray[i-5])








