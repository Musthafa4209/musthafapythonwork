# lst=[2,3,4,6]
# sum=8
# count=1
# for i in range(len(lst)):
#     for j in range((i+1),len(lst)):
#         curr_sum=lst[i]+lst[j]
#         if curr_sum==sum:
#             print(f"pairs{lst[i]},{lst[j]}")
#             break
#         count+=1  #to check number of iteration
# print(count)



lst=[2,4,3,6,5]
lst.sort()
print(lst)
sum=8
low=0
upp=len(lst)-1
while(low<upp):
    curr_sum = lst[low] + lst[upp]

    if curr_sum==sum:
        print(f"pairs {lst[low]},{lst[upp]}")
        low+=1
    elif curr_sum>sum:
        upp-=1
    elif curr_sum<sum:
        low+=1



