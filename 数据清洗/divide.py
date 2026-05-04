import pandas as pd
# 读取XLSX文件，并指定列名
df = pd.read_excel('weibo.xlsx', usecols=['label', 'review'])
# 打开输出文件
f1 = open('pos.txt', 'a+', encoding='utf-8')
f2 = open('neg.txt', 'a+', encoding='utf-8')
# 遍历数据框的每一行
for index, row in df.iterrows():
    # 检查label列的值是否为'1'或'0'
    sentiment = row['label']
    if sentiment == '1':
        # 写入pos.txt文件
        f1.write(row['review'] + '\n')
        num=num+1
    elif sentiment == '0':
        # 写入neg.txt文件
        f2.write(row['review'] + '\n')
    # 关闭文件
f1.close()
f2.close()