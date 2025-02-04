
arr = [42, 23, 74, 11, 65, 58, 94, 36, 99, 87, 74]
# elements larger than the pivot move to the right
#elements move to the left if it's smaller than the pivot. 
#place pivot at it's correct position
#recursion



def quick_sort(arr,low, up): 
    pivot = arr[low]
    if (low<up):
        pivot_index = Partition(arr,low,up);
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,up)

        
def Partition(arr,low, up ): 
    pivot = arr[low]
    left = low+1
    right = up
    
    while(left<right):
        while arr[left]<=pivot and left<=right:
            left+=1
        while left<=right and arr[right]>pivot: 
            right -=1
        if left<right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right;



quick_sort(arr,0,len(arr)-1)
print(arr)