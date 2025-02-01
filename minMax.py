arr = [7 ,10, 14, 9 ,11 ,32, 52, 74 ,6]


def MinMax(arr, l,r): 
    if (l==r): 
        minVal = maxVal = arr[l]
    elif (l==r-1):
         minVal = min(arr[l],arr[r])
         maxVal = max(arr[l], arr[r])
    else: 
        mid = int((l+r)/2)
        min1,max1= MinMax(arr,l,mid)
        min2,max2= MinMax(arr,mid+1,r)
        minVal = min(min1,min2)
        maxVal = max(max1,max2)
    return (minVal,maxVal)



print(MinMax(arr,0,len(arr)-1))


        




