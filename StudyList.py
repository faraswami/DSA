# stack
lst = [1, 2, 3]
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]


lst = [1, 2, 3]
lst.insert(1, 10)
print(lst)  # Output: [1, 10, 2, 3]

# queue
lst = [1, 2, 3]
lst.insert(0, 5)
print(lst)  # Output: [5, 1, 2, 3]


# POP -Removes and returns an element from the list.
# By default, removes the last element (pop() == pop(-1)).


lst = []
lst.append("apple")
lst.append("banana")
lst.append("mango")

print(lst)  # ['apple', 'banana', 'mango']
print(lst.pop())  # 'mango' (last item removed)
print(lst)  # ['apple', 'banana']


# ----insert pop
lst = ["apple", "banana"]
lst.insert(1, "mango")  # Insert 'mango' at index 1

print(lst)  # ['apple', 'mango', 'banana']
print(lst.pop())  # 'banana' (last item still removed)
print(lst)  # ['apple', 'mango']


# -----pop at index
lst = ["apple", "mango", "banana"]
print(lst.pop(1))  # 'mango'
print(lst)  # ['apple', 'banana']
