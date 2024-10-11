
import pandas as pd

data = pd.read_csv('uni.txt', sep='\s+', header=None)

data.columns = ['Unicode','g'] 

# data Unicode 转换为list数组
cache_list = data.values.tolist()

print(cache_list)
# 合并相邻的数字为区间
result = []
# start end 读取作为数字类型

start = cache_list[0][0]
end = cache_list[0][0]


for i in range(1, len(cache_list)):
    if cache_list[i][0] - cache_list[i - 1][0] == 1:
        end = cache_list[i][0]
    else:
        if start == end:
            result.append([start])
        else:
            result.append([start ,end])
        start = cache_list[i][0]
        end = cache_list[i][0]
if start == end:
    result.append([start])
else:
    result.append([start ,end])
print(result)

# 存为txt文件
with open('uni_range.txt', 'w') as f:
    f.write(str(result))
