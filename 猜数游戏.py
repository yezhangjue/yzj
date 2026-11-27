# 实验六 任务1：猜数游戏
# 程序在指定范围内生成一个随机数，提示用户进行猜测，并根据输入给出提示：
# 猜对了 / 太大了 / 太小了；猜对则提前结束程序；
# 如果猜测次数用完仍没有猜中，提示游戏结束并给出正确答案。

import random


def main():
    lower, upper = 1, 100      # 指定猜测的范围
    max_times = 7             # 最多允许猜测的次数
    answer = random.randint(lower, upper)

    print(f"猜数游戏：请猜一个 {lower}~{upper} 之间的整数，共有 {max_times} 次机会。")

    for times in range(1, max_times + 1):
        try:
            guess = int(input(f"第 {times} 次猜测："))
        except ValueError:
            print("输入无效，请输入一个整数！")
            continue
        except EOFError:
            print("\n输入结束，游戏终止。")
            return

        if guess == answer:
            print(f"猜对了！答案就是 {answer}，恭喜你！")
            return
        elif guess > answer:
            print("太大了！")
        else:
            print("太小了！")

    # 次数用完仍未猜中
    print(f"游戏结束！正确答案是 {answer}，下次再接再厉。")


if __name__ == "__main__":
    main()
