import random  #use a library that exists

def createList(a,b,size):
    '''function to  create and return a list and fill it with random int.
    parameters: 
        a: lower bound of the random numbers
        b: Uower bound of the random numbers
        size: size of the created list
  '''
  
    list = []  # empty list
    for i in range(0,size):
        #random is a library (package) in python
        n= random.randint(a,b)
        list.append(n) #method that adds values to the list
    return list

def main():
    list1=createList(1,6,5)
    list2=createList(1,6,5)
    print(list1)
    #print(list2)
    #slicing
    list3 = list1[0:2]  #gets list[0], list[1]
    #print(list3)
    #print(list1[:-len(list1)+1])
    #list[0:5]=[1,1,1,1,1]
    #list3 = list1+list2
    list4 = list1*2
    print("list 4: ", list4)
    list4+=list4
    #print("list 3: ", list3)
    print("list 4: ", list4)
    
    for x in list1:  #common loop for accessing elements in lists
        print(x)
        
    if not 555 in list4:
        print("no")
    else:
        print("yes")
    
    
    
main()
        
