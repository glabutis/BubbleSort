import random

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [20.1, 19.6, 18.0, 17.8, 25.2, 18.7, 21.9, 16.3, 25.4, 20.5, 17.8, 19.3]
newarr = []

bubbleSort(arr)
f = open("num.txt", "w+")
print ("Sorted array is:")
for i in range(len(arr)):
    f.write("%d" %arr[i] + "\n")
    newarr.append(arr[i])
print(newarr[len(newarr) - 1] - newarr[0])
print(newarr)
