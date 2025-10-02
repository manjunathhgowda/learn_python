# Python Dictionary Methods

d = {"a": 1, "b": 2, "c": 3}

# 1. dict.keys()-Returns all the keys in the dictionary.
print(d.keys())   # dict_keys(['a', 'b', 'c'])

# 2. dict.values()-Returns all the values in the dictionary.
print(d.values())   # dict_values([1, 2, 3])

# 3. dict.items()-Returns key–value pairs as tuples.
print(d.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])

# 4. dict.get(key, default)-Returns the value for a given key. If key not found → returns default instead of error.
print(d.get("a"))        # 1
print(d.get("z", "NA"))  # NA

# 5. dict.update(other_dict)-Updates dictionary with another dictionary (or key=value pairs).
d.update({"d": 4})
print(d)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 6. dict.pop(key, default)-Removes the element with given key and returns its value.
print(d.pop("b"))   # 2
print(d)            # {'a': 1, 'c': 3, 'd': 4}

# 7. dict.popitem()-Removes and returns the last inserted (key, value) pair.
print(d.popitem())   # ('d', 4)

# 8. dict.setdefault(key, default)-Returns value of key; if key not present, inserts it with given default.
print(d.setdefault("x", 100))  # 100
print(d)   # {'a': 1, 'c': 3, 'x': 100}

# 9. dict.clear()-Removes all items from dictionary.
d.clear()
print(d)   # {}