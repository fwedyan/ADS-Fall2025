from linked_list import LinkedList

class LinkedListExtended(LinkedList):
    def _reverse_list(self,node:LinkedList.Node,n):
     if n< 2:
         return node
     rest = self._reverse_list(node._next,n-1)
     node._next._next = node
     node._next = None 
     
     return rest

    def reverse(self):
        if self.is_empty():
            return
        #self._tail = self._head
        self._head = self._reverse_list(self._head,len(self))
        #self._tail._next = None

def printList(llist:LinkedList):
    # create a new linked list
    new_llist = LinkedList()
    # traverse the linked list and add the elements on the new linked list
    while not llist.is_empty(): 
        element = llist.remove_head()
        if not llist.is_empty():
            print(element, end='->')
        else:
            print(element)
        new_llist.insert_first(element)

    while not new_llist.is_empty(): # un-reverse the list
        element = new_llist.remove_head()
        llist.insert_first(element)

if __name__ == "__main__":
    # create a linked list 
    my_list = LinkedListExtended()
    my_list.insert_first(1)
    my_list.insert_first(3)
    my_list.insert_first(5)
    my_list.insert_first(7)
    my_list.insert_first(9)
    my_list.insert_first(11)
    my_list.insert_first(13)
    my_list.insert_first(15)    

    printList(my_list)
    my_list.reverse()
    print("Reversed List:") 
    printList(my_list)
    print(len( my_list))
