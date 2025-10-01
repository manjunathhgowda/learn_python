# Python String Methods
#------------------------------1. Case Conversion--------------------------------------

# upper() → Converts string to uppercase.
"hello".upper()   # "HELLO"

# lower() → Converts string to lowercase.
"Hello".lower()   # "hello"

# capitalize() → First letter uppercase, rest lowercase.
"python".capitalize()   # "Python"

# title() → First letter of each word capitalized.
"hello world".title()   # "Hello World"

# swapcase() → Swaps case (upper→lower, lower→upper).
"PyThOn".swapcase()   # "pYtHoN"


# ------------------------------2. Checking String Content------------------------------
# isalnum() → True if all chars are alphanumeric.
"abc123".isalnum()   # True

# isalpha() → True if all chars are alphabets.
"abc".isalpha()   # True

# isdigit() → True if all chars are digits.
"123".isdigit()   # True

# isnumeric() → True if string is numeric.
"23".isnumeric()   # True

# isdecimal() → True if string has only decimal digits.
"123".isdecimal()   # True

# isspace() → True if string has only spaces.
"   ".isspace()   # True

# islower() → True if all chars are lowercase.
"hello".islower()   # True

# isupper() → True if all chars are uppercase.
"HELLO".isupper()   # True

# istitle() → True if string is title-cased.
"Hello World".istitle()   # True

# isidentifier() → True if valid Python identifier.
"name1".isidentifier()   # True


# ------------------------------3. Searching------------------------------

# find(sub) → Returns index of first occurrence (or -1).
"hello".find("l")   # 2

# rfind(sub) → Returns last occurrence index.
"hello".rfind("l")   # 3

# index(sub) → Like find, but raises error if not found.
"hello".index("e")   # 1

# rindex(sub) → Like rfind, but raises error.
"hello".rindex("l")   # 3

# startswith(sub) → True if string starts with substring.
"python".startswith("py")   # True

# endswith(sub) → True if string ends with substring.
"python".endswith("on")   # True

# ------------------------------4. Modification------------------------------

# replace(old, new) → Replace substring with another.
"hello world".replace("world", "Python")   # "hello Python"

# strip() → Removes leading and trailing spaces.
"  hello  ".strip()   # "hello"

# lstrip() → Removes spaces from left.
"  hello".lstrip()   # "hello"

# rstrip() → Removes spaces from right.
"hello  ".rstrip()   # "hello"

# ljust(width) → Left-align string in given width.
"hi".ljust(5, "-")   # "hi---"

# rjust(width) → Right-align string in given width.
"hi".rjust(5, "-")   # "---hi"

# center(width) → Center-align string.
"hi".center(6, "*")   # "**hi**"

# zfill(width) → Pads with leading zeros.
"42".zfill(5)   # "00042"

# ------------------------------5. Splitting & Joining------------------------------

# split() → Splits string into list.
"a,b,c".split(",")   # ['a','b','c']

# rsplit() → Splits from right side.
"a,b,c".rsplit(",",1)   # ['a','b,c']

# splitlines() → Splits by line breaks.
"hello\nworld".splitlines()   # ['hello','world']

# partition(sep) → Splits into 3 parts (before, sep, after).
"hello world".partition(" ")   # ('hello',' ','world')

# rpartition(sep) → Like partition but from right.
"hello world".rpartition(" ")   # ('hello',' ','world')

# join(iterable) → Joins elements with separator.
"-".join(["a","b","c"])   # "a-b-c"

# ------------------------------6. Encoding / Formatting------------------------------

# encode() → Returns encoded version.
"hello".encode()   # b'hello'

# format() → Formats string.
"My name is {}".format("Tom")   # "My name is Tom"

# format_map(dict) → Formats using dict.
"{name}".format_map({"name":"Tom"})   # "Tom"

# ------------------------------7. Utility------------------------------

# count(sub) → Returns number of occurrences.
"banana".count("a")   # 3

# expandtabs(n) → Sets tab size (default 8).
"a\tb".expandtabs(4)   # "a   b"

# casefold() → Aggressive lowercasing for comparisons.
"HELLO".casefold()   # "hello"