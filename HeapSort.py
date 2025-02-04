arr = [16 ,14, 10 ,8 ,7 ,9 ,3 ,2 ,4 ,1]
#heap is represented in an array. the array representation of a heap is done through breadth tree traversal
#for every parent node i in the heap, it consists of i/2 children.
#for every node j, it consists of children of node 2j and 2j+1. for eg : node j=1 has children 2 and 3




def HeapSort(A, n, value): 
    n = n +1 
    A[n] = value
    for i in range (0,1): 
        print(i)
        
HeapSort(arr,0,5)
