#Program: Lists Demo
#Author: Nanette n.
#Date: 16/02/2025
 
#Declare Lists
 
#Initialised list
rainbowList = ["red","yellow", "green"]
 
#print list
print("This is the rainbowList")
print(rainbowList)
 
#Append List(Task 1)
print("\nAppend rainbowList\n")
print("Append blue")
rainbowList.append("blue")
print(rainbowList)
print("Append indigo")
rainbowList.append("indigo")
print(rainbowList)
print("\nThis is the rainbowList.")
 
#Count the number of elements(Bonus Task)
print("\nFind the number of elements in the list")
i = str(len(rainbowList))
print("\nThe number of elements in the list is: " + i)
 
 
#Insert at Position(Task 2)
print("\nInsert at Position in rainbowList")
print(rainbowList)
rainbowList.insert(1, "orange")
print(rainbowList)
 
#Delete at position(Task 2)
print("\nDelete at position 1 and last= ")
rainbowList.remove("orange")
rainbowList.pop(-1)
print(rainbowList)
 
#Append new elements to the list(Bonus Task)
print("\nAppend new elements")
print("Append orange in position 1, indigo, and violet\n")
rainbowList.insert(1, "orange")
rainbowList.append("indigo")
rainbowList.append("violet")
print(rainbowList)
 
#Print out one line at a time (Task 3)
#Implement sorthing a list in ascending and descending order (Bonus Task)
print("\nSorthing the list in ascending and descending alphabetical order\n")
print("Ascending...")
rainbowList.sort()
i = len(rainbowList)
j = 0
 
for j in range(i) :
    print(rainbowList[j])
    j = j+1
 
print("\n")
print("Descending...")
j=0
for j in range(i) :
    print(rainbowList[i-1])
    i = i-1