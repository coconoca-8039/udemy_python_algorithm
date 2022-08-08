#メールの送信に必要なライブラリ
import datetime
import smtplib
import ssl
from email.mime.text import MIMEText
#import sys,codecs
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import feedparser
import requests
from bs4 import BeautifulSoup

#######################################################################

#今日と明日の最高気温
#tenki.jp
def get_forecast(url_forecast):
    
    #グローバル宣言
    global today_high_temp
    global today_low_temp
    today_rain = []
    tomorrow_rain = []
    
    url = url_forecast
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    today_forecast = soup.find('div',attrs={'class':'forecast-days-wrap'})

    #今日の最高気温
    high_temp = today_forecast.find_all('dd',attrs={'class':'high-temp'})[0]
    today_high_temp = int(high_temp.text.replace('℃',''))
    #明日の最高気温
    high_temp = today_forecast.find_all('dd',attrs={'class':'high-temp'})[2]
    tomorrow_high_temp = int(high_temp.text.replace('℃',''))

    #今日の最低気温
    low_temp = today_forecast.find_all('dd',attrs={'class':'low-temp'})[0]
    today_low_temp = int(low_temp.text.replace('℃',''))
    #明日の最低気温
    low_temp = today_forecast.find_all('dd',attrs={'class':'low-temp'})[2]
    tomorrow_low_temp = int(low_temp.text.replace('℃',''))

    print('今日の最高気温：',today_high_temp)
    print('今日の最低気温：',today_low_temp)
    print('明日の最高気温：',tomorrow_high_temp)
    print('明日の最低気温：',tomorrow_low_temp)

    #６時間毎の降水確率
    #print(today_forecast.prettify())
    rain_probability = today_forecast.find_all('td')
    #ループの変数
    i = [0,1,2,3,4]
    j = [5,6,7,8,9]
    
    #ループの変数
    i = [0,1,2,3,4]
    j = [5,6,7,8,9]

    #今日の降水確率
    for x in i:
        rain_probability = today_forecast.find_all('td')[x]
        rain_probability = rain_probability.text
        today_rain.append(rain_probability)

    #明日の降水確率
    for x in j:
        rain_probability = today_forecast.find_all('td')[x]
        rain_probability = rain_probability.text
        tomorrow_rain.append(rain_probability)

    print("今日の降水確率",today_rain)
    print("明日の降水確率",tomorrow_rain)
    
    #グローバル宣言
    global rain0006 
    global rain0612 
    global rain1218 
    global rain1824
    global today_wind
    
    rain0006 = today_rain[0]
    rain0612 = today_rain[1]
    rain1218 = today_rain[2]
    rain1824 = today_rain[3]
    today_wind = today_rain[4]

#######################################################################

#紫外線の取得
#higashine_uv = "https://tenki.jp/indexes/uv_index_ranking/2/9/3510/6211/"
#get_uv(higashine_uv)
def get_uv(url_uv):
    
    #グローバル宣言
    global today_uv_comment
    global today_uv_summary
    
    url = url_uv
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    today_uv = soup.find_all('div',attrs={'class':'clearfix'})[1]
    #print(today_uv)

    today_uv_comment = today_uv.find_all('p',attrs={'class':'indexes-telop-1'})
    today_uv_comment = str(today_uv_comment)
    today_uv_comment = today_uv_comment.replace('<p class="indexes-telop-1">','')
    today_uv_comment = today_uv_comment.replace('</p','')
    print(today_uv_comment)

    today_uv_summary = today_uv.find_all('span',attrs={'class':'indexes-telop-0'})
    today_uv_summary = str(today_uv_summary)
    today_uv_summary = today_uv_summary.replace('<span class="indexes-telop-0">','')
    today_uv_summary = today_uv_summary.replace('</span>','')
    print(today_uv_summary)

#######################################################################

jma_news = feedparser.parse("https://news.yahoo.co.jp/rss/media/tenki/all.xml")
print(jma_news['feed']['title'])
i = 1

for article in jma_news['entries']:
    #print(i,"件目")
    #print(f' タイトル:{article.get("title")}')
    #print(f' リンク:{article.get("link")}')
    #print(f' 日付:{article.get("published")}')
    #print(f' 概要:{article.get("summary")}')
    #print() #空白を作るだけ
    
    #取得した文字をそれぞれの関数に格納する
    if i == 1:
        title1 = (f' タイトル:{article.get("title")}')
        link1 = (f' リンク:{article.get("link")}')
        published1 = (f' 日付:{article.get("published")}')
        summary1 = (f' 概要:{article.get("summary")}')
    elif i == 2:
        title2 = (f' タイトル:{article.get("title")}')
        link2 = (f' リンク:{article.get("link")}')
        published2 = (f' 日付:{article.get("published")}')
        summary2 = (f' 概要:{article.get("summary")}')
    elif i == 3:
        title3 = (f' タイトル:{article.get("title")}')
        link3 = (f' リンク:{article.get("link")}')
        published3 = (f' 日付:{article.get("published")}')
        summary3 = (f' 概要:{article.get("summary")}')
    elif i == 4:
        title4 = (f' タイトル:{article.get("title")}')
        link4 = (f' リンク:{article.get("link")}')
        published4 = (f' 日付:{article.get("published")}')
        summary4 = (f' 概要:{article.get("summary")}')
    elif i == 5:
        title5 = (f' タイトル:{article.get("title")}')
        link5 = (f' リンク:{article.get("link")}')
        published5 = (f' 日付:{article.get("published")}')
        summary5 = (f' 概要:{article.get("summary")}') 
    
    i = i + 1 
    
    #3回分ループしたら処理を抜ける
    if i == 6:
        break
        
#print("End")

title1 = title1.replace('タイトル:','')
title2 = title2.replace('タイトル:','')
title3 = title3.replace('タイトル:','')
title4 = title4.replace('タイトル:','')
title5 = title5.replace('タイトル:','')

link1 = link1.replace('リンク:','')
link2 = link2.replace('リンク:','')
link3 = link3.replace('リンク:','')
link4 = link4.replace('リンク:','')
link5 = link5.replace('リンク:','')
    
#######################################################################

def get_wet(url_wet):

    global today_wet
    global today_hukai
    global today_pascal
    global hukai_comment

    url = url_wet
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    today_wet = soup.find_all('li')[10]
    today_pascal = soup.find_all('li')[11]

    today_wet = today_wet.text
    today_wet = today_wet.replace('湿度','')
    today_wet = today_wet.replace('%','')
    print('湿度',today_wet)
    
    today_pascal = today_pascal.text
    today_pascal = today_pascal.replace('気圧','')
    today_pascal = today_pascal.replace('hPa','')
    print('気圧',today_pascal)
    
    #不快指数の算出
    temp = today_high_temp
    today_hukai = 0.81 * temp + 0.01 * 55 * (0.99 * temp - 14.3) + 46.3 
    today_hukai = int(today_hukai)
    
    if today_hukai < 50:
        hukai_comment = ("寒くてたまらない")
    elif today_hukai <= 55:
        hukai_comment = ("寒い")
    elif today_hukai <= 60:
        hukai_comment = ("肌寒い")
    elif today_hukai <= 65:
        hukai_comment = ("何も感じない")
    elif today_hukai <= 70:
        hukai_comment = ("快適")
    elif today_hukai <= 75:
        hukai_comment = ("不快感をもつ人が出始める")
    elif today_hukai <= 80:
        hukai_comment = ("半数以上が不快に感じる")
    elif today_hukai <= 85:
        hukai_comment = ("全員が不快に感じる")    
    else:
        hukai_comment = ("暑くてたまらない")
        
    print(hukai_comment)

#######################################################################

#日本語対応
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
#メールの設定
gmail_account = "nozamaiuy@gmail.com"
gmail_password = "Naochan60kg"
app_pass = "dwiy fpnr qpjv mham"

#def gmail_send(send_name,mail_to,filename):
def gmail_send(send_name,mail_to):
    
    #文章の設定
    today_date =datetime.date.today()
    subject = "{0}様,{1}の天気予報です".format(send_name,today_date)
    body = "本日の{0}の天気です<br><br>\
    予想気温は[{1}]~[{2}]度となっています<br>\
    降水確率は0~6時[{3}],6~12時[{4}],12~18時[{5}],18~24時[{6}]です<br>\
    風向きは[{7}]です<br>\
    紫外線-{8}-{9}<br>\
    気圧-[{10}hPa]<br>\
    湿度-[{11}%]<br>\
    不快指数-[{12}]-[{13}]<br><br>\
    If I think about something at three o'clock in the morning and thnen again at noon the next day, you get different answers... By スヌーピー<br><br>\
    Message From Yui".format(area,today_low_temp,today_high_temp,\
                             rain0006,rain0612,rain1218,rain1824,\
                             today_wind,today_uv_summary,today_uv_comment,\
                             today_pascal,today_wet,today_hukai,hukai_comment)
    
    #件名、送り先、
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = gmail_account
    msg_body = MIMEText(body,"html")
    
    #添付ファイルの準備
    msg.attach(msg_body)
    #filename = filename
    #file = open(filename,"rb")

    #添付ファイルのセッティング
    #attachment_file = MIMEBase('application','png')
    #attachment_file.set_payload((file).read())
    #file.close()

    #日本語対応にする処理
    #encoders.encode_base64(attachment_file)
    #attachment_file.add_header('Content-Disposition',"attachment",filename=filename)
    #msg.attach(attachment_file)
    
    #メールを送る処理
    server = smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl.create_default_context())
    server.login(gmail_account,app_pass)
    server.send_message(msg)
    server.close()
    print(send_name,"様:送信完了")
    
#######################################################################

#東根市
forecast_url = "https://tenki.jp/forecast/2/9/3510/6211/"
get_forecast(forecast_url)
print("☆☆☆☆☆天気の取得完了☆☆☆☆☆")

uv_url = "https://tenki.jp/indexes/uv_index_ranking/2/9/3510/6211/"
get_uv(uv_url)
print("☆☆☆☆☆ニュースの取得完了☆☆☆☆☆")

wet_url = "https://weathernews.jp/onebox/tenki/yamagata/06211/"
get_wet(wet_url)
print("☆☆湿度・気圧・不快指数の取得完了☆☆")

address = 'yuito.8039@gmail.com'
onamae = 'yui'
area = "東根市"
gmail_send(onamae,address)

#######################################################################

forecast_url = "https://tenki.jp/forecast/2/9/3530/6204/"
get_forecast(forecast_url)
print("☆☆☆☆☆天気の取得完☆☆☆☆☆了")

uv_url = "https://tenki.jp/indexes/uv_index_ranking/2/9/3530/6204/"
get_uv(uv_url)
print("☆☆☆☆☆ニュースの取得完了☆☆☆☆☆")

wet_url = "https://weathernews.jp/onebox/tenki/yamagata/06204/"
get_wet(wet_url)
print("☆☆湿度・気圧・不快指数の取得完了☆☆")

address = 'naoko8039@gmail.com'
onamae = 'N'
area = "酒田市"
gmail_send(onamae,address)

#######################################################################
