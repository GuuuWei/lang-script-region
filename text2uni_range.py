import re
strlist = "1231"


ss = [x[0] or x[1] for x in re.findall(r"\{([^}]+)\}|(\S+)", strlist)]
print(ss)

# 去除空格
strlist = strlist.replace(' ', '')

# str 中的每个元素都是一个字符，将其转换为一个整数
cache_list = [ord(c) for c in strlist]

# 压缩
cache_list = list(set(cache_list))
# 排序
cache_list.sort()

remove_list = [123, 125, 9676]
for i in remove_list:
    if i in cache_list:
        cache_list.remove(i)

result = []
start = cache_list[0]
end = cache_list[0]
for i in range(1, len(cache_list)):
    if cache_list[i] - cache_list[i - 1] == 1:
        end = cache_list[i]
    else:
        if start == end:
            result.append([start])
        else:
            result.append([start, end])
        start = cache_list[i]
        end = cache_list[i]
if start == end:
    result.append([start])
else:
    result.append([start, end])
print(result)


# 存为txt文件
with open('uni_range.txt', 'w') as f:
    f.write(str(result))
