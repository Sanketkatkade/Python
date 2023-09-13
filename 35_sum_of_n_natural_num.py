def sumOfnNaturalnum(num):
    if num == 0:
        return 0
    return num + sumOfnNaturalnum(num-1)
f = sumOfnNaturalnum(10)
print(f)