

lst=[1,22,3,12,5,17,18,1,5,10,40,17,50,48,40,17]
evenlst=[]
for num in lst:
    if num%2==0:
        evenlst.append(num)
print(evenlst)
evenlst.sort(reverse=True)
print(evenlst)