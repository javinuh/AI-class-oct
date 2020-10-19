listlen = int(input("Enter list length"))
inplist=[]
for k in range(0,listlen):
    value=int(input("enter value index of "+str(k)+"="))
    inplist.append(value)
print(inplist)

for i in inplist:
    if i>0:
        print(i,',',end="")
print("")
