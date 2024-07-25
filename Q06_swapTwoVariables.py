# Using temporary variable
a=10
b=20

c=a
a=b
b=c
print(a," ",b)

# Without using 3rd variable
a=10
b=20

a=a+b
b=a-b
a=a-b
print(a," ",b)
