# num1=11
# num2=12
# num3=32
# if(num1>num2) & (num1>num3):
#     print(f"num1={num1} is largest")
# elif(num2>num1) & (num2>num3):
#     print(f"num2={num2} is largest")
# elif(num3>num1) & (num3>num2):
#     print(f"num3={num3} is largest")
# else:
#     print("all are same")

num1=10
num2=8
num3=9
if(num1>num2) and (num1>num3):
    if num2>num3:
        print(f"{num2} is 2nd largest")
    else:
        print(f"{num3} is 2nd largest")
elif(num2>num1) and (num2>num3):
    if num1>num3:
        print(f"{num1} is 2nd largest")
    else:
        print(f"{num3} is 2nd largest")
elif(num3>num1) and (num3>num2):
        if(num1 > num2):
            print(f"{num1} is 2nd largest")
        else:
            print(f"{num2} is 2nd largest")




