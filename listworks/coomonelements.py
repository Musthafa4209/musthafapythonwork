arr1=[2,4,6,8,10,12]
arr2=[3,6,9,12,15,18]
count=0
p1=0
p2=0
arr1.sort()
arr2.sort()

while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(f"common element found: {arr1[p1]}")
        p1+=1
        p2+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
    count+=1
print(count)