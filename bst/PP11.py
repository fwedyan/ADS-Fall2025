from bst.binary_search_tree import TreeMap
from bst.avl_tree import AVLTreeMap
import random

def create(size, value = 1):
    bst = AVLTreeMap()     
    bst2 = TreeMap()
    counter = 0
    while counter<size:
        val = random.randint(1,1000)
        if not val in bst.keys():
            bst[val] = value
            bst2[val] = value
            counter +=1
    return bst,bst2

bst_avl, bst_org = create(2000)

print(bst_avl.height())
print(bst_org.height())