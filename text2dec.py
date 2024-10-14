text = "1234"

# str 中的每个元素都是一个字符，将其转换为一个整数
dec = [ord(c) for c in text]

# 压缩
dec = list(set(dec))
# 排序
dec.sort()

print(dec)
# 存为txt文件
with open('dec.txt', 'w') as f:
    for i in dec:
        f.write(str(i) + '\n')