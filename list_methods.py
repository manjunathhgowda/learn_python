# Python List Methods
# 1. append()-Adds an element at the end of the list.

lst = [1, 2, 3]
lst.append(4)
print(lst)   # [1, 2, 3, 4]

# 2. insert()-Adds an element at a specific position.

lst = [1, 2, 3]
lst.insert(1, 10)  
print(lst)   # [1, 10, 2, 3]

# 3. extend()-Adds all elements of another iterable (like list/tuple).

lst = [1, 2]
lst.extend([3, 4])
print(lst)   # [1, 2, 3, 4]

# 4. remove()-Removes the first occurrence of a value.

lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)   # [1, 3, 2]

# 5. pop()-Removes element at given index (default last).

lst = [10, 20, 30]
x = lst.pop()
print(x)     # 30
print(lst)   # [10, 20]

# 6. clear()-Removes all elements.

lst = [1, 2, 3]
lst.clear()
print(lst)   # []

# 7. index()-Returns the index of first occurrence.

lst = [5, 10, 15, 10]
print(lst.index(10))  # 1

# 8. count()-Returns how many times a value appears.

lst = [1, 2, 2, 3, 2]
print(lst.count(2))   # 3

# 9. sort()-Sorts the list (ascending by default).

lst = [3, 1, 4, 2]
lst.sort()
print(lst)   # [1, 2, 3, 4]

# With reverse:

lst.sort(reverse=True)
print(lst)   # [4, 3, 2, 1]

# 10. reverse()-Reverses the list order.

lst = [1, 2, 3]
lst.reverse()
print(lst)   # [3, 2, 1]

# 11. copy()- Creates a shallow copy of the list.

lst = [1, 2, 3]
new_lst = lst.copy()
print(new_lst)   # [1, 2, 3]