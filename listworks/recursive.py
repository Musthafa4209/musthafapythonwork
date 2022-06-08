lst=[2,4,6,8,10,12,14,16,18,3,6,9,12,15,18,18,18,18]
dup_list=[]

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j]:
            dup_list.append(lst[i])
print(dup_list)