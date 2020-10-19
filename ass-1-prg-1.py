a=0
b=1
endvalue = int(input("Enter the end"))
print("fibnacci series")
print(a)
print(b)
for i in range(endvalue+1):
    c=a+b
    a=b
    b=c
    print(c)
    