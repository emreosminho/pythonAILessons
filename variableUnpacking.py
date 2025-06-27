x, y = (4,7)
print(x)
print(y)

print("**************************")

x, y, z = (4,7,9)
print(x)
print(y)
print(z)

print("**************************")

x, _ = (4,8)
print(x)

print("**************************")

x, y, *z = (4,7,9,8,98)
print(z)
print(type(z))
