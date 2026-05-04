import time
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def get_weibo_hot_search():
    url = 'https://s.weibo.com/top/summary'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        ,'Cookie':'SUB=_2AkMRW1y5f8NxqwFRmfsUz2vlbol2ywHEieKnB61iJRMxHRl-yT8XqmkttRB6OttyVoxFubwQmglPJrJGv-VVTHpPMFrU; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5TVC7YPLUs7.xPR_lbwqsE; SINAGLOBAL=1682531805692.4443.1711788932174; _s_tentry=-; Apache=1279932814886.0933.1711877254279; ULV=1711877254288:4:4:3:1279932814886.0933.1711877254279:1711872860859'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('请求失败:', response.status_code)
        return None
    # print(response.content.decode("utf-8"))
    soup = BeautifulSoup(response.text, 'html.parser')
    hot_search_items = soup.select('.td-02 > a')[:50]  # 获取前50条热搜榜名称
    # print(hot_search_items)
    hot_search_data = []
    for item in hot_search_items:
        hot_search_name = item.text.strip()
        hot_search_link = item.get('href')  # 获取链接
        # 查找热度值，它紧跟在热搜名称的<a>标签后面
        hot_score_span = item.find_next('span')  # 使用find_next找到下一个<span>标签
        if hot_score_span:
            hot_score = hot_score_span.text.strip()  # 获取热度值并去除两端的空白字符
        else:
            hot_score = '未知'  # 如果没有找到热度值，则标记为'未知'
        hot_search_data.append({
            'rank': hot_search_items.index(item) + 1,
            'name': hot_search_name,
            'link': hot_search_link,
            'hot_score': hot_score
        })
        # print(item)
    return hot_search_data
def send_email(subject, body, recipient):
    # 邮件配置信息
    sender = '2653210085@qq.com'
    password = 'ujwefiffianzdiib'  #使用的是授权码不是密码
    smtp_server = 'smtp.qq.com'
    smtp_port = 465#smtp端口号
    # 创建邮件内容
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    try:
        # 使用SMTP_SSL进行SSL加密连接（非常重要）
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender, password)
        server.sendmail(sender, recipient, message.as_string())
        print('邮件发送成功')
    except Exception as e:
        print('邮件发送失败', str(e))
    finally:
        if 'server' in locals() and server:
            server.quit()
if __name__ == '__main__':
    recipient_email = 'rhtc584@163.com'  # 收件人邮箱
    interval = 20  # 发送邮件的时间间隔，单位为秒
    num = 0
    while True:
        if num >= 5:
            break
        try:
            hot_search_data = get_weibo_hot_search()
            if hot_search_data:
                subject = '微博热搜榜前50条'
                body = '\n'.join([f"排名: {item['rank']}, 名称: {item['name']}, 链接: {item['link']},热度: {item['hot_score']}" for item in hot_search_data])
                send_email(subject,body,recipient_email)
            else:
                print("未获取到微博热搜榜数据")
            num = num + 1
            time.sleep(interval)
        except Exception as e:
            print("发生错误:", e)