import csv
from collections import Counter

with open("C:\\Users\\TRUSTANA MARKETING\\Downloads\\SOCR-HeightWeight.csv", newline= "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    height = file_data[i][1]
    new_data.append(float(height))

#finding mean
totalElements = len(new_data)
sumOfAllElements = 0
for i in new_data:
    sumOfAllElements+=i

mean = sumOfAllElements/totalElements

print(mean)

#median
new_data.sort()
if totalElements%2==0:
    number1 = float(new_data[totalElements//2])
    number2 = float(new_data[totalElements//2-1])

    median = (number2 + number1)/2

else:
    median = new_data[totalElements//2]

print(median)

#mode
data = Counter(new_data)
modeDataForRange = {"50-60":0,"60-70":0,"70-80":0}
for height , occurence in data.items():
    if 50<float(height)<60:
        modeDataForRange["50-60"]+=occurence
    elif 60<float(height)<70:
        modeDataForRange["60-70"]+=occurence
    elif 70<float(height)<80:
        modeDataForRange["70-80"]+=occurence

modeRange, modeOccurence = 0,0

for range, occurence in modeDataForRange.items():
    if occurence> modeOccurence:
        modeRange, modeOccurence=[int(range.split("-")[0]), int(range.split("-")[1])],occurence
mode = float((modeRange[0]+modeRange[1])/2)

print(mode)
        
