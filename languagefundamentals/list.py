# lst=[1,22,3,12,5,17,18,1,5,10,40,17,50,48,40,17]
# print(lst)


# element=22
# flag=0
# for num in lst:
#     if element==num:
#         flag=1
#         break
# print("element found" if flag!=0 else "element not found")


# evenlst=[]
# for num in lst:
#     if num%2==0:
#         evenlst.append(num)
# print(evenlst)
# evenlst.sort(reverse=True)
# print(evenlst)


# lst.insert(0,20)
# print(lst)
# print(lst.count(17))



lst1=[2,4,6,6,8,10,12,14,16,18]
lst2=[3,6,6,9,12,15,18]
samelst=[]

for num in lst1:
    if num in lst2:
        samelst.append(num)
print(set(samelst))


#most frequent number
#first recursive number



