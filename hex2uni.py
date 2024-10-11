import pandas as pd

data = pd.read_csv('hex.txt', sep='\s+', header=None)

data.columns = ['hex']
# 插入新一列
data.insert(1, 'Unicode', None)


for x in data.index:
    uni = data.loc[x, "hex"]
    data.loc[x, "Unicode"] = chr(int(uni, 16))



data = data.sort_values(by='Unicode')
data = data.reset_index(drop=True)


print(data)
# 保存data 到文件
data.to_csv('uni.txt',
            sep=' ', header=None, index=None)
