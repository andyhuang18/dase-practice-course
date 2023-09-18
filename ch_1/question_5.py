# 5.写一个 Python程序,输人x,y,z这三个数,将这三个数从小到大使用 Print 函数打印出来

# 获取用户输入
x = float(input("请输入第一个数 x: "))
y = float(input("请输入第二个数 y: "))
z = float(input("请输入第三个数 z: "))

# 使用sorted()函数排序
sorted_numbers = sorted([x, y, z])

# 打印排序后的结果
print("从小到大排序后的结果为:", sorted_numbers)