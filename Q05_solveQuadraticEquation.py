# Quardatic equation ---> ax**2 + bx + c = 0
# a,b and c are real numbers
# a!=0

# complex math
import cmath

a=4
b=2
c=6

# Discriminant
d=b**2-(4*a*c)
e=cmath.sqrt(d)

root1=(-b-e)/2*a
root2=(-b+e)/2*a

print(root1)
print(root2)

