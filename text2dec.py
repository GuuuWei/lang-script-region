text = "㖭㗎㘭㧬㩒㷫个乪乸冚冧凪劏吓吖咓咗哋响哣唂唓唞唥唶唻啝啩啫啱啲喺喼嗌嗰嗱嘅嘢嘥嘭噃噉噏嚟嚡嚿埞壆媪嫲嬅孭尅尐怱愠慤戥抆拃担掟掹揞揦揸揼揾搣摷攞攰曱枱櫈氹滘烚燶珏琼甴畧疎睄瞓硤窰筲糉糭羗羣耷脷膶蔴衞裇譌跣踎躭軚輋迹鉢鍚鎅鑛閪韵餸麖麪鼈龢𠝹𠺢𠻹𠽌𡁵𡁻𡃁𢳂𣲷𨋢"

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