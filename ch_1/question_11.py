# 11.写一个 Python程序,输人一个字符串 S,去掉其中所有的空格后输出。
#    例如，DataScience and Engineering”,去掉空格后为“DataScienceandEngineering

# 获取用户输入的字符串
input_string = input("请输入一个字符串: ")

# 使用replace()方法去掉空格
result_string = input_string.replace(" ", "")

# 打印去掉空格后的字符串
print("去掉空格后的字符串:", result_string)