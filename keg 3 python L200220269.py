Nama = "Muhammad Aksal Pratama
NIM = "L200220269"
x = '1' + NIM[7:]
a = int(x)
b = len(Nama)

print(type(a))
# a merupakan type integer
print(type(b))
# b merupakan type integer
print(a/b)
# menghasilkan output 57,68
print(a//b)
# menghasilkan output 58
print(10*(a-999))
# menghasilkan output 2700
print(b**2)
# menghasilkan output 484
print(a%b)
# menghasilkan output 15

c = 12.5

print(type(c))
# c merupakan type float
print(a/c)
# menghasilkan output 101,52
print(a//c)
# menghasilkan output 102
print(a%c)
# menghasilkan output 6,5

print(c>b)
# menghasilkan output False
print(type(c>b))
# merupakan type boolean
print(a>b and b>c)
# menghasilkan output True
print(a>1100 or b<10)
# menghasilkan output True
