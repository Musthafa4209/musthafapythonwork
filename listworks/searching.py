arr=[1,2,33,4,50,6,7,8,13,20,29,56,60]
arr.sort()
flag=0
element=13

low=0
upp=len(arr)-1
while(low<=upp):
    mid=(low+upp)//2
    if element==arr[mid]:
        flag=1
        break
    elif element>arr[mid]:
        low=mid+1
    elif element<arr[mid]:
        upp=mid-1
print("found" if flag>0 else "not found")

