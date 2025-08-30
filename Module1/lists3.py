import random
def createList(a,b,n):
    list = []
    for i in range(0,n):
        n= random.randint(a,b)
        list.append(n)
    return list

def main():
    list1=createList(1,6,5)
    try:
        print(list1.index(5))        
        print(list1.index(15))
        
    except ValueError:
        print("requested value does not exist in the list")
        
    list1.insert(9,"nine")
    list1.insert(1,"one")
    print(list1)
    print(list1.index("nine"))
    #print(list1.index("nineee"))
    
main()
        
