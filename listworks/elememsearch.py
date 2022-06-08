lst=[1,22,3,12,5,17,18,1,5,10,40,17,50,48,40,17]
print(lst)


element=22
flag=0
for num in lst:
    if element==num:
        flag=1
        break
print("element found" if flag!=0 else "element not found")