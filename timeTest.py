import XMLPatternTreeMatch as XMLQuery
import xml.etree.ElementTree as ET
import time

data = ET.parse('smallData.xml').getroot()
dataMedium = ET.parse('mediumData.xml').getroot()
dataLarge = ET.parse('largeData.xml').getroot()
pattern1 = ET.parse('search.xml').getroot()
pattern2 = ET.parse('search2.xml').getroot()

print("Each query will run 10 times and print the average elapsed time")

totalTime = 0
for i in range(100):
    solutions = dict()
    startTime = time.time()
    XMLQuery.find(data, pattern1, solutions)
    endTime = time.time()
    totalTime += (endTime - startTime)
print("average time first small query: ", totalTime / 100)

totalTime = 0
for i in range(100):
    solutions = dict()
    startTime = time.time()
    XMLQuery.find(data, pattern2, solutions)
    endTime = time.time()
    totalTime += (endTime - startTime)
print("average time second small query: ", totalTime / 100)

print("\n")

totalTime = 0
for i in range(100):
    solutions = dict()
    startTime = time.time()
    XMLQuery.find(dataMedium, pattern1, solutions)
    endTime = time.time()
    totalTime += (endTime - startTime)
print("average time first medium query: ", totalTime / 100)

totalTime = 0
for i in range(100):
    startTime = time.time()
    XMLQuery.find(dataMedium, pattern2, solutions)
    endTime = time.time()
    totalTime += (endTime - startTime)
print("average time second medium query: ", totalTime / 100)

print("\n")

totalTime = 0
for i in range(10):
    solutions = dict()
    startTime = time.time()
    XMLQuery.find(dataLarge, pattern1, solutions)
    endTime = time.time()
    totalTime += (endTime - startTime)
print("average time first large query: ", totalTime / 10)

totalTime = 0
for i in range(10):
    startTime = time.time()
    XMLQuery.find(dataLarge, pattern2, solutions)
    endTime = time.time()
    totalTime += (endTime - startTime)
print("average time second large query: ", totalTime / 10)