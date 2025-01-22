arr = [5,1,12,-5,16,2,12,14]

for i in range(1,len(arr)): 
    x = arr[i];
    j = i-1; 
    while (x<arr[j] and j>=0):
        arr[j+1] = arr[j];
        j = j-1
    arr[j+1] = x; 


print(arr)



