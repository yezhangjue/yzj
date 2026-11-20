# 坐标各两个整数
p1 = list(map(int, input("输入点 1 坐标 x y：").split()))
p2 = list(map(int, input("输入点 2 坐标 x y：").split()))
d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
print("曼哈顿距离：", d)
