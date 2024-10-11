import pandas as pd

data = pd.read_csv('dec.txt', sep='\s+', header=None)

data.columns = ['dec']
# 插入新一列
data.insert(1, 'Unicode', None)


for x in data.index:
    uni = hex(data.loc[x, "dec"])
    data.loc[x, "dec"] = uni
    data.loc[x, "Unicode"] = chr(int(uni, 16))
    data.loc[x, "dec"] = data.loc[x, "dec"].replace('0x', '')



data = data.sort_values(by='Unicode')
data = data.reset_index(drop=True)


print(data)
# 保存data 到文件
data.to_csv('uni.txt',
            sep=' ', header=None, index=None)
