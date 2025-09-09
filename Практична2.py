list1 = [4,16,5,12,17,1,10,14,2,5, "larl","collapse","yatoro","mira","skiter","pure","watson","quinn","no[o]ne","bzm"]

intList = []
for x in list1:
    if type(x) == str:
        break
    intList.append(x)
intList.sort()

strList = []
for x in list1:
    if type(x) == int:
        continue
    strList.append(x)
strList.sort()

twoIntList = []
for x in intList:
    if x%2 == 0:
        twoIntList.append(x)

capsList = []
for x in strList:
    capsList.append(x.upper())

intList.extend(strList)
list1 = intList

print("Список усіх елементів:", list1)
print("Список усіх елементів кратних двом:", twoIntList)
print("Список усіх елементів типу str великими літерами:", capsList)
