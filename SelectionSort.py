arr = [-5,1,12,5,16,2,12,14]

for i in range(len(arr)-1):
    minVal = arr[i]
    minIndex = i 
    for j in range(i+1,len(arr)):
        if arr[j]<minVal: 
            minVal = arr[j]
            minIndex = j
    arr[minIndex] = arr[i]
    arr[i] = minVal

for i in arr: 
    print(i);