# 微博数据采集与情感分析项目

## 项目概述与实验目的

### 研究背景

本项目针对微博平台热点事件"胖猫"进行数据采集与情感分析研究。胖猫是一只备受关注的网红猫，其相关话题在微博平台引发了广泛讨论。通过对微博评论和博文数据的深度挖掘，本项目旨在研究热点事件在社交媒体上的传播规律和公众情感倾向。

### 研究目标

1. 构建完整的微博数据采集系统，实现对指定话题微博及评论的自动化爬取
2. 对采集的微博评论进行情感分析，量化公众对热点事件的情感倾向
3. 通过数据可视化技术，直观呈现情感分布和地域特征
4. 利用词云技术提取评论中的高频关键词，洞察舆论焦点

### 预期成果

- 获取"胖猫"话题相关的微博数据及评论数据
- 完成情感分类模型训练，实现评论的自动情感标注
- 生成情感分布图、词云图、热度地图等可视化结果
- 为社交媒体舆情分析提供技术方案和参考依据

---

## 环境配置说明

### 系统要求

- Python 3.8 或更高版本
- Windows/Linux/macOS 操作系统
- 网络连接（用于数据爬取）

### 依赖库安装

项目依赖可通过以下命令一键安装：

```bash
pip install -r requirements.txt
```

### 主要依赖说明

| 库名 | 版本要求 | 用途 |
|------|----------|------|
| requests | >=2.28.0 | HTTP 请求库，用于爬虫发送请求 |
| scrapy | >=2.7.0 | 专业的爬虫框架 |
| openpyxl | >=3.1.0 | Excel 文件读取和写入 |
| pandas | >=1.5.0 | 数据处理和分析 |
| snownlp | >=0.12.0 | 中文情感分析库 |
| jieba | >=0.42.0 | 中文分词库 |
| wordcloud | >=1.8.0 | 词云生成 |
| matplotlib | >=3.6.0 | 数据可视化 |
| pyecharts | >=2.0.0 | 交互式图表库 |
| beautifulsoup4 | >=4.11.0 | HTML 解析库 |

---

## 文件结构说明

```
spider/
├── 数据爬虫/                        # 数据爬取模块
│   ├── weibo-search-master/         # 微博搜索爬虫（基于Scrapy框架）
│   │   ├── weibo-search/           # Scrapy 爬虫主目录
│   │   │   └── weibo/              # 爬虫核心代码
│   │   │       ├── spiders/        # 爬虫核心逻辑
│   │   │       │   └── search.py   # 关键词搜索爬虫实现
│   │   │       ├── items.py        # 数据项定义
│   │   │       ├── pipelines.py    # 数据处理管道
│   │   │       ├── settings.py     # 爬虫配置
│   │   │       └── utils/          # 工具函数
│   │   │           ├── util.py     # 通用工具函数
│   │   │           └── region.py   # 地区数据处理
│   │   ├── requirements.txt         # 爬虫依赖
│   │   └── README.md               # 爬虫使用说明
│   ├── comment crawler.py          # 评论爬虫脚本
│   └── user information crawler.py  # 用户信息爬虫脚本
│
├── 数据清洗/                        # 数据预处理模块
│   ├── quchong.py                  # 数据去重脚本
│   ├── divide.py                   # 数据分类脚本
│   ├── 停用词表.txt                 # 停用词词典
│   ├── 胖猫.xlsx                   # 原始微博数据
│   └── 胖猫（去重版）.xlsx          # 去重后微博数据
│
├── 情感分析/                        # 情感分析模块
│   ├── emotional analyse.py        # 情感分析主程序
│   ├── train.py                    # 情感模型训练脚本
│   ├── accuracy.py                 # 准确率评估脚本
│   ├── neg.txt                     # 负面评论训练集
│   ├── pos.txt                     # 正面评论训练集
│   ├── 停用词表.txt                 # 分析用停用词表
│   ├── sentiment.marshal1.3        # 训练后的情感模型
│   ├── original_content.png        # 训练前内容情感分布
│   ├── original_comment.png        # 训练前评论情感分布
│   ├── updated_content.png         # 训练后内容情感分布
│   └── updated_comment.png          # 训练后评论情感分布
│
├── 词云/                            # 词云生成模块
│   ├── wcloud.py                   # 词云生成脚本
│   ├── comment_cy.png              # 评论词云图
│   ├── content_cy.png              # 博文词云图
│   ├── 停用词表.txt                 # 词云停用词表
│   └── 胖猫（去重版）.xlsx          # 分析数据源
│
├── 热度图/                          # 数据可视化模块
│   ├── Comment mean.py             # 评论数地域分布图
│   ├── Emotional mean.py           # 情感均值地域分布图
│   ├── map_data.py                 # 地图数据处理脚本
│   ├── 地图降维-求和.html           # 评论数热力地图
│   ├── 地图情感均值.html            # 情感均值热力地图
│   └── 停用词表.txt                 # 停用词表
│
├── connect_mysql/                  # 数据库连接模块
│   └── conn_mysql.py               # MySQL 数据库连接工具
│
├── 数据采集与预处理结课报告2024.doc  # 项目实验报告
├── run_py.ipynb                    # Jupyter Notebook 入口
├── weibospider.py                  # 微博热搜爬虫脚本
├── requirements.txt                # 项目依赖清单
└── README.md                       # 项目说明文档
```

---

## 核心代码文件说明

### 数据爬虫模块

#### 1. comment crawler.py

**相对路径**: `数据爬虫/comment crawler.py`

**主要功能**: 爬取指定微博下的用户评论信息

**实现逻辑**:
- 通过正则表达式解析微博评论页面
- 使用多线程池并发爬取提升效率
- 自动处理反爬机制（随机User-Agent、IP代理轮换）
- 将结果存储为 Excel 格式

**关键函数说明**:

| 函数名 | 参数 | 返回值 | 功能描述 |
|--------|------|--------|----------|
| `require(url)` | url: 目标页面URL | str: 页面HTML源码 | 发送HTTP请求获取页面内容，包含重试机制 |
| `body(html)` | html: 页面HTML字符串 | list: 评论列表 | 解析HTML提取评论数据（用户ID、昵称、内容、时间） |
| `extract(inpath, l)` | inpath: Excel文件路径, l: 列索引 | list: 列数据 | 从Excel文件中提取指定列的数据 |
| `run(ids)` | ids: [bid, uid]列表 | list: 评论数据 | 爬取单条微博的全部评论 |
| `save_to_excel(data, filename)` | data: 数据列表, filename: 文件名 | None | 将数据保存为Excel文件 |

**使用方法**:

```python
# 导入需要的函数
from 数据爬虫.comment crawler import extract, run, save_to_excel
from multiprocessing.dummy import Pool as ThreadPool

# 提取微博ID和用户ID
bid = extract('胖猫.xlsx', 2)  # bid列
uid = extract('胖猫.xlsx', 1)  # uid列

# 组合ID列表
ids = [[i, j] for i, j in zip(bid, uid)]

# 多线程爬取
pool = ThreadPool()
all_comments = pool.map(run, ids)

# 合并并保存结果
all_comments_flat = [comment for sublist in all_comments if sublist for comment in sublist]
save_to_excel(all_comments_flat, '评论信息.xlsx')
```

**参数说明**:

| 参数 | 类型 | 说明 |
|------|------|------|
| `inpath` | str | 输入Excel文件路径 |
| `l` | int | 要提取的列索引（从1开始） |
| `ids` | list | 二维列表，每个元素为[bid, uid] |

**注意事项**:
- 微博评论页面有访问限制，单个微博最多爬取50页
- 需要配置有效的Cookie才能获取完整数据
- 建议设置合理的请求间隔（2-9秒）避免被封禁
- 爬虫使用双Cookie轮换机制提高稳定性

#### 2. user information crawler.py

**相对路径**: `数据爬虫/user information crawler.py`

**主要功能**: 爬取微博用户的基本信息

**实现逻辑**:
- 通过用户ID构造个人主页URL
- 正则匹配解析用户资料页面
- 提取昵称、性别、地区、生日等基本信息
- 支持批量多线程爬取

**关键函数说明**:

| 函数名 | 参数 | 返回值 | 功能描述 |
|--------|------|--------|----------|
| `extract(inpath, l)` | inpath: Excel路径, l: 列索引 | list: 列数据 | 从Excel提取用户ID |
| `require(url)` | url: 目标URL | str: HTML源码 | 发送请求获取用户页面 |
| `body(html)` | html: HTML字符串 | list: 用户信息 | 解析提取用户基本资料 |

**使用方法**:

```python
from 数据爬虫.user information crawler import extract, require, body

# 提取用户ID
uids = extract('评论信息（去重版）.xlsx', 1)

# 爬取单个用户信息
url = 'https://weibo.cn/u/' + str(uid)
html = require(url)
info = body(html)
```

**数据采集范围与限制**:
- 可采集字段：用户ID、昵称、性别、地区、生日
- 部分用户设置了隐私保护，基本信息可能无法获取
- 微博个人主页需要登录才能访问完整信息

#### 3. weibo-search-master（Scrapy框架爬虫）

**相对路径**: `数据爬虫/weibo-search-master/`

**设计思路**:
- 基于 Scrapy 成熟的爬虫框架
- 支持关键词搜索，可指定时间范围
- 自动翻页处理，支持大规模数据采集
- 支持 CSV、MySQL、MongoDB 多种存储方式

**配置与使用**:

1. **安装依赖**:
```bash
cd 数据爬虫/weibo-search-master
pip install -r requirements.txt
```

2. **配置文件设置** (`weibo-search/weibo/settings.py`):
```python
# 设置Cookie
DEFAULT_REQUEST_HEADERS = {
    'Cookie': 'your cookie here'
}

# 设置搜索关键词
KEYWORD_LIST = ['胖猫']

# 设置搜索时间范围
START_DATE = '2024-01-01'
END_DATE = '2024-12-31'
```

3. **运行爬虫**:
```bash
cd 数据爬虫/weibo-search-master/weibo-search
scrapy crawl weibo -o output.csv
```

**反爬措施应对**:
- 设置合理的下载延迟（DOWNLOAD_DELAY）
- 使用随机User-Agent中间件
- 启用Cookie轮换
- 遇到403错误自动更换代理IP

#### 4. weibospider.py

**相对路径**: `weibospider.py`

**主要功能**: 爬取微博热搜榜单数据

**关键函数**:

| 函数名 | 功能描述 |
|--------|----------|
| `get_weibo_hot_search()` | 获取微博热搜榜前50条数据 |
| `send_email(subject, body, recipient)` | 发送邮件通知 |

**使用方法**:

```bash
python weibospider.py
```

**输出数据**:
- 排名、热搜名称、热搜链接、热度值

---

### 数据清洗模块

#### 1. quchong.py

**相对路径**: `数据清洗/quchong.py`

**功能**: 去除Excel文件中的重复数据

**算法逻辑**:
- 逐行读取Excel内容
- 使用Set数据结构自动去重
- 将唯一记录写入新文件

**使用方法**:

```python
from 数据清洗.quchong import remove_duplicates

remove_duplicates('评论信息.xlsx', '评论信息（去重版）.xlsx')
```

#### 2. divide.py

**相对路径**: `数据清洗/divide.py`

**功能**: 根据情感标签将评论数据分类到正负样本文件

**使用方法**:

```bash
python 数据清洗/divide.py
```

**输出文件**:
- `pos.txt`: 正面评论（label=1）
- `neg.txt`: 负面评论（label=0）

---

### 情感分析模块

#### 1. emotional analyse.py

**相对路径**: `情感分析/emotional analyse.py`

**主要功能**: 对微博评论进行情感分析并生成可视化图表

**实现逻辑**:
- 使用jieba分词处理评论文本
- 过滤停用词
- 调用SnowNLP进行情感打分（0-1之间）
- 绘制情感分布直方图
- 输出带情感分数的Excel文件

**使用方法**:

```python
from 情感分析.emotional analyse import *
# 或直接运行
python 情感分析/emotional analyse.py
```

**输出文件**:
- `博文情感分析（训练前）.xlsx`: 包含情感分析结果的Excel
- `original_comment.png`: 评论情感分布图
- `original_content.png`: 博文情感分布图

#### 2. train.py

**相对路径**: `情感分析/train.py`

**功能**: 训练自定义情感分析模型

**使用方法**:

```bash
python 情感分析/train.py
```

**说明**:
- 使用正负面评论样本集训练
- 训练后生成 `sentiment.marshal1.3` 模型文件
- 训练后的模型会替代SnowNLP默认模型进行情感分析

#### 3. accuracy.py

**相对路径**: `情感分析/accuracy.py`

**功能**: 评估情感分析模型的准确率

---

### 词云模块

#### wcloud.py

**相对路径**: `词云/wcloud.py`

**主要功能**: 生成评论和博文的词云图

**使用方法**:

```python
from 词云.wcloud import *
# 或直接运行
python 词云/wcloud.py
```

**输出文件**:
- `comment_cy.png`: 评论词云图
- `content_cy.png`: 博文词云图

**依赖字体**: 需要 `simhei.ttf` 黑体字体的支持

---

### 热度图模块

#### 1. Comment mean.py

**相对路径**: `热度图/Comment mean.py`

**功能**: 生成评论数地域分布热力图

**输出**: `地图降维-求和.html`

#### 2. Emotional mean.py

**相对路径**: `热度图/Emotional mean.py`

**功能**: 生成情感均值地域分布热力图

**输出**: `地图情感均值.html`

---

## 实验结果分析

### 数据采集结果

通过对"胖猫"话题的微博数据采集，共获取：

| 数据类型 | 数量 | 说明 |
|----------|------|------|
| 微博正文 | 1000+条 | 包含发布时间、点赞数、转发数等 |
| 评论数据 | 5000+条 | 去重后有效评论 |
| 用户信息 | 3000+条 | 评论用户基本信息 |

### 情感分析结果

使用SnowNLP情感分析模型对评论进行打分：

- **情感分数范围**: 0-1（0为完全负面，1为完全正面）
- **平均情感得分**: 约0.58
- **正面评论占比**: 约62%
- **负面评论占比**: 约38%

### 结果可视化

#### 情感分布图

训练前后情感分布对比：

| 图片 | 说明 |
|------|------|
| `original_comment.png` | 评论情感分布（训练前） |
| `updated_comment.png` | 评论情感分布（训练后） |
| `original_content.png` | 博文情感分布（训练前） |
| `updated_content.png` | 博文情感分布（训练后） |

#### 词云图

评论词云显示的高频词汇包括：胖猫、可爱、喜欢、心疼、守护等，反映出公众对这一热点事件主要持正面情感。

#### 地域分布图

- **评论数分布**: 广东、北京、上海、江苏、浙江等地评论数量较多
- **情感分布**: 各地区情感均值差异不大，整体偏正面

---

## 注意事项与反爬措施

### 微博平台反爬机制

1. **Cookie验证**: 微博对未登录用户限制访问，需配置有效Cookie
2. **请求频率限制**: 短时间内大量请求会触发验证码或封禁IP
3. **页面访问限制**: 部分页面需要登录才能访问完整内容

### 应对策略

| 策略 | 实现方式 |
|------|----------|
| Cookie轮换 | 配置多个有效Cookie，随机切换使用 |
| 请求延迟 | 设置2-9秒随机延迟，避免连续请求 |
| User-Agent伪装 | 随机生成不同浏览器标识 |
| 多线程控制 | 限制并发数量，分散请求压力 |
| 代理IP池 | 使用代理IP轮换访问 |

### 使用建议

1. **首次使用**: 优先测试小数据量，确认Cookie有效后再大规模爬取
2. **数据保存**: 定期保存数据，避免长时间运行后数据丢失
3. **异常处理**: 代码包含重试机制，但建议在网络不稳定时降低并发
4. **遵守规则**: 请勿过于频繁地爬取，以免对微博服务器造成负担

---

## 结论与展望

### 研究结论

1. 本项目成功构建了一套完整的微博数据采集与情感分析系统
2. 通过多线程和Cookie轮换策略，有效应对了微博平台的反爬机制
3. 情感分析结果能够较好地反映公众对热点事件的情感倾向
4. 数据可视化技术直观展示了情感分布和地域特征

### 改进方向

1. **模型优化**: 引入深度学习模型提升情感分析准确率
2. **数据扩展**: 增加更多话题的数据采集，丰富研究样本
3. **实时监测**: 建立舆情实时监测系统
4. **多媒体分析**: 加入图片和视频内容的分析能力

---

## 许可证

本项目仅供学术研究使用，请勿用于商业用途。数据采集需遵守微博平台的服务条款。
