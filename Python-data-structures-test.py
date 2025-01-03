test = "Hello World"
print(test)
length = len(test)
print(length)
partOfTest = test[0]
print(partOfTest)
print()
numbers = [1,2,3,4]
stringList = ["name", "age", "birthday"]
emptyList = []
numberList = list(range(1,5))
newList = numbers + stringList
forSorting = [3,10,9,8,1]
forSorting.sort()
for x in numbers:
    print(x, end = " ")
print()
for x in stringList:
    print(x, end = " ")
print()
for x in emptyList:
    print(x, end = " ")
print()
for x in numberList:
    print(x, end = " ")
print()
for x in newList:
    print(x, end = " ")
print()
for x in forSorting:
    print(x, end = " ")
print()
print(numbers == numberList)
print(len(forSorting))
