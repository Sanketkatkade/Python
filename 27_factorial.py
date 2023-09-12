num = int(input("Enter the number: "))
res = 1
if(num == 0):
    res = 1
else:
    for i in range(1,num+1):
        res *= i

print(res)