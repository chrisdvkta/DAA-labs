arr = [16 ,14, 10 ,8 ,7 ,9 ,3 ,2 ,4 ,1]
#heap is represented in an array. the array representation of a heap is done through breadth tree traversal
#for every parent node i in the heap, it consists of i/2 children.
#for every node j, it consists of children of node 2j and 2j+1. for eg : node j=1 has children 2 and 3




class MaxHeap: 
    def __init__(self): 
        self.heap = []
    
    def insert(self,value): 
        self.heap.append(value); 
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,index): 
        parent = (index-1)//2
        print("current parent index is " ,parent)
        if (self.heap[parent]<self.heap[index]):
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index -1)//2
            print("nnew parent index becomes", parent)

    def display(self): 
        print(self.heap);

max_heap = MaxHeap();
max_heap.insert(10);
max_heap.insert(20);
max_heap.insert(5);
max_heap.insert(40);
max_heap.insert(90);

max_heap.display();

