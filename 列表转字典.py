# 输入示例
lstA = list(map(int, input("输入列表 A，空格隔开：").split()))
lstB = list(map(int, input("输入列表 B，空格隔开：").split()))
n = min(len(lstA), len(lstB))
res_dict = {lstA[i]: lstB[i] for i in range(n)}
print(res_dict)
