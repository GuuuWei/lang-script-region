strlist =    "- , . % + 0 1 2 3 4 5 6 7 8 9 〇 一 七 三 九 二 五 八 六 四"



# 去除空格
strlist = strlist.replace(' ', '')

# str 中的每个元素都是一个字符，将其转换为一个整数
cache_list = [ord(c) for c in strlist]

# 压缩
cache_list = list(set(cache_list))
# 排序
cache_list.sort()

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
            result.append([start ,end])
        start = cache_list[i]
        end = cache_list[i]
if start == end:
    result.append([start])
else:
    result.append([start ,end])
print(result)




# 存为txt文件
with open('uni.txt', 'w') as f:
    f.write(str(result))
