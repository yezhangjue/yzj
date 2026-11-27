# 任务(4)：输入任意长的字符串，统计该字符串中所有字母和数字的频次，
# 并将结果以字典保存和输出。


def main():
    s = input("请输入字符串：")

    freq = {}
    for ch in s:
        if ch.isalpha() or ch.isdigit():    # 只统计字母和数字，忽略空格与符号
            freq[ch] = freq.get(ch, 0) + 1

    print("字母和数字的频次字典：", freq)


if __name__ == "__main__":
    main()
