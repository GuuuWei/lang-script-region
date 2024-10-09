import re
strlist = "ء أ ؤ إ ئ ا آ ب ة ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ى ي ـ  ـ ‌ ‍ ‎ ‏ پ چ ژ ڜ ڢ ڤ ڥ ٯ ڧ ڨ ک گ ی   ◌ٰ ◌ٓ ◌ٔ ◌ٕ ◌ً ◌ٌ ◌ٍ ◌َ ◌ُ ◌ِ ◌ّ ◌ْ  ؜ ‎ - , ٫ ٬ . % ٪ ؉ + 0٠ 1 ١ 2 ٢ 3 ٣ 4 ٤ 5 ٥ 6 ٦ 7 ٧ 8 ٨ 9 ٩   - – — ۔ ، ؛ : ! ؟ ٭ . … \' \" « » ﴾ ﴿ ( ) [ ] ؍   ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي"


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
# 移除 9676 ◌
cache_list.remove(9676)

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
with open('uni.txt', 'w') as f:
    f.write(str(result))
