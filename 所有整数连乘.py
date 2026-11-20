lst = list(map(int, input("输入整数列表：").split()))
prod = 1
for num in lst:
    prod *= num
print("连乘结果：", prod)
