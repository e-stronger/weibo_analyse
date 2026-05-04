from snownlp import SnowNLP
import pandas as pd
import jieba
import matplotlib.pyplot as plt
# 读取停用词表
stopwords_file = '停用词表.txt'
with open(stopwords_file, 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())
# 读取 Excel 文件
df = pd.read_excel('胖猫（去重版）.xlsx')
# 获取评论列数据
comments = df.iloc[:, 4].tolist()
# comments = df.iloc[:, 2].tolist()# 假设评论数据从第二行开始，第三列是评论列
# 情感分析
sentiments = []
for comment in comments:
    # 清洗数据，分词处理并过滤停用词
    words = [word for word in jieba.cut(str(comment)) if word not in stopwords]
    cleaned_comment = ''.join(words)
    s = SnowNLP(cleaned_comment)
    sentiment = s.sentiments
    sentiments.append(sentiment)
# 绘制情感分布直方图
plt.hist(sentiments, bins=20, histtype='bar', rwidth=0.8)  # 使用圆括号，并指定bins参数
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
# plt.savefig('original_comment.png',dpi=600)
plt.show()  # 显示直方图
# 将情感分析结果添加到 DataFrame 中
df['Sentiment'] = sentiments
selected_columns = df.loc[:, ['user_id', '用户昵称', '微博正文','Sentiment']]
# selected_columns = df.loc[:, ['用户ID', '用户名', '评论内容','Sentiment']]
# 打印结果
selected_columns.to_excel('./博文情感分析（训练前）.xlsx')

