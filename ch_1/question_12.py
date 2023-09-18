# 方法一：采用牛顿迭代法

def cuberoot(n, epsilon=1e-6, max_iterations=100):
    guess = n / 3.0  # 初始猜测值，可以选择其他值
    for i in range(max_iterations):
        guess = guess - (guess ** 3 - n) / (3 * guess ** 2)
        if abs(guess ** 3 - n) < epsilon:
            return guess
    return guess

# 获取用户输入的数字
n = float(input("请输入一个数字: "))

# 调用cuberoot函数计算三次方根
result = cuberoot(n)

# 打印结果
print(f"{n}的三次方根为: {result}")

# 方法二：采用二分查找法

def cuberoot_binary_search(n, epsilon=1e-6, max_iterations=100):
    if n < 0:
        raise ValueError("输入的数必须大于等于0")

    low = 0.0
    high = max(n, 1.0)  # 初始化搜索范围，确保包含n
    guess = (low + high) / 2.0

    for i in range(max_iterations):
        guess_cubed = guess ** 3
        if abs(guess_cubed - n) < epsilon:
            return guess
        if guess_cubed < n:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0

    return guess

# 获取用户输入的数字
n = float(input("请输入一个非负数字: "))

# 调用cuberoot_binary_search函数计算三次方根
try:
    result = cuberoot_binary_search(n)
    print(f"{n}的三次方根为: {result}")
except ValueError as e:
    print(e)