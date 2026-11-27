# 任务(3)：输入一个字符串，输出其中出现次数最多的字符及其出现的次数。
# 要求使用字典。


def main():
    s = input("请输入一个字符串：")

    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    if not count:
        print("字符串为空，无法统计！")
        return

    # 按键取值最大者对应的字符；若有多个并列最多，取最先出现的那个
    max_ch = max(count, key=count.get)
    print(f"出现次数最多的字符是：'{max_ch}'，共出现 {count[max_ch]} 次")


if __name__ == "__main__":
    main()
