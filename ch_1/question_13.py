def factorial(n):
    if n < 0:
        return "阶乘只定义在非负整数上"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# 获取用户输入的常数n
n = int(input("请输入一个非负整数 n: "))

# 调用factorial函数计算阶乘
result = factorial(n)

# 打印结果
print(f"{n}的阶乘为: {result}")