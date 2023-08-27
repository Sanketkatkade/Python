myDict = {
    "fast" : "a quick manner",
    "sanket" : "a coder",
    "marks" : [1,2,3],
    "anotherDict" : {"harry" : "youtuber"}
}


print(myDict['fast'])
print(myDict["sanket"])
print(myDict["marks"])
myDict["marks"] = [45.56]
print(myDict["marks"])
print(myDict["anotherDict"]["harry"])


# methods
print(myDict.keys())
print(myDict.values())
print(type(myDict.keys()))#it will print keys of the dictionary
print(list(myDict.keys()))#we can convert it into a list
print(myDict.items())#it print (key,value)for all items in the dictionary

# updating my list
print(myDict)
updateDict = {
    "lovish" : "friend",
    "sanket" : "a coder"
}

myDict.update(updateDict) # updates the dictionary by adding the key-value pairs from updateDict
print(myDict)

print(myDict.get("harry")) # if the key is not present then it will print none
# print(myDict["harry"]) # it will throw an error because it is not presnt in the dictionary



# Example
myDict = {
    "Pankha" : "Fan",
    "Ghadi" : "Watch",
    "Dabba" : "Box"
}
print(myDict.keys())
a = input("Enter you word\n ")
# print("The meaning of your word is :",myDict[a])

# Below line will not throw an error
print("The meaning of your word is :",myDict.get(a))