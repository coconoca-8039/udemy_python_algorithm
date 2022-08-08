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

#3件
ITmediaNEWS_break = 4
ITmediaNEWS = "https://news.yahoo.co.jp/rss/media/zdn_n/all.xml"
#2件
ITmediaEnterprise_break = 3
ITmediaEnterprise = "https://news.yahoo.co.jp/rss/media/zdn_ep/all.xml"
#1件
MONOist_break = 2
MONOist = "https://news.yahoo.co.jp/rss/media/it_monoist/all.xml"
#3件
MotorFan_break = 4
MotorFan = "https://news.yahoo.co.jp/rss/media/motorfan/all.xml"
#2件
sorae_break = 3
sorae = "https://news.yahoo.co.jp/rss/media/sorae_jp/all.xml"
#3件
tenkijp_break = 4
tenkijp = "https://news.yahoo.co.jp/rss/media/tenki/all.xml"
#2件
whethermap_break = 3
whethermap = "https://news.yahoo.co.jp/rss/media/wmap/all.xml"
#3件
nikkansangyo_break = 4
nikkansangyo = "https://news.yahoo.co.jp/rss/media/sangyo/all.xml"
#3件
netolab_break = 4
netolab = "https://news.yahoo.co.jp/rss/media/it_nlab/all.xml"
#5件
keizai_break = 6
keizai = "https://news.yahoo.co.jp/rss/topics/business.xml"

#######################################################################

def get_rss(url,end_loop):
    
    jma_news = feedparser.parse(url)
    print(jma_news['feed']['title'])
    i = 1
    
    #グローバル宣言
    global title1
    global title2
    global title3
    global title4
    global title5
    global link1
    global link2
    global link3
    global link4
    global link5

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
            title1 = title1.replace('タイトル:','')
            link1 = (f' リンク:{article.get("link")}')
            link1 = link1.replace('リンク:','')
            published1 = (f' 日付:{article.get("published")}')
            summary1 = (f' 概要:{article.get("summary")}')
        elif i == 2:
            title2 = (f' タイトル:{article.get("title")}')
            title2 = title2.replace('タイトル:','')
            link2 = (f' リンク:{article.get("link")}')
            link2 = link2.replace('リンク:','')
            published2 = (f' 日付:{article.get("published")}')
            summary2 = (f' 概要:{article.get("summary")}')
        elif i == 3:
            title3 = (f' タイトル:{article.get("title")}')
            title3 = title3.replace('タイトル:','')
            link3 = (f' リンク:{article.get("link")}')
            link3 = link3.replace('リンク:','')
            published3 = (f' 日付:{article.get("published")}')
            summary3 = (f' 概要:{article.get("summary")}')
        elif i == 4:
            title4 = (f' タイトル:{article.get("title")}')
            title4 = title4.replace('タイトル:','')
            link4 = (f' リンク:{article.get("link")}')
            link4 = link4.replace('リンク:','')
            published4 = (f' 日付:{article.get("published")}')
            summary4 = (f' 概要:{article.get("summary")}')
        elif i == 5:
            title5 = (f' タイトル:{article.get("title")}')
            title5 = title5.replace('タイトル:','')
            link5 = (f' リンク:{article.get("link")}')
            link5 = link5.replace('リンク:','')
            published5 = (f' 日付:{article.get("published")}')
            summary5 = (f' 概要:{article.get("summary")}') 

        i = i + 1 
        
        #x回分ループしたら処理を抜ける
        if i == end_loop:
            break

    #print("End")

#######################################################################

get_rss(ITmediaNEWS,ITmediaNEWS_break)
ITmediaNEWS_title1 = title1   #0
ITmediaNEWS_title2 = title2   #2
ITmediaNEWS_title3 = title3   #4
ITmediaNEWS_link1 = link1    #1
ITmediaNEWS_link2 = link2    #3
ITmediaNEWS_link3 = link3    #5

get_rss(ITmediaEnterprise,ITmediaEnterprise_break)
ITmediaEnterprise_title1 = title1    #6
ITmediaEnterprise_title2 = title2    #8
ITmediaEnterprise_link1 = link1    #7
ITmediaEnterprise_link2 = link2    #9

get_rss(MONOist,MONOist_break)
MONOist_title1 = title1    #10
MONOist_title2 = title2    #12
MONOist_link1 = link1    #11
MONOist_link2 = link2    #13

get_rss(MotorFan,MotorFan_break)
MotorFan_title1 = title1    #14
MotorFan_title2 = title2    #16
MotorFan_title3 = title3    #18
MotorFan_link1 = link1    #15
MotorFan_link2 = link2    #17
MotorFan_link3 = link3    #19

get_rss(sorae,sorae_break)
sorae_title1 = title1    #20
sorae_title2 = title2    #22
sorae_link1 = link1    #21
sorae_link2 = link2    #23

get_rss(tenkijp,tenkijp_break)
tenkijp_title1 = title1    #24
tenkijp_title2 = title2    #26
tenkijp_title3 = title3    #28
tenkijp_link1 = link1    #25
tenkijp_link2 = link2    #27
tenkijp_link3 = link3    #29

get_rss(whethermap,whethermap_break)
whethermap_title1 = title1    #30
whethermap_title2 = title2    #32
whethermap_link1 = link1    #31
whethermap_link2 = link2    #33

get_rss(nikkansangyo,nikkansangyo_break)
nikkansangyo_title1 = title1    #34
nikkansangyo_title2 = title2    #36
nikkansangyo_title3 = title3    #38
nikkansangyo_link1 = link1    #35
nikkansangyo_link2 = link2    #37
nikkansangyo_link3 = link3    #39

get_rss(netolab,netolab_break)
netolab_title1 = title1    #40
netolab_title2 = title2    #42
netolab_title3 = title3    #44
netolab_link1 = link1    #41
netolab_link2 = link2    #43
netolab_link3 = link3    #45

get_rss(keizai,keizai_break)
keizai_title1 = title1    #46
keizai_title2 = title2    #48
keizai_title3 = title3    #50
keizai_title4 = title4    #52
keizai_title5 = title5    #54
keizai_link1 = link1    #47
keizai_link2 = link2    #49
keizai_link3 = link3    #51
keizai_link4 = link4    #53
keizai_link5 = link5    #55

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
    subject = "{0}様,{1}のニュースです".format(send_name,today_date)
    body = "本日のクリッピングです<br><br>\
    ☆ITmediaNEWS<br>\
    {0}<br>\
    {1}<br>\
    {2}<br>\
    {3}<br>\
    {4}<br>\
    {5}<br><br><br>\
    ☆ITmediaEnterprise<br>\
    {6}<br>\
    {7}<br>\
    {8}<br>\
    {9}<br><br><br>\
    ☆MONOist<br>\
    {10}<br>\
    {11}<br>\
    {12}<br>\
    {13}<br><br><br>\
    ☆MotorFan<br>\
    {14}<br>\
    {15}<br>\
    {16}<br>\
    {17}<br>\
    {18}<br>\
    {19}<br><br><br>\
    ☆sorae 宙へのポータルサイト<br>\
    {20}<br>\
    {21}<br>\
    {22}<br>\
    {23}<br><br><br>\
    ☆tenki.jp<br>\
    {24}<br>\
    {25}<br>\
    {26}<br>\
    {27}<br>\
    {28}<br>\
    {29}<br><br><br>\
    ☆ウェザーマップ<br>\
    {30}<br>\
    {31}<br>\
    {32}<br>\
    {33}<br><br><br>\
    ☆日刊産業新聞<br>\
    {34}<br>\
    {35}<br>\
    {36}<br>\
    {37}<br>\
    {38}<br>\
    {39}<br><br><br>\
    ☆ねとらぼ<br>\
    {40}<br>\
    {41}<br>\
    {42}<br>\
    {43}<br>\
    {44}<br>\
    {45}<br><br><br>\
    ☆Yahooニュース[経済]<br>\
    {46}<br>\
    {47}<br>\
    {48}<br>\
    {49}<br>\
    {50}<br>\
    {51}<br>\
    {52}<br>\
    {53}<br>\
    {54}<br>\
    {55}<br>\
    <br><br>\
    Message From Yui".format(ITmediaNEWS_title1,ITmediaNEWS_link1,ITmediaNEWS_title2,ITmediaNEWS_link2,ITmediaNEWS_title3,ITmediaNEWS_link3,\
                             ITmediaEnterprise_title1,ITmediaEnterprise_link1,ITmediaEnterprise_title2,ITmediaEnterprise_link2,\
                             MONOist_title1,MONOist_link1,MONOist_title2,MONOist_link2,\
                             MotorFan_title1,MotorFan_link1,MotorFan_title2,MotorFan_link2,MotorFan_title3,MotorFan_link3,\
                             sorae_title1,sorae_link1,sorae_title2,sorae_link2,\
                             tenkijp_title1,tenkijp_link1,tenkijp_title2,tenkijp_link2,tenkijp_title3,tenkijp_link3,\
                             whethermap_title1,whethermap_link1,whethermap_title2,whethermap_link2,\
                             nikkansangyo_title1,nikkansangyo_link1,nikkansangyo_title2,nikkansangyo_link2,nikkansangyo_title3,nikkansangyo_link3,\
                             netolab_title1,netolab_link1,netolab_title2,netolab_link2,netolab_title3,netolab_link3,\
                             keizai_title1,keizai_link1,keizai_title2,keizai_link2,keizai_title3,keizai_link3,keizai_title4,keizai_link4,keizai_title5,keizai_link5
                             )
    
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
    
address = 'yuito.8039@gmail.com'
onamae = 'yui'
gmail_send(onamae,address)
