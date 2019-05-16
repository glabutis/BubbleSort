import random

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [20.1, 19.6, 18.0, 17.8, 25.2, 18.7, 21.9, 16.3, 25.4, 20.5, 17.8]
newarr = []
full = 0

#Get average
for i in arr:
    full += i
#Call bubbleSort function
bubbleSort(arr)
#Make newarr
for i in range(len(arr)):
    newarr.append(arr[i])
#Get range of newarr
print("Range: " + str(newarr[len(newarr) - 1] - newarr[0]))
#Get average of newarr
print("Average: " + str(int(full / len(newarr))))
#Print newarr
print("Sorted arry is: " + str(newarr))
