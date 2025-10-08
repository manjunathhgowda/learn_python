def palin(str):
    return str==str[::-1]
print(palin("madam"))
print(palin("python"))

#To avoid casesensitive
def palin(str):
    return str.lower()==str[::-1].lower()
print(palin("maDaM"))
print(palin("python"))
