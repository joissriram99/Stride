dic = {}
n = int(input("enter the value of n : "))


if n==0:
    raise Exception('n should not be zero. The value of x was: {}'.format(n))

for i in range(1, n + 1):
    dic[i] = i * i
print(dic)

