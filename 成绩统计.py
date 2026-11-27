# 实验六 任务2：成绩统计
# 要求输入 10 个成绩，按 -1 结束输入，
# 统计成绩中“优、良、中、及格和不及格”各等级的人数。
# 等级划分：优 90~100，良 80~89，中 70~79，及格 60~69，不及格 0~59。


def classify(score):
    """根据成绩返回对应的等级。"""
    if score >= 90:
        return "优"
    elif score >= 80:
        return "良"
    elif score >= 70:
        return "中"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def main():
    counts = {"优": 0, "良": 0, "中": 0, "及格": 0, "不及格": 0}
    total = 0

    print("请输入成绩（输入 -1 结束输入，最多 10 个）：")
    while total < 10:
        try:
            score = float(input(f"第 {total + 1} 个成绩："))
        except ValueError:
            print("输入无效，请输入数字！")
            continue

        if score == -1:          # 按 -1 提前结束输入
            break

        if score < 0 or score > 100:
            print("成绩应在 0~100 之间，请重新输入！")
            continue

        counts[classify(score)] += 1
        total += 1

    print(f"\n共录入 {total} 个成绩，统计结果如下：")
    for level, count in counts.items():
        print(f"{level}：{count} 人")


if __name__ == "__main__":
    main()
