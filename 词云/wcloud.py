import pandas as pd
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取停用词表
stopwords_file = '停用词表.txt'
with open(stopwords_file, 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())

# 读取 Excel 文件
df = pd.read_excel('评论信息（去重版）.xlsx')
# comments = df.iloc[:, 2].tolist()# 假设评论数据从第二行开始，第三列是评论列
comments = df.iloc[:, 2].tolist()
# 清洗数据，分词处理
word_list = []
for comment in comments:
    comment = str(comment)  # 转换为字符串
    # 分词处理并过滤停用词
    words = [word for word in jieba.cut(comment) if word not in stopwords]
    word_list.extend(words)

# 统计词频
word_count = Counter(word_list)

# 生成词云
wordcloud = WordCloud(font_path='simhei.ttf').generate_from_frequencies(word_count)

# 显示词云图
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('comment_cy.png',dpi=600)
plt.show()