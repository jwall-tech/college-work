keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

d = dict(zip(keys,values))
print(d)

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}

keysToRemove = ["name", "salary"]

for key in keysToRemove:
    sampleDict.pop(key)

print(sampleDict)

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

temp = sampleDict["city"]
sampleDict["location"] = temp
sampleDict.pop("city")

print(sampleDict)
