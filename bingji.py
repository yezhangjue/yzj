from functools import reduce
lst = eval(input("输入集合列表"))
res = reduce(lambda s1,s2: s1.union(s2),lst)
print("并集结果 :",res)