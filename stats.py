# reads from a file and computes mean, median, and mode
from collections import Counter

def meanList(numbers): 
        mean = sum(numbers)/len(numbers)
        return mean

def modeList(numbers): 
    frequency = Counter(numbers)
    maxCount = max(frequency.values())
    mode = [x for x in frequency if frequency[x] == maxCount]
    if len(mode) == len(numbers): 
        return []
    return sorted(mode)

def medianList(numbers): 
    sortedList = sorted(numbers)
    n = len(numbers)
    if n % 2 == 1:
        return sortedList[n//2]
    else:  
        middle1 = sortedList[n//2-1]
        middle2 = sortedList[n//2]
        median = (middle1+middle2)/2
        return median    

def main(): 
    f = open("File1.txt", "r")
    numbers = [] 
    for line in f: 
        numbers.extend([int(x) for x in line.split()])
    print(f"The set of numbers is: {numbers}")
    print(f"Mean: {meanList(numbers)}")
    print(f"Mode: {', '.join(map(str, modeList(numbers)))}")
    print(f"Median: {medianList(numbers)}")
    f.close()

if __name__ == "__main__": 
    main()