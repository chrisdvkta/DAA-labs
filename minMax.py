arr = [7 ,10, 14, 9 ,11 ,32, 52, 74 ,6]


def MinMax(arr, l,r): 
    m = int((l+r)/2)
    if (l==r): 
        max = min = arr[l]
    elif (l==r-1):
        if (arr[l]>arr[r]): 
            max = arr[l]
            min = arr[r]
        else:
            max = arr[r]
            min = arr[l]    



    left = MinMax(arr,l,m)
    right = MinMax(arr,m+1,r)


