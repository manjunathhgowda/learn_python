# Python Set Methods
# 1. add()-Adds a single element to the set.

s = {1, 2, 3}
s.add(4)
print(s)   # {1, 2, 3, 4}

# 2. update(iterable)-Adds multiple elements (from list/tuple/set) to the set.

s.update([5, 6])
print(s)   # {1, 2, 3, 4, 5, 6}

# 3. remove(x)-Removes element x. Raises KeyError if not present.

s.remove(2)
print(s)   # {1, 3, 4, 5, 6}

# 4. discard(x)-Removes element x. Does not raise error if missing.

s.discard(10)   # no error

# 5. pop()-Removes and returns a random element.

print(s.pop())   # removes some random element

# 6. clear()-Removes all elements from the set.

s.clear()
print(s)   # set()

# 7. copy()-Returns a shallow copy of the set.

s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)   # {1, 2, 3}

# Set Operations Methods

# 8. union(other)-Returns a set with elements from both sets.

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))   # {1, 2, 3, 4, 5}

# 9. intersection(other)-Returns common elements of both sets.

print(a.intersection(b))   # {3}

# 10. difference(other)-Returns elements present in first set but not in second.

print(a.difference(b))   # {1, 2}

# 11. symmetric_difference(other)-Returns elements in either set, but not both.

print(a.symmetric_difference(b))   # {1, 2, 4, 5}

# 12. issubset(other)-Checks if current set is subset of another.

print({1,2}.issubset(a))   # True

# 13. issuperset(other)-Checks if current set is superset of another.

print(a.issuperset({1,2}))   # True

# 14. isdisjoint(other)-Checks if two sets have no common elements.

print(a.isdisjoint({7,8}))   # True