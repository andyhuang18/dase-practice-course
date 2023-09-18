# 打印星星
def print_stars():
    for _ in range(10):
        print(chr(0x2605), end=' ')
    print()

# 打印文本和星星
def print_text_with_stars(text):
    print_stars()
    print(text)
    print_stars()

# 主程序
if __name__ == "__main__":
    text = "数据科学与工程导论"
    print_text_with_stars(text)
