from snownlp import SnowNLP
import pandas as pd
import jieba

# 读取 Excel 文件
df = pd.read_excel('胖猫（去重版）.xlsx')

# 读取停用词表
stopwords_file = '停用词表.txt'
with open(stopwords_file, 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())
# 获取不同 IP 的评论列数据
target_ip=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','新疆','中国台湾','宁夏','澳门','香港']
# 获取所有评论和 IP 列数据
comments = df.iloc[:, 4].tolist()
ip_column = df.loc[:, 'ip'].tolist()
# 创建一个空的 DataFrame
result_df = pd.DataFrame(columns=['城市', '情感分析均值', '评论数'])
# 存储其他城市的评论
other_comments = []
# 遍历每个城市
for city in target_ip:
    selected_comments = []
    # 遍历评论和 IP 列数据
    for ip, comment in zip(ip_column, comments):
        if ip == city:
            selected_comments.append(comment)
        elif ip not in target_ip and comment not in other_comments:  # 如果 IP 不在目标列表中且不为空
            other_comments.append(comment)
    # 情感分析
    sentiments = []
    for comment in selected_comments:
        # 清洗数据，分词处理并过滤停用词
        words = [word for word in jieba.cut(str(comment)) if word not in stopwords]
        cleaned_comment = ''.join(words)
        s = SnowNLP(cleaned_comment)
        sentiment = s.sentiments
        sentiments.append(sentiment)
    # 计算情感分析结果的平均值
    if len(sentiments) == 0:
        average_sentiment = 0  # 如果没有评论，平均值设为0
    else:
        average_sentiment = sum(sentiments) / len(sentiments)
    # 将城市和情感分析均值添加到 DataFrame 中
    result_df = pd.concat([result_df, pd.DataFrame({'城市': [city], '情感分析均值': [average_sentiment], '评论数': [len(sentiments)]})], ignore_index=True)
# 计算其他城市的情感分析均值
sentiments_other = []
for comment in other_comments:
    # 清洗数据，分词处理并过滤停用词
    words = [word for word in jieba.cut(str(comment)) if word not in stopwords]
    cleaned_comment = ''.join(words)
    s = SnowNLP(cleaned_comment)
    sentiment = s.sentiments
    sentiments_other.append(sentiment)
# 计算其他城市情感分析结果的平均值
num=0
if len(sentiments_other) == 0:
    average_sentiment_other = 0  # 如果没有评论，平均值设为0，防止出现除以0的情况存在
else:
    average_sentiment_other = sum(sentiments_other) / len(sentiments_other)
# 将其他城市和情感分析均值添加到 DataFrame 中
result_df = pd.concat([result_df, pd.DataFrame({'城市': ['其他'], '情感分析均值': [average_sentiment_other], '评论数': [len(sentiments_other)]})], ignore_index=True)
# 打印结果
print(result_df)
