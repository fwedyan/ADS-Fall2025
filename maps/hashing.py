########## create a hash using user-defined objects#########
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        """defines how an object is hashed"""
        return hash((self.id, self.name))

s = Student("078722","Fadi")
print(hash(s))
print(hash(s.name))
print(hash(123344586586))
#Notes about Python hash
# 1. Only immutable objects 
# 2. implement __eq__ if you implement __hash__
# 3. if two objects are equal, then their hashes 
# should also be equal
#####################
