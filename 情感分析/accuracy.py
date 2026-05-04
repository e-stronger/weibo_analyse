from snownlp import SnowNLP
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import jieba

stopwords_file = '停用词表.txt'
with open(stopwords_file, 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())

df = pd.read_excel('胖猫.xlsx')

df_sample = df.sample(n=100)

# comments = df_sample.iloc[0:, 4].tolist()
# # 初始化真实标签列表和预测标签列表
# y_true = [0 for i in range(100)]
# y_true.extend([1 for j in range(100)])
# y_pred = []
comments = df_sample.iloc[:, 4].tolist()  # 提取第四列的评论
# 从抽取的样本中提取真实标签
y_true = df_sample.iloc[:, 0].tolist()  # 假设第一列是真实标签
y_pred = []

for comment in comments:
    # 清洗数据，分词处理并过滤停用词
    words = [word for word in jieba.cut(str(comment)) if word not in stopwords]
    cleaned_comment = ''.join(words)
    s = SnowNLP(cleaned_comment)
    if s.sentiments>=0.5:
        y_pred.append(1)
    else:
        y_pred.append(0)

    # 绘制混淆矩阵
plt.subplots()
c2 = confusion_matrix(y_true, y_pred)
print(c2)
print(c2.ravel())

TN, FP, FN, TP = c2.ravel()[0], c2.ravel()[1], c2.ravel()[3], c2.ravel()[2]  # 注意这里的索引顺序，因为ravel()是按行优先展开的
print("Accuracy:", str(round((TP + TN) / (TP + TN + FN + FP), 2)))
print("Recall:", str(round(TP / (TP + FN), 2)))

# 绘制热力图
sns.heatmap(c2, annot=True, cmap='Blues')  # 使用'Blues'或其他你喜欢的颜色映射
plt.title("Sns_Heatmap_Confusion_Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.savefig("Sns_Heatmap_Confusion_Matrix.png", bbox_inches="tight", dpi=600)
plt.show()