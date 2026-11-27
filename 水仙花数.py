# 实验六 任务3：水仙花数
# 水仙花数（自幂数）：一个数等于其各位数字的 n 次幂之和，
# 其中 n 为该数的位数。例如 153 = 1^3 + 5^3 + 3^3。
# 求 10000 以内的水仙花数。


def is_narcissistic(number):
    """判断 number 是否为水仙花数（自幂数）。"""
    digits = [int(ch) for ch in str(number)]
    n = len(digits)
    return number == sum(d ** n for d in digits)


def main():
    # 从 10 开始，排除一位数这种平凡情况；一位数 1~9 按定义也满足 n=1 的条件
    result = [num for num in range(10, 10000) if is_narcissistic(num)]
    print("10000 以内的水仙花数有：")
    print(result)


if __name__ == "__main__":
    main()
