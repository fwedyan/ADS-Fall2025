from array_stack import ArrayStack

'''create a copy of the stack'''
def copy(source, dest):
   #source: [1,2,3,4,5]  -> 5 is the top 
   #why we needed the temp stack?
   temp = ArrayStack()
   #create the copy
   while not source.is_empty():
       temp.push(source.top())
       source.pop()
   #temp = [5,4,3,2,1] source = [ ]
   while not temp.is_empty():
       dest.push(temp.top())
       source.push(temp.pop())
   #dest = [1,2,3,4,5], source = [1,2,3,4,5]    
         
'''print from top to bottom'''
def printStack(s:ArrayStack):
  print("from top: ", end = ' ')
  temp = ArrayStack()
  while not s.is_empty():
      print(s.top(), end = ' ')
      temp.push(s.pop())
  print()   
  while not temp.is_empty():
      s.push(temp.pop())

def printStack_bottom_top(s:ArrayStack()):
    print("from bottom to top: ", end = ' ')
    temp = ArrayStack()
    while not s.is_empty():
        temp.push(s.pop())
    while not temp.is_empty():
        print(temp.top(), end = ' ')
        s.push(temp.pop())
    print()   
   # S= [1,
   #    2
   #     ,3,
   #     10
   #     ,5] top =1
''' Swap the top with the value underneath '''
def swapFirstTwo(s:ArrayStack):
    #[1,2,3,4], 4, 3
   if len(s) >=2:
     first = s.pop()
     second = s.pop()
     s.push(first)
     s.push(second)
   #...
   #s = [2,
   #     1,
   #     3,
   #     10
   #     ,5] top = 2 
''' Write a function to swap the top and 
bottom of a given stack'''
def swapTopBottom(s:ArrayStack()):
    temp = ArrayStack()
    if len(s) >=2:
      top =s.top()
    while not s.is_empty():
        temp.push(s.top())
        bottom = s.pop()
    temp.pop()
    temp.push(top)
    while len(temp)>1:
        s.push(temp.pop())
    s.push(bottom)    
    
''' Push a stack (source) on top of another stack
(dest)'''
def push_stack(source, dest):
    pass

if __name__ == '__main__':        
 s1 = ArrayStack()
 x = 1
 y = 2
 s1.push(x)
 s1.push(y)
 s1.push(3)
 s1.push(4)
 s1.push(5)
 # x = s1.pop()
 # y = s1.pop()
 # print(x)
 # print(y)
 
 s2 = ArrayStack()
 copy(s1,s2)
 print("s1: ", end = " "); printStack(s1)
 print("s1: ", end = " "); printStack_bottom_top(s1)
 #print("s2: "); printStack(s2)
 #print(s2)
# s1.push(1)
 #s1.push(2)
 #s1.push(3)
 #s1.push(4)
 #s1.push(5)
 #printStack(s1)
# swapFirstTwo(s1)
# copy(s1,s2)
# printStack(s2)
# swapTopBottom(s1)
# printStack(s1)
 