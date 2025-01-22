arr = [34,45,23,12,56]; 

for i in range(len(arr)):
    for j in range(len(arr)-i-1): 
        if arr[j]>arr[j+1]: 
            temp = arr[j]; 
            arr[j] = arr[j+1]
            arr[j+1]= temp
print("end of sort"); 

for i in arr:
    print(i);