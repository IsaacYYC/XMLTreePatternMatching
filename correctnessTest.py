import XMLPatternTreeMatch as XMLQuery
import xml.etree.ElementTree as ET
import time

mediumData = ET.parse('mediumData.xml').getroot()
pattern1 = ET.parse('search.xml').getroot()
pattern2 = ET.parse('search2.xml').getroot()
mediumSolutions = dict()
mediumSolutions2 = dict()
XMLQuery.find(mediumData, pattern1, mediumSolutions)
XMLQuery.find(mediumData, pattern2, mediumSolutions2)

print("\nA dataset has been created for the purpose of testing correctness")
print("modify xml patterns in search and search2 to adjust query")
print("There are 104 client total")
print("100 with card_numbers and 1 with a cart_total, they all have names and account numbers")
print("\nThere are 205 employees total")
print("They all have names, and compensations, with at least a salary under compensation")
print("102 have stock, and 102 have commission, one has both\n\n")


print("query has found the following tags given query pattern\n", mediumSolutions.keys())

print("\n", len(mediumSolutions["employee"]), " records have been found matching this employee pattern")

userInput = int(input("Enter 1 to see all records found"))
if userInput == 1:
    for child in mediumSolutions["employee"]:
        print("------------------------------")
        XMLQuery.printResults(child, mediumSolutions)
        print("------------------------------")

print("\n\n")

print("query has found the following tags given query pattern\n", mediumSolutions2.keys())

print("\n", len(mediumSolutions2["client"]), " records have been found matching this client pattern")

userInput = int(input("Enter 1 to see all records found"))
if userInput == 1:
    for child in mediumSolutions2["client"]:
        print("------------------------------")
        XMLQuery.printResults(child, mediumSolutions2)
        print("------------------------------")

        
    



