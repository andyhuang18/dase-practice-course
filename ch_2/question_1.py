#  1.给定一个正整数n,找出一个正整数列表,它们的乘积是所有和为 n 的正整数列表中最大的。
#    例如,如果 n 为 4,那么要求的正整数列就是 2,2,因为 2X2 的结果比1X1X1X1、2X1X1以及3X1 的结果都要大。
#    再比如,如果n 为 5,那么所求的正整数列就是 2,3。

def max_product_partition(n):
    # 创建一个列表来存储以每个i为和的最大乘积
    max_product = [0] * (n + 1)
    
    # 创建一个列表来存储生成最大乘积的正整数列表
    max_product_list = [[] for _ in range(n + 1)]
    
    # 初始条件
    max_product[1] = 1
    max_product_list[1] = [1]
    
    # 计算每个i的最大乘积
    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            # 计算以i为和的最大乘积，将其与当前最大值比较
            product = max(j * max_product[i - j], j * (i - j))
            if product > max_product[i]:
                max_product[i] = product
                max_product_list[i] = max_product_list[i - j] + [j]

    return max_product[n], max_product_list[n]

# 输入正整数n
n = int(input("请输入正整数n："))
result, integer_list = max_product_partition(n)
print(f"最大乘积为：{result}")
print(f"正整数列表为：{integer_list}")