# Creating a tuple with multiple elements
my_tuple = (1, 2, 3, "hello", 4.5)

# Creating a tuple without parentheses (optional, but parentheses are recommended for clarity)
my_tuple = 1, 2, 3, "hello", 4.5

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with a single element (note the trailing comma)
single_element_tuple = (5,)
# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: hello

# Negative indexing
print(my_tuple[-1])  # Output: 4.5
print(my_tuple[-2])  # Output: hello

tuples2 = ((1.5,5,7),[3.6,1.4])
print(tuples2[1])
t3 = ('a','b','c')[1:3]
print(type(t3))
print(t3)
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")