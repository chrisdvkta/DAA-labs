arr = [1, 3 ,7, 9, 11 ,32, 52, 74 ,90]
 
flag = 0
def binarySearch(arr,target,l,r): 
    flag = 0;
    while (l<=r): 
        m = int((l+r)/2)
        if target==arr[m]: 
            flag = m;
        elif target<arr[m]:
            return binarySearch(arr,target,l,m-1); 
        else: 
            return binarySearch(arr,target,m+1,r);
        return flag;

print(binarySearch(arr,32,0,len(arr)-1))
            
