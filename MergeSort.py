
def MergeSort(arr, l, r, n=0):   
    if l < r:
        mid = (l + r) // 2
        MergeSort(arr, l, mid, n+1)   
        MergeSort(arr, mid+1, r, n+1) 
        Merge(arr, l, mid, r, n+1)    

def Merge(arr, l, mid, r, n): 
    left = arr[l:mid+1]   
    right = arr[mid+1:r+1]  
    i = 0 
    j = 0
    merged = []
    print("call no " , n)
    print("left ", left)
    while (i<len(left)) and (j<len(right)):
        if (left[i]<right[j]):
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j +=1
    while (i<len(left)): 
        merged.append(left[i])
        i+=1
    while j<len(right): 
        merged.append(right[j])
        j+=1

    arr[l:r+1] = merged

arr = [724, 521 ,2 ,98 ,529 ,31 ,189 ,451,111,345,555]

MergeSort(arr, 0, len(arr)-1)
print("Sorted Array : ", arr)
