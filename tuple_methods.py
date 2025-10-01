# Tuple Object Methods
# 1. tuple.count(x)- Counts how many times x appears.

t = (1, 2, 3, 2, 2, 4)
print(t.count(2))   # 3

# 2. tuple.index(x, start=0, end=len(tuple))- Returns the index of the first occurrence of x.

t = (10, 20, 30, 20)
print(t.index(20))   # 1

# Built-in Functions Usable with Tuples
# These are not tuple methods, but they work with tuples:

# 1. len(tuple) → Returns number of elements
t = (1, 2, 3, 4)
print(len(t))   # 4

# 2. max(tuple) → Returns maximum element
t = (5, 10, 2, 8)
print(max(t))   # 10

# 3. min(tuple) → Returns minimum element
t = (5, 10, 2, 8)
print(min(t))   # 2

# 4. sum(tuple) → Returns sum of all elements
t = (1, 2, 3, 4)
print(sum(t))   # 10

# 5. sorted(tuple) → Returns a list of sorted elements
t = (5, 1, 4, 3)
print(sorted(t))   # [1, 3, 4, 5]

# 6. any(tuple) → Returns True if any element is truthy
t = (0, 0, 5, 0)
print(any(t))   # True (because 5 is truthy)

# 7. all(tuple) → Returns True if all elements are truthy
t = (1, 2, 3)
print(all(t))   # True
t2 = (0, 1, 2)
print(all(t2))  # False (because 0 is falsy)

# 8. tuple(iterable) → Creates a tuple from iterable
lst = [1, 2, 3]
t = tuple(lst)
print(t)   # (1, 2, 3)