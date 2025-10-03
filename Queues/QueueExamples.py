from array_queue import ArrayQueue

''' a function to apply round robin'''
def roundRobin(q:ArrayQueue, slice:int):
    pass
''' if the size is even, the mid is the first
value in the upper half'''

def get_queue_mid(q:ArrayQueue):
    #1,2,3,4
    
    copy1 = ArrayQueue()
    half_index = len(q)//2 
    i = 0
    while i<half_index:
        copy1.enqueue(q.dequeue())
        i+=1
    half_value = q.first()
    while not q.is_empty():
        copy1.enqueue(q.dequeue())
    while not copy1.is_empty():
        q.enqueue(copy1.dequeue())
    return half_value

''' duplciate each queue entry
example: a,b,c--> a,a, b,b,c,c'''
def duplicateQueueEntries(q:ArrayQueue):
   copy1 = ArrayQueue()
   copy2 = ArrayQueue()
   while not q.is_empty():
      copy1.enqueue(q.first())
      copy2.enqueue(q.dequeue())
      
   while not copy1.is_empty():
       q.enqueue(copy1.dequeue())
       q.enqueue(copy2.dequeue())
       
        

''' duplicate the queue 
example: a,b,c --> a,b,c,a,b,c
'''
'''What is the big-O of the function below, assumming
all queue operations are O(1)'''
def duplicateQueue(q:ArrayQueue):
    copy1 = ArrayQueue()
    copy2 = ArrayQueue()
    while not q.is_empty():
       copy1.enqueue(q.first())
       copy2.enqueue(q.dequeue())
       #q.dequeue()
       
    while not copy1.is_empty():
        q.enqueue(copy1.dequeue())
    while not copy2.is_empty():
        q.enqueue(copy2.dequeue())
        

''' printing the queue, starting from head(front)'''
def printQueue(q:ArrayQueue()):
    tempQ = ArrayQueue()
    print("starting from the front: ", end = ' ')
    while not q.is_empty():
       tempQ.enqueue(q.first())
       print(q.dequeue(), end = ' ') 
       
    while not tempQ.is_empty():
        q.enqueue(tempQ.dequeue())
        
    print()


q = ArrayQueue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.enqueue('d')

print(get_queue_mid(q))

#duplicateQueue(q)
duplicateQueueEntries(q)
printQueue(q)
duplicateQueueEntries(q)
printQueue(q)
duplicateQueue(q)
printQueue(q)
#print(q.is_empty())
