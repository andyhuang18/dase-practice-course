# 6.写一个Python程序,有w,x,y,z 四个数,将这四个数从大到小使用 Print 函数打印出来

# 获取用户输入
w = float(input("请输入第一个数 w: "))
x = float(input("请输入第二个数 x: "))
y = float(input("请输入第三个数 y: "))
z = float(input("请输入第四个数 z: "))

# 使用sorted()函数排序，并使用reverse=True参数降序排序
sorted_numbers = sorted([w, x, y, z], reverse=True)

# 打印排序后的结果
print("从大到小排序后的结果为:", sorted_numbers)

# 请注意，这个程序假设用户输入的是有效的数字。
# 如果用户输入的不是数字，程序可能会引发异常。
# 你可以添加一些错误处理来处理这种情况，以使程序更健壮。