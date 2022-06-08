
lst1=[2,4,6,6,8,10,12,14,16,18]
lst2=[3,6,6,9,12,15,18]
samelst=[]
for num in lst1:
    if num in lst2:
        samelst.append(num)
print(set(samelst))