def has_consecutive_duplicate(s):
    consecutive_count = 1  # 用于记录连续相同字符的计数
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            consecutive_count += 1
            if consecutive_count >= 2:
                return True
        else:
            consecutive_count = 1  # 重置计数

    return False

# 获取用户输入的字符串
input_string = input("请输入一个字符串: ")

# 调用函数检查是否包含连续相同字符
if has_consecutive_duplicate(input_string):
    print("输入的字符串包含由两个或两个以上连续出现的相同字符组成的字符串。")
else:
    print("输入的字符串不包含由两个或两个以上连续出现的相同字符组成的字符串。")