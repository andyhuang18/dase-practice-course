# 给定序列
L = [1, 2, 3, 4, 5]

# 使用for循环倒排序输出
reversed_list = []
for item in reversed(L):
    reversed_list.append(item)

print(reversed_list)

# 使用while循环倒排序输出
reversed_list = []
index = len(L) - 1
while index >= 0:
    reversed_list.append(L[index])
    index -= 1

print(reversed_list)