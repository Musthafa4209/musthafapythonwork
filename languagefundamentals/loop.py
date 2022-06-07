# while loop

# initialization
# while(condition)
#     loppbody
#     incr/decr



#print hello 5 times
# i=1
# while(i<=5):
#     print('hello')
#     i+=1



#print number in reverse order
# i=4
# while(i >= 1):
#         print(i)
#         i-=1


#factorial
# num=5
# i=1
# fact=1
# while(i<=num):
#         fact=fact*i
#         i=+1
# print(fact)



#sum of number upto a limit
# num=10
# sum=0
# i=1
# while(i<=10):
#        sum+=i
#        i+=1
# print(sum)



#reverse of number in line by line
# num=234
# while(num!=0):
#         last_digit=num%10
#         print(last_digit)
#         num=num//10



#reverse of number in a single line
# num=234
# res=""
# while(num!=0):             #123!=0,   12!=0   1!=0
#         last=num%10        #last=3,2,1
#         res=res+str(last)   #num=12 num=1 ,0
#         num=num//10
# print(res)



#question  2=>2+22 =>24
#          3=> 3+33+333+>
#       4=>4+44+444+4444
num=5
sum=0
total=0
i=1
while(i<=num):
        sum=(sum*10)+num
        i+=1
        total=total+sum
        print(sum)
print(total)