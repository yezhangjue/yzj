# 任务(1)：输入包含若干集合的列表，输出这些集合的并集。
# 要求使用 reduce() 函数和 lambda 表达式完成。

from functools import reduce
import ast


def main():
    text = input("请输入包含若干集合的列表（示例：[{1, 2}, {2, 3}, {3, 4}]）：")
    sets_list = ast.literal_eval(text)

    # reduce() 配合 lambda：依次把前一个累积结果与下一个集合取并集（a | b）
    union = reduce(lambda a, b: a | b, sets_list, set())
    print("这些集合的并集为：", union)


if __name__ == "__main__":
    main()
