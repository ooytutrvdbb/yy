# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="EqRUDTL9V2COEwg2VqZa.apGNZMzba418M2CeQxD9/G.4ulFYxJwFbG9jWQdXOKFCS0tILAyxWU25tkIMM5Riug=")
cl.loginResult()

ki1 = LINETCR.LINE()
ki1.login(token="EqkIExwj66GELOpG2vb2.Tp+2DgIZ3zX4aseyVxboKG.Ah/I800UBlmzMboOnT4ZGBTAj+GgKMd29fSqW2GC+l8=")
ki1.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EqNTQqAcOAjC65ZgUJ79.8zdD5KVVm93F+f9Qbktt/q.p5PntqFwrlEzw12XKhRVeJpn1rBKWRTnzwUk/Sgq2U0=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EqstMe22kiCoQHR0TKcf.dNBs/Ys/puxDk2XazUUBRW.dBLapBlQTDb99vxA3rHSp1vrd2KxeNcWkZVcUZLEM0Q=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EqtM8zYM3Isc15sYe4Hd.rHmdTXsLiNLo2z/kRLt+hq.16nIMXj2Az4YgngjmjleC/aWPwI2rjcvLQayZYsP28M=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="Eqwqdq0WdSp5YmcBj27c.EZg/zoOGM6cbGX3GoOipxa.YYd7LPhBFZ61km64mhgDhvyi8SD2+2vjlF6B1PV7dHM=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EqCN97em5zdQEFwOGMN3.Qt4DQz3PcTDk9RXedVuBOW.D2SHXBNrr7wEHqChZf52Ppa+dqPxj+8l1D9QB0okPV4=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="EqvvDm2Ik0kvfY2hR9i1.dAbFu5qDJ6YPw1jeyKhVKq.Gdi22MrXyc7ydi8iIr1ZmhH74yiq4m/Eqkw/tLJJp9M=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="Eq1yngcheoADlYc8QBE9.fgus0a7u5LoEfs9YS70wwq.K8Bw/2/vZiwWX648Uos5cf3b0EZk3HiG2/UcF7a7aJo=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EqSHSJ1ZZhw5BiCztJTa.IZkp05oQhsSFjCfboqmFkG.eoJGZTsOJFb7BaoEtstXw0fw7Jx+nvET1QpgLdN9liM=")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="EqJf8QCnp4CS7nyWnOHa.+snuuxSMcQBLjXVJitdSEG.sfcmcUI9n9kyGO9taN/qXHA2vqKaf6Pl0G0KxvcgUMI=")
ki10.loginResult()

ki11 = LINETCR.LINE()
ki11.login(token="EqPRTwizcnePNOEL9FM2./h4lhOAL7KJYBUqHOOzoGG.W+qDT4S/KJQh+63NDIPaDVxuyXETm+KkJC1kRwNUia0=")
ki11.loginResult()

ki12 = LINETCR.LINE()
ki12.login(token="EqiVEWXh81OO0BHQEOl6.1rfIy/E83J50WHhH6XYgbG.GkDJ21uDiwgwc4ge3B3Wjmr0AuU79Q9wiG10Db6Mt8U=")
ki12.loginResult()

ki13 = LINETCR.LINE()
ki13.login(token="EqYx4oW3hf4lmFtedf52.+V7zeX47x3/huBTrBq7JiG.78ikizJprX6MmPbO/+8uRJW/PrSgsAYVs6X2I4GXOac=")
ki13.loginResult()

ki14 = LINETCR.LINE()
ki14.login(token="EqsNNJEJUqUeZtjXaOoc.GyqJDAN7UOhmlSK1F0bKFa.zFNqfve9q6Mv4FDAD05qzpZP4jYOE8DlEQVK/DlaCFw=")
ki14.loginResult()

ki15 = LINETCR.LINE()
ki15.login(token="EqgbIM0rTmTjelpaqIY0.YQgIMwLeV3oxvR5G0dnHya.LW9N0S9KcArwDMYsVUz0sJ/Cose2L4CgWhUwrhQsnuw=")
ki15.loginResult()

ki16 = LINETCR.LINE()
ki16.login(token="EqfQoiUUVPGmJvRSzLYe.vABFWhFVuF9fRmkg6+bVFG.w47t5cE7gdnBwF0diIGM4zvVvNLOt2+HzrUk4r+XjAA=")
ki16.loginResult()

ki17 = LINETCR.LINE()
ki17.login(token="EqaE4d1Vmu2SqTFcgvUc.ZHFtUEUDt3xzxAUi6j9PJa.X5klZppkfMUDhd2oMH6m9ZB9X7Z7WIcRARsex9zz7dY=")
ki17.loginResult()

ki18 = LINETCR.LINE()
ki18.login(token="Eqbij2FZD2liVgmqHhh3.AFjFi3Id/gpOgrtYTfhSyW.De0LT4cQ9SChC/hZrS+aJ4XEqyKKDOsKgIZKm+snSVk=")
ki18.loginResult()

ki19 = LINETCR.LINE()
ki19.login(token="EquhKIyg7AaNTj8z1cv9.SxNrJwhMjr+NgarNkRQEMq.e5ZlDRpKvuWdLYyFeSuI2MZD+yy+VJlTAPDiIP8SKQY=")
ki19.loginResult()

ki20 = LINETCR.LINE()
ki20.login(token="Eq6lGVnFnqFY4RdsK6Yf.eUtowOEM6l9CNjdCzYk8BW.jYIyLLduiIP2FSDsUO7Dc/LP7VDIRJ2djeHdFm9jk/M=")
ki20.loginResult()

ki21 = LINETCR.LINE()
ki21.login(token="Eqyn4YH7PbaRrNzm4za9.wJ+pQr0LE4r+B8fQrUJGsq.RIPuPZAyjzRRKSQXYchG8PQwe7XWoB7bqJAYB2ovHhg=")
ki21.loginResult()

ki22 = LINETCR.LINE()
ki22.login(token="Eq2vlZ2dRg6XsDaBN5ia.MfTKqhz+PM+X2QRY9830AG.XEWL5cyRlVetTU00q3j04s+hE0L3GosJOMc3QfJSF7Q=")
ki22.loginResult()

ki23 = LINETCR.LINE()
ki23.login(token="EqJ8dAVxNqJoUZq193W8.97UN36ECvAYPTrF82bSAMa.PG2wCIIpEQUjfIOajRaIOMzlEfjpbllfC4UG0pgvV3w=")
ki23.loginResult()

ki24 = LINETCR.LINE()
ki24.login(token="Eq88agRTP2qAdXt5gB87.8WXlhPISVfvSwZVCMm8trW.V9TinSUL9ayWmlwMCq7BuhhWUSLflvZ871v6cC9IQw8=")
ki24.loginResult()

ki25 = LINETCR.LINE()
ki25.login(token="EqWTL1oc8mqz0nti2J96.3gbXCx+35kvbr3Aa1GclLG.EBfsPoaN63u5Cx2C4EbJnUV349KWH2R4292TBrLCBjA=")
ki25.loginResult()

ki26 = LINETCR.LINE()
ki26.login(token="Eq7ohpRvzkE1Ui6wX5q7.yiVhtGqFXEogTBSsvAEAjW.w2M6Y6TOTXASZv+o9G2GluOewuX2I6dZvaMa9pmDNOc=")
ki26.loginResult()

ki27 = LINETCR.LINE()
ki27.login(token="EqFgMFOQoEde5M4eYGAd.UPsHSev3CJF/OIop2wEMhq.a+KoNU7VW4iINBAGOrNj45Hdc10PeEP79qlfpIAOGWY=")
ki27.loginResult()

ki28 = LINETCR.LINE()
ki28.login(token="EqLtToUc9hCLTgoONykb.PNd7qLcczJW00ek2Ow2qMW.l3bZRUu6fAEHYBD1UBIfkcqUvDa+ExwKwPF2vZL0nIQ=")
ki28.loginResult()

ki29 = LINETCR.LINE()
ki29.login(token="EqnARUYHsadUpZBEcjK6.O3P+/622/qxgUZ4VNaxKbG.52kQbq5eva4dW5OAVKU4iAG3A6IxJP/d/sJEWeFoCFg=")
ki29.loginResult()

ki30 = LINETCR.LINE()
ki30.login(token="EqWoc6dRcxEMrsHjo6a6.wuRsY0/V927nD9OY59WnPG.MiyLPZXa3g7wfwbCtNPI4tbmpkOADk2HGzjJ6Rk0zQ0=")
ki30.loginResult()

start_runtime = datetime.now()
print "login success"
start_runtime = datetime.now()
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""     ─┅═✥हईທຮຮๅજईह✥═┅─

─┅═✥s̵ᴇʟғʙᴏᴛ ᴛʜᴀɪʟᴀɴᴅ✥═┅─
                     
❂͜͡☆➣ 『Me』
❂͜͡☆➣ 『Id』
❂͜͡☆➣ 『Wc』
❂͜͡☆➣ 『Mc:』
❂͜͡☆➣ 『Mid』
❂͜͡☆➣ 『BBc:』
❂͜͡☆➣ 『Gift』
❂͜͡☆➣ 『Mid @』
❂͜͡☆➣ 『Cn: Display Name』
❂͜͡☆➣ 『Cc: Clock Name』
❂͜͡☆➣ 『Hack @』
❂͜͡☆➣ 『Tl: text』
❂͜͡☆➣ 『Auto join: on/off』
❂͜͡☆➣ 『Auto add: on/off』
❂͜͡☆➣ 『Auto leave: on/off』
❂͜͡☆➣ 『Clock: on/off』
❂͜͡☆➣ 『Share on』
❂͜͡☆➣ 『Add message: text』
❂͜͡☆➣ 『Message:』
❂͜͡☆➣ 『Add comment: text』
❂͜͡☆➣ 『Comment: 』
❂͜͡☆➣ 『Cbroadcast text』
❂͜͡☆➣ 『Gbroadcast text』
❂͜͡☆➣ 『Reject』
 
──┅═✥===========✥═┅──

                 SELFBOT

          PHET HACK BOT
            
──┅═✥===========✥═┅──

❂͜͡☆➣ 『Creator 』
❂͜͡☆➣ 『Gn: text 』
❂͜͡☆➣ 『Invite:on 』
❂͜͡☆➣ 『Invite: mid』 
❂͜͡☆➣ 『Allgift 』
❂͜͡☆➣ 『All mid』
❂͜͡☆➣ 『Cancel』
❂͜͡☆➣ 『Link on/off』
❂͜͡☆➣ 『Spam on/off』
❂͜͡☆➣ 『ginfo』
❂͜͡☆➣ 『Myginfo』
❂͜͡☆➣ 『Gurl』
❂͜͡☆➣ 『Glist』
❂͜͡☆➣ 『Set』
❂͜͡☆➣ 『Phet: Tag』
❂͜͡☆➣ 『Gcancel:』
❂͜͡☆➣ 『Masuk Join』
❂͜͡☆➣ 『Sa:yang』
❂͜͡☆➣ 『Beb』
❂͜͡☆➣ 『Cinta』
❂͜͡☆➣ 『Sayang: 』
❂͜͡☆➣ 『P:ulang』
❂͜͡☆➣ 『Ban @』
❂͜͡☆➣ 『Uban @』
❂͜͡☆➣ 『Ban 』
❂͜͡☆➣ 『Unban』
❂͜͡☆➣ 『Comment :』
❂͜͡☆➣ 『Banlist』
❂͜͡☆➣ 『Cekban』
❂͜͡☆➣ 『Clear ban』
❂͜͡☆➣ 『Kill @ Fuck @』
❂͜͡☆➣ 『Speed / Sp』
❂͜͡☆➣ 『Hack @2@3@4』
❂͜͡☆➣ 『Ambilin @』
❂͜͡☆➣ 『Sampul @』
❂͜͡☆➣ 『Copy @』
❂͜͡☆➣ 『Mycopy @』
❂͜͡☆➣ 『Keluar :@』
❂͜͡☆➣ 『music』
❂͜͡☆➣ 『.reboot』
❂͜͡☆➣ 『Wikipedia』
❂͜͡☆➣ 『Cleanse』
❂͜͡☆➣ 『Bot Speed』
❂͜͡☆➣ 『P1-P36 link on/off』
 
  
──┅═✥===========✥═┅──

❂͜͡☆➣ 『Key』
❂͜͡☆➣ 『Qr on/off』
❂͜͡☆➣ 『Backup on/off』
❂͜͡☆➣ 『Protect On/off』
❂͜͡☆➣ 『Namelock On/off』

    
        ─┅═✥ᵀᴴᴬᴵᴸᴬᴺᴰ✥═┅─

      [By. เพชร ทีมทดลองบอท]

──┅═✥============✥═┅──"""
helpMessage2 ="""
╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Help protect〙
╠➩〘Help self〙
╠➩〘Help grup〙
╠➩〘Help set〙
╠➩〘Help media〙
╠➩〘Speed〙
╠➩〘Status〙
╚═════════════════

╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Protect on/off〙
╠➩〘Qr on/off〙
╠➩〘Invit on/off〙
╠➩〘Cancel on/off〙
╚═════════════════

╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Me〙
╠➩〘Myname: 〙
╠➩〘Mybio: 〙
╠➩〘Myname〙
╠➩〘Mybio〙
╠➩〘Mypict〙
╠➩〘Mycover〙
╠➩〘My,copy @〙
╠➩〘Mybackup〙
╠➩〘Getgrup image〙
╠➩〘Getmid @〙
╠➩〘Getprofile @〙
╠➩〘Getcontact @〙
╠➩〘Getinfo @〙
╠➩〘Getname @〙
╠➩〘Getbio @〙
╠➩〘Getpict @〙
╠➩〘Getcover @〙
╠➩〘Mention〙
╠➩〘Lurk on/off〙
╠➩〘Lurkers〙
╠➩〘Mimic on/off〙
╠➩〘Micadd @〙
╠➩〘Micdel @〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Contact on/off〙
╠➩〘Autojoin on/off〙
╠➩〘Autoleave on/off〙
╠➩〘Autoadd on/off〙
╠➩〘Like me〙
╠➩〘Like friend〙
╠➩〘Like on〙
╠➩〘Respon on/off〙
╠➩〘Read on/off〙
╠➩〘Simisimi on/off〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Link on/off〙
╠➩〘Url〙
╠➩〘Cancel〙
╠➩〘Gcreator〙
╠➩〘Ki'ck @〙
╠➩〘Ulti @〙
╠➩〘Cancel〙
╠➩〘Gname: 〙
╠➩〘Gbroadcast: 〙
╠➩〘Cbroadcast: 〙
╠➩〘Infogrup〙
╠➩〘Gruplist〙
╠➩〘Friendlist〙
╠➩〘Blocklist〙
╠➩〘Ba'n @〙
╠➩〘U'nban @〙
╠➩〘Clearban〙
╠➩〘Banlist〙
╠➩〘Contactban〙
╠➩〘Midban〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Kalender〙
╠➩〘tr-id 〙
╠➩〘tr-en 〙
╠➩〘tr-jp 〙
╠➩〘tr-ko 〙
╠➩〘say-id 〙
╠➩〘say-en 〙
╠➩〘say-jp 〙
╠➩〘say-ko 〙
╠➩〘profileig 〙
╠➩〘checkdate 〙
╚═════════════════
"""
helpMessage3 ="""􀔃􀅉􏿿SELFBOTPHETHACKBOT􀔃􀅉􏿿
╔══════════════════════
║       ✦เปิด/ปิดข้อความต้อนรับ✦
╠══════════════════════
║✰ Hhx1 on ➠เปิดข้อความต้อนรับ
║✰ Hhx1 off ➠ปิดข้อความต้อนรับ
║✰ Hhx2 on ➠เปิดข้อความออกกลุ่ม
║✰ Hhx2 off ➠เปิดข้อความออกกลุ่ม
║✰ Hhx3 on ➠เปิดข้อความคนลบ
║✰ Hhx3 off ➠เปิดข้อความคนลบ
║✰ Mbot on ➠เปิดเเจ้งเตือนบอท
║✰ Mbot off ➠ปิดเเจ้งเตือนบอท
║✰ M on ➠เปิดเเจ้งเตือนตนเอง
║✰ M off ➠ปิดเเจ้งเตือนตนเอง
║✰ Tag on ➠เปิดกล่าวถึงเเท็ค
║✰ Tag off ➠ปิดกล่าวถึงเเท็ค
║✰ Kicktag on ➠เปิดเตะคนเเท็ค
║✰ Kicktag off ➠ปิดเตะคนเเท็ค
╚══════════════════════
╔══════════════════════
║         ✦โหมดตั้งค่าข้อความ✦
╠══════════════════════
║✰ Hhx1˓: ➠ไส่ข้อความต้อนรับ
║✰ Hhx2˓: ➠ไส่ข้อความออกจากกลุ่ม
║✰ Hhx3˓: ➠ไส่ข้อความเมื่อมีคนลบ
╚══════════════════════
╔══════════════════════
║       ✦โหมดเช็คตั้งค่าข้อความ✦
╠══════════════════════
║✰ Hhx1 ➠เช็คข้อความต้อนรับ
║✰ Hhx2 ➠เช็คข้อความคนออก
║✰ Hhx3 ➠เช็คข้อความคนลบ
╚══════════════════════
􀔃􀅉􏿿BY. เพชร ทีมทดลองบอท􀔃􀅉􏿿"""

KAC=[cl,ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30]
mid = cl.getProfile().mid
Amid1 = ki1.getProfile().mid
Amid2 = ki2.getProfile().mid
Amid3 = ki3.getProfile().mid
Amid4 = ki4.getProfile().mid
Amid5 = ki5.getProfile().mid
Amid6 = ki6.getProfile().mid
Amid7 = ki7.getProfile().mid
Amid8 = ki8.getProfile().mid
Amid9 = ki9.getProfile().mid
Amid10 = ki10.getProfile().mid
Amid11 = ki11.getProfile().mid
Amid12 = ki12.getProfile().mid
Amid13 = ki13.getProfile().mid
Amid14 = ki14.getProfile().mid
Amid15 = ki15.getProfile().mid
Amid16 = ki16.getProfile().mid
Amid17 = ki17.getProfile().mid
Amid18 = ki18.getProfile().mid
Amid19 = ki19.getProfile().mid
Amid20 = ki20.getProfile().mid
Amid21 = ki21.getProfile().mid
Amid22 = ki22.getProfile().mid
Amid23 = ki23.getProfile().mid
Amid24 = ki24.getProfile().mid
Amid25 = ki25.getProfile().mid
Amid26 = ki26.getProfile().mid
Amid27 = ki27.getProfile().mid
Amid28 = ki28.getProfile().mid
Amid29 = ki29.getProfile().mid
Amid30 = ki30.getProfile().mid

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
mid = cl.getProfile().mid
Bots = ["u00f827ce6641038d7c9b6704a9777dfa",mid,Amid1,Amid2,Amid3,Amid4,Amid5,Amid6,Amid7,Amid8,Amid9,Amid10,Amid11,Amid12,Amid13,Amid14,Amid15,Amid16,Amid17,Amid18,Amid19,Amid20,Amid21,Amid22,Amid23,Amid24,Amid25,Amid26,Amid27,Amid28,Amid29,Amid30]
self = ["u00f827ce6641038d7c9b6704a9777dfa",mid,Amid1,Amid2,Amid3,Amid4,Amid5,Amid6,Amid7,Amid8,Amid9,Amid10,Amid11,Amid12,Amid13,Amid14,Amid15,Amid16,Amid17,Amid18,Amid19,Amid20,Amid21,Amid22,Amid23,Amid24,Amid25,Amid26,Amid27,Amid28,Amid29,Amid30]
admin = cl.getProfile().mid
admsa = cl.getProfile().mid
owner = cl.getProfile().mid
adminMID = cl.getProfile().mid
wait = {
    "alwayRead":False,
    "aalwayRead":False,
    "detectMention":False,    
    "kickMention":False,
    "steal":False,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add Me MY NAME IS PHET",
    "lang":"JP",
    "comment":"AutoLike by Phet",
    "commentOn":False,
    "acommentOn":False,
    "bcommentOn":False,
    "ccommentOn":False,
    "asacommentOn":False,
    "asbcommentOn":False,
    "asccommentOn":False,
    "Protectcancl":False,
    "pautoJoin":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"༺ ㏒ Ᵽɧëȶ ㏒ ༻",
    "likeOn":False,
    "comment1":"""
          SELFBOTPHETHACKBOT

▀██▀─▄███▄─▀██─██▀██▀▀█ 
─██─███─███─██─██─██▄█ 
─██─▀██▄██▀─▀█▄█▀─██▀█ 
▄██▄▄█▀▀▀─────▀──▄██▄▄█

      http://line.me/ti/p/~Phet_testbot

             By. เพชร ทีมทดลองบอท
""",
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "ainvite":False,
    "binvite":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Hhx1":False,
    "Hhx2":False,
    "Hhx3":False,
    "Notifed":False,
    "Notifedbot":False,
    "atjointicket":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
	"posts":False,
	}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)

def sendImage(self, to_, path):
    M = Message(to=to_, text=None, contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M2 = self._client.sendMessage(0,M)
    M_id = M2.id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendImage2(self, to_, path):
    M = Message(to=to_,contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M_id = self._client.sendMessage(M).id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = cl.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    ki1.sendText(op.param1,str(wait["message"]))
                    ki2.sendText(op.param1,str(wait["message"]))
                    ki3.sendText(op.param1,str(wait["message"]))
                    ki4.sendText(op.param1,str(wait["message"]))
                    ki5.sendText(op.param1,str(wait["message"]))
                    ki6.sendText(op.param1,str(wait["message"]))
                    ki7.sendText(op.param1,str(wait["message"]))
                    ki8.sendText(op.param1,str(wait["message"]))
                    ki9.sendText(op.param1,str(wait["message"]))
                    ki10.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki1.getGroup(op.param1)
                        except:
                            try:
                                G = ki2.getGroup(op.param1)
                            except:
                                try:
                                    G = ki3.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki4.getGroup(op.param1)
                                    except:
                                        try:
                                            G = ki5.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki1.updateGroup(G)
                        except:
                            try:
                                ki2.updateGroup(G)
                            except:
                                try:
                                    ki2.updateGroup(G)
                                except:
                                    try:
                                        ki3.updateGroup(G)
                                    except:
                                        try:
                                            ki4.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki2.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki3.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki4.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group Name Lock")
                                        ki1.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        ki2.sendText(op.param1,"Wekawekaweka (Har Har)")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)



                if op.param3 in mid:
                    if op.param2 in Amid1:
                        G = ki1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki1.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid2:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid3:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid4:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid5:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid6:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid7:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid8:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid9:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid10:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                if op.param3 in Amid1:
                    if op.param2 in Amid2:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)
                        ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in Amid2:
                    if op.param2 in Amid3:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)

                if op.param3 in Amid3:
                    if op.param2 in Amid4:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)

                if op.param3 in Amid4:
                    if op.param2 in Amid5:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)

                if op.param3 in Amid5:
                    if op.param2 in Amid6:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)

                if op.param3 in Amid6:
                    if op.param2 in Amid7:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)

                if op.param3 in Amid7:
                    if op.param2 in Amid8:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Amid8:
                    if op.param2 in Amid9:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Amid9:
                    if op.param2 in Amid10:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                if op.param3 in Amid10:
                    if op.param2 in Amid11:
                        X = ki11.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki11.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki11.updateGroup(X)
                        Ti = ki11.reissueGroupTicket(op.param1)
                if op.param3 in Amid11:
                    if op.param2 in Amid12:
                        X = ki12.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki12.updateGroup(X)
                        Ti = ki12.reissueGroupTicket(op.param1)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki12.updateGroup(X)
                        Ti = ki12.reissueGroupTicket(op.param1)
                if op.param3 in Amid12:
                    if op.param2 in Amid13:
                        X = ki13.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki13.updateGroup(X)
                        Ti = ki13.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki13.updateGroup(X)
                        Ti = ki13.reissueGroupTicket(op.param1)
                if op.param3 in Amid13:
                    if op.param2 in Amid14:
                        X = ki14.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki14.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki14.updateGroup(X)
                        Ti = ki14.reissueGroupTicket(op.param1)
                if op.param3 in Amid14:
                    if op.param2 in Amid15:
                        X = ki15.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki15.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki15.updateGroup(X)
                        Ti = ki15.reissueGroupTicket(op.param1)
                if op.param3 in Amid15:
                    if op.param2 in Amid16:
                        X = ki16.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki16.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki16.updateGroup(X)
                        Ti = ki16.reissueGroupTicket(op.param1)
                if op.param3 in Amid16:
                    if op.param2 in Amid17:
                        X = ki17.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki17.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki17.updateGroup(X)
                        Ti = ki17.reissueGroupTicket(op.param1)
                if op.param3 in Amid17:
                    if op.param2 in Amid18:
                        X = ki18.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki18.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki18.updateGroup(X)
                        Ti = ki18.reissueGroupTicket(op.param1)
                if op.param3 in Amid18:
                    if op.param2 in Amid19:
                        X = ki19.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki19.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki19.updateGroup(X)
                        Ti = ki19.reissueGroupTicket(op.param1)
                if op.param3 in Amid19:
                    if op.param2 in Amid20:
                        X = ki20.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki20.updateGroup(X)
                        Ti = ki20.reissueGroupTicket(op.param1)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki20.updateGroup(X)
                        Ti = ki20.reissueGroupTicket(op.param1)
                if op.param3 in Amid20:
                    if op.param2 in Amid21:
                        X = ki21.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki21.updateGroup(X)
                        Ti = ki21.reissueGroupTicket(op.param1)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki21.updateGroup(X)
                        Ti = ki21.reissueGroupTicket(op.param1)
                if op.param3 in Amid21:
                    if op.param2 in Amid22:
                        X = ki22.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki22.updateGroup(X)
                        Ti = ki22.reissueGroupTicket(op.param1)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki22.updateGroup(X)
                        Ti = ki22.reissueGroupTicket(op.param1)
                if op.param3 in Amid22:
                    if op.param2 in Amid23:
                        X = ki23.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki23.updateGroup(X)
                        Ti = ki23.reissueGroupTicket(op.param1)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki23.updateGroup(X)
                        Ti = ki23.reissueGroupTicket(op.param1)
                if op.param3 in Amid23:
                    if op.param2 in Amid24:
                        X = ki24.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki24.updateGroup(X)
                        Ti = ki24.reissueGroupTicket(op.param1)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki24.updateGroup(X)
                        Ti = ki24.reissueGroupTicket(op.param1)
                if op.param3 in Amid24:
                    if op.param2 in Amid25:
                        X = ki25.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki25.updateGroup(X)
                        Ti = ki25.reissueGroupTicket(op.param1)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki25.updateGroup(X)
                        Ti = ki25.reissueGroupTicket(op.param1)
                if op.param3 in Amid25:
                    if op.param2 in Amid26:
                        X = ki26.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki26.updateGroup(X)
                        Ti = ki26.reissueGroupTicket(op.param1)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki26.updateGroup(X)
                        Ti = ki26.reissueGroupTicket(op.param1)
                if op.param3 in Amid26:
                    if op.param2 in Amid27:
                        X = ki27.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki27.updateGroup(X)
                        Ti = ki27.reissueGroupTicket(op.param1)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki27.updateGroup(X)
                        Ti = ki27.reissueGroupTicket(op.param1)
                if op.param3 in Amid27:
                    if op.param2 in Amid28:
                        X = ki28.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki28.updateGroup(X)
                        Ti = ki28.reissueGroupTicket(op.param1)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki28.updateGroup(X)
                        Ti = ki28.reissueGroupTicket(op.param1)
                if op.param3 in Amid28:
                    if op.param2 in Amid29:
                        X = ki29.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki29.updateGroup(X)
                        Ti = ki29.reissueGroupTicket(op.param1)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki29.updateGroup(X)
                        Ti = ki29.reissueGroupTicket(op.param1)
                if op.param3 in Amid29:
                    if op.param2 in Amid30:
                        X = ki30.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki30.updateGroup(X)
                        Ti = ki30.reissueGroupTicket(op.param1)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki30.updateGroup(X)
                        Ti = ki30.reissueGroupTicket(op.param1)
                if op.param3 in Amid30:
                    if op.param2 in Amid1:
                        X = ki1.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki1.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki1.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)
#===========================================
        if op.type == 32:
            if not op.param2 in Bots:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1, "★[รับทำSelfbot]★\n★[ป้องกันการรันทุกอย่าง]★\nhttp://line.me/ti/p/tRyWb1P94w\nBy. ✧เพชร ทีมทดลองบอท✧")
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1, "★[รับทำSelfbot]★\n★[ป้องกันการรันทุกอย่าง]★\nhttp://line.me/ti/p/tRyWb1P94w\nBy. ✧เพชร ทีมทดลองบอท✧")
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    cl.sendText(op.param1, "ผู้ใช้รายนี้อยู่ในบัณชีดำของฉัน...")
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["protectionOn"] == True:
                 try:                    
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                 except Exception, e:
                           print e
        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots:
                if wait["protectionOn"] == True:  
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki1.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        gs = ki3.getGroup(op.param1)
                        gs = ki4.getGroup(op.param1)
                        gs = ki5.getGroup(op.param1)
                        gs = ki6.getGroup(op.param1)
                        gs = ki7.getGroup(op.param1)
                        gs = ki8.getGroup(op.param1)
                        gs = ki9.getGroup(op.param1)
                        gs = ki10.getGroup(op.param1)
                        gs = ki11.getGroup(op.param1)
                        gs = ki12.getGroup(op.param1)
                        gs = ki13.getGroup(op.param1)
                        gs = ki14.getGroup(op.param1)
                        gs = ki15.getGroup(op.param1)
                        gs = ki16.getGroup(op.param1)
                        gs = ki17.getGroup(op.param1)
                        gs = ki18.getGroup(op.param1)
                        gs = ki19.getGroup(op.param1)
                        gs = ki20.getGroup(op.param1)
                        gs = ki21.getGroup(op.param1)
                        gs = ki22.getGroup(op.param1)
                        gs = ki23.getGroup(op.param1)
                        gs = ki24.getGroup(op.param1)
                        gs = ki25.getGroup(op.param1)
                        gs = ki26.getGroup(op.param1)
                        gs = ki27.getGroup(op.param1)
                        gs = ki28.getGroup(op.param1)
                        gs = ki29.getGroup(op.param1)
                        gs = ki30.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       G.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.1)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       G.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       G.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots:
                    try:
                        gs = ki1.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        gs = ki3.getGroup(op.param1)
                        gs = ki4.getGroup(op.param1)
                        gs = ki5.getGroup(op.param1)
                        gs = ki6.getGroup(op.param1)
                        gs = ki7.getGroup(op.param1)
                        gs = ki8.getGroup(op.param1)
                        gs = ki9.getGroup(op.param1)
                        gs = ki10.getGroup(op.param1)
                        gs = ki11.getGroup(op.param1)
                        gs = ki12.getGroup(op.param1)
                        gs = ki13.getGroup(op.param1)
                        gs = ki14.getGroup(op.param1)
                        gs = ki15.getGroup(op.param1)
                        gs = ki16.getGroup(op.param1)
                        gs = ki17.getGroup(op.param1)
                        gs = ki18.getGroup(op.param1)
                        gs = ki19.getGroup(op.param1)
                        gs = ki20.getGroup(op.param1)
                        gs = ki21.getGroup(op.param1)
                        gs = ki22.getGroup(op.param1)
                        gs = ki23.getGroup(op.param1)
                        gs = ki24.getGroup(op.param1)
                        gs = ki25.getGroup(op.param1)
                        gs = ki26.getGroup(op.param1)
                        gs = ki27.getGroup(op.param1)
                        gs = ki28.getGroup(op.param1)
                        gs = ki29.getGroup(op.param1)
                        gs = ki30.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:              
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ki1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki1.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki1.updateGroup(G)
                    Ti = ki1.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid1 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki1.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki1.updateGroup(X)
                    Ticket = ki1.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


                if Amid2 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki3.updateGroup(X)
                    Ticket = ki3.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid3 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki3.updateGroup(X)
                    Ticket = ki3.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid4 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki4.updateGroup(X)
                    Ticket = ki4.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid5 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki6.updateGroup(X)
                    Ti = ki6.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki5.updateGroup(X)
                    Ticket = ki5.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid6 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki7.updateGroup(X)
                    Ti = ki7.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki6.updateGroup(X)
                    Ticket = ki6.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid7 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki8.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki8.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki8.updateGroup(X)
                    Ti = ki8.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki7.updateGroup(X)
                    Ticket = ki7.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid8 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki9.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki9.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki9.updateGroup(X)
                    Ti = ki9.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki8.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki8.updateGroup(X)
                    Ticket = ki8.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid9 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki10.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki10.updateGroup(X)
                    Ti = ki10.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki9.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki9.updateGroup(X)
                    Ticket = ki9.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid10 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki11.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki11.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki11.updateGroup(X)
                    Ti = ki11.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki10.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki10.updateGroup(X)
                    Ticket = ki10.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid11 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki12.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki12.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki12.updateGroup(X)
                    Ti = ki12.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki11.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki11.updateGroup(X)
                    Ticket = ki11.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid12 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki13.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki13.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki13.updateGroup(X)
                    Ti = ki13.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki12.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki12.updateGroup(X)
                    Ticket = ki12.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid13 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki14.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki14.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki14.updateGroup(X)
                    Ti = ki14.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki13.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki13.updateGroup(X)
                    Ticket = ki13.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid14 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki15.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki15.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki15.updateGroup(X)
                    Ti = ki15.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki14.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki14.updateGroup(X)
                    Ticket = ki14.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid15 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki16.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki16.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki16.updateGroup(X)
                    Ti = ki16.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki15.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki15.updateGroup(X)
                    Ticket = ki15.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid16 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki17.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki17.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki17.updateGroup(X)
                    Ti = ki17.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki16.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki16.updateGroup(X)
                    Ticket = ki16.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid17 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki18.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki18.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki18.updateGroup(X)
                    Ti = ki18.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki17.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki17.updateGroup(X)
                    Ticket = ki17.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid18 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki19.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki19.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki19.updateGroup(X)
                    Ti = ki19.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki18.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki18.updateGroup(X)
                    Ticket = ki18.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid19 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki20.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki20.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki20.updateGroup(X)
                    Ti = ki20.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki19.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki19.updateGroup(X)
                    Ticket = ki19.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid20 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki21.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki21.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki21.updateGroup(X)
                    Ti = ki21.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki20.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki20.updateGroup(X)
                    Ticket = ki20.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid21 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki22.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki22.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki22.updateGroup(X)
                    Ti = ki22.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki21.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki21.updateGroup(X)
                    Ticket = ki21.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid22 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki23.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki23.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki23.updateGroup(X)
                    Ti = ki23.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki22.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki22.updateGroup(X)
                    Ticket = ki22.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid23 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki24.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki24.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki24.updateGroup(X)
                    Ti = ki24.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki23.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki23.updateGroup(X)
                    Ticket = ki23.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid24 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki25.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki25.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki25.updateGroup(X)
                    Ti = ki25.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki24.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki24.updateGroup(X)
                    Ticket = ki24.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid25 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki26.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki26.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki26.updateGroup(X)
                    Ti = ki26.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki25.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki25.updateGroup(X)
                    Ticket = ki25.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid26 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki27.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki27.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki27.updateGroup(X)
                    Ti = ki27.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki26.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki26.updateGroup(X)
                    Ticket = ki26.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid27 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki28.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki28.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki28.updateGroup(X)
                    Ti = ki28.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki27.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki27.updateGroup(X)
                    Ticket = ki27.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid28 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki29.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki29.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki29.updateGroup(X)
                    Ti = ki29.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki28.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki28.updateGroup(X)
                    Ticket = ki28.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid29 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki30.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki30.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki30.updateGroup(X)
                    Ti = ki30.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki29.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki29.updateGroup(X)
                    Ticket = ki29.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid30 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki1.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki1.updateGroup(X)
                    Ti = ki1.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki16.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki17.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki18.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki19.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki20.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki21.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki22.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki23.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki24.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki25.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki26.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki27.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki28.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki29.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki30.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki30.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki30.updateGroup(X)
                    Ticket = k310.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                ki1.leaveRoom(op.param1)
                ki2.leaveRoom(op.param1)
                ki3.leaveRoom(op.param1)
                ki4.leaveRoom(op.param1)
                ki5.leaveRoom(op.param1)
                ki6.leaveRoom(op.param1)
                ki7.leaveRoom(op.param1)
                ki8.leaveRoom(op.param1)
                ki9.leaveRoom(op.param1)
                ki10.leaveRoom(op.param1)
                ki11.leaveRoom(op.param1)
                ki12.leaveRoom(op.param1)
                ki13.leaveRoom(op.param1)
                ki14.leaveRoom(op.param1)
                ki15.leaveRoom(op.param1)
                ki16.leaveRoom(op.param1)
                ki18.leaveRoom(op.param1)
                ki19.leaveRoom(op.param1)
                ki20.leaveRoom(op.param1)
                ki21.leaveRoom(op.param1)
                ki22.leaveRoom(op.param1)
                ki23.leaveRoom(op.param1)
                ki24.leaveRoom(op.param1)
                ki25.leaveRoom(op.param1)
                ki26.leaveRoom(op.param1)
                ki27.leaveRoom(op.param1)
                ki28.leaveRoom(op.param1)
                ki29.leaveRoom(op.param1)
                ki30.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                ki1.leaveRoom(op.param1)
                ki2.leaveRoom(op.param1)
                ki3.leaveRoom(op.param1)
                ki4.leaveRoom(op.param1)
                ki5.leaveRoom(op.param1)
                ki6.leaveRoom(op.param1)
                ki7.leaveRoom(op.param1)
                ki8.leaveRoom(op.param1)
                ki9.leaveRoom(op.param1)
                ki10.leaveRoom(op.param1)
                ki11.leaveRoom(op.param1)
                ki12.leaveRoom(op.param1)
                ki13.leaveRoom(op.param1)
                ki14.leaveRoom(op.param1)
                ki15.leaveRoom(op.param1)
                ki16.leaveRoom(op.param1)
                ki18.leaveRoom(op.param1)
                ki19.leaveRoom(op.param1)
                ki20.leaveRoom(op.param1)
                ki21.leaveRoom(op.param1)
                ki22.leaveRoom(op.param1)
                ki23.leaveRoom(op.param1)
                ki24.leaveRoom(op.param1)
                ki25.leaveRoom(op.param1)
                ki26.leaveRoom(op.param1)
                ki27.leaveRoom(op.param1)
                ki28.leaveRoom(op.param1)
                ki29.leaveRoom(op.param1)
                ki30.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to, "error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
                    ki1.leaveRoom(msg.to)
                    ki2.leaveRoom(msg.to)
                    ki3.leaveRoom(msg.to)
                    ki4.leaveRoom(msg.to)
                    ki5.leaveRoom(msg.to)
                    ki6.leaveRoom(msg.to)
                    ki7.leaveRoom(msg.to)
                    ki8.leaveRoom(msg.to)
                    ki9.leaveRoom(msg.to)
                    ki10.leaveRoom(msg.to)
                    ki11.leaveRoom(msg.to)
                    ki12.leaveRoom(msg.to)
                    ki13.leaveRoom(msg.to)
                    ki14.leaveRoom(msg.to)
                    ki15.leaveRoom(msg.to)
                    ki16.leaveRoom(msg.to)
                    ki17.leaveRoom(msg.to)
                    ki18.leaveRoom(msg.to)
                    ki19.leaveRoom(msg.to)
                    ki20.leaveRoom(msg.to)
                    ki21.leaveRoom(msg.to)
                    ki22.leaveRoom(msg.to)
                    ki23.leaveRoom(msg.to)
                    ki24.leaveRoom(msg.to)
                    ki25.leaveRoom(msg.to)
                    ki26.leaveRoom(msg.to)
                    ki27.leaveRoom(msg.to)
                    ki28.leaveRoom(msg.to)
                    ki29.leaveRoom(msg.to)
                    ki30.leaveRoom(msg.to)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[ChatBOT] " + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["เเท็กทำไมเดะตบ..!!"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break            
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + ""]
                     ret_ = "[Auto] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7
                                  msg.text = ''
                                  msg.contentMetadata = {
                                                            'STKPKGID': '608',
                                                            'STKTXT': '[]',
                                                            'STKVER': '16',
                                                            'STKID':'5507'
                                                        }
                                  cl.sendMessage(msg)
                                  break
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Alin lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30]
                                  kicker = random.choice(klist)
                                  cl.sendText(msg.to,ret_)
                                  kicker.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass    
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)

            if wait["aalwayRead"] == True:
                if msg.toType == 0:
                    ki1.sendChatChecked(msg.from_,msg.id)
                    ki2.sendChatChecked(msg.from_,msg.id)
                    ki3.sendChatChecked(msg.from_,msg.id)
                    ki4.sendChatChecked(msg.from_,msg.id)
                    ki5.sendChatChecked(msg.from_,msg.id)
                    ki6.sendChatChecked(msg.from_,msg.id)
                    ki7.sendChatChecked(msg.from_,msg.id)
                    ki8.sendChatChecked(msg.from_,msg.id)
                    ki9.sendChatChecked(msg.from_,msg.id)
                    ki10.sendChatChecked(msg.from_,msg.id)
                    ki11.sendChatChecked(msg.from_,msg.id)
                    ki12.sendChatChecked(msg.from_,msg.id)
                    ki13.sendChatChecked(msg.from_,msg.id)
                    ki14.sendChatChecked(msg.from_,msg.id)
                    ki15.sendChatChecked(msg.from_,msg.id)
                    ki16.sendChatChecked(msg.from_,msg.id)
                    ki17.sendChatChecked(msg.from_,msg.id)
                    ki18.sendChatChecked(msg.from_,msg.id)
                    ki19.sendChatChecked(msg.from_,msg.id)
                    ki20.sendChatChecked(msg.from_,msg.id)
                    ki21.sendChatChecked(msg.from_,msg.id)
                    ki22.sendChatChecked(msg.from_,msg.id)
                    ki23.sendChatChecked(msg.from_,msg.id)
                    ki24.sendChatChecked(msg.from_,msg.id)
                    ki25.sendChatChecked(msg.from_,msg.id)
                    ki26.sendChatChecked(msg.from_,msg.id)
                    ki27.sendChatChecked(msg.from_,msg.id)
                    ki28.sendChatChecked(msg.from_,msg.id)
                    ki29.sendChatChecked(msg.from_,msg.id)
                    ki30.sendChatChecked(msg.from_,msg.id)
                else:
                    ki1.sendChatChecked(msg.to,msg.id)
                    ki2.sendChatChecked(msg.to,msg.id)
                    ki3.sendChatChecked(msg.to,msg.id)
                    ki4.sendChatChecked(msg.to,msg.id)
                    ki5.sendChatChecked(msg.to,msg.id)
                    ki6.sendChatChecked(msg.to,msg.id)
                    ki7.sendChatChecked(msg.to,msg.id)
                    ki8.sendChatChecked(msg.to,msg.id)
                    ki9.sendChatChecked(msg.to,msg.id)
                    ki10.sendChatChecked(msg.to,msg.id)
                    ki11.sendChatChecked(msg.to,msg.id)
                    ki12.sendChatChecked(msg.to,msg.id)
                    ki13.sendChatChecked(msg.to,msg.id)
                    ki14.sendChatChecked(msg.to,msg.id)
                    ki15.sendChatChecked(msg.to,msg.id)
                    ki16.sendChatChecked(msg.to,msg.id)
                    ki17.sendChatChecked(msg.to,msg.id)
                    ki18.sendChatChecked(msg.to,msg.id)
                    ki19.sendChatChecked(msg.to,msg.id)
                    ki20.sendChatChecked(msg.to,msg.id)
                    ki21.sendChatChecked(msg.to,msg.id)
                    ki22.sendChatChecked(msg.to,msg.id)
                    ki23.sendChatChecked(msg.to,msg.id)
                    ki24.sendChatChecked(msg.to,msg.id)
                    ki25.sendChatChecked(msg.to,msg.id)
                    ki26.sendChatChecked(msg.to,msg.id)
                    ki27.sendChatChecked(msg.to,msg.id)
                    ki28.sendChatChecked(msg.to,msg.id)
                    ki29.sendChatChecked(msg.to,msg.id)
                    ki30.sendChatChecked(msg.to,msg.id)

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        ki1.sendText(msg.to,"already")
                        ki2.sendText(msg.to,"already")
                        ki3.sendText(msg.to,"already")
                        ki4.sendText(msg.to,"already")
                        ki5.sendText(msg.to,"already")
                        ki6.sendText(msg.to,"already")
                        ki7.sendText(msg.to,"already")
                        ki8.sendText(msg.to,"already")
                        ki9.sendText(msg.to,"already")
                        ki10.sendText(msg.to,"already")

                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
                        ki1.sendText(msg.to,"decided not to comment")
                        ki2.sendText(msg.to,"decided not to comment")
                        ki3.sendText(msg.to,"decided not to comment")
                        ki4.sendText(msg.to,"decided not to comment")
                        ki5.sendText(msg.to,"decided not to comment")
                        ki6.sendText(msg.to,"decided not to comment")
                        ki7.sendText(msg.to,"decided not to comment")
                        ki8.sendText(msg.to,"decided not to comment")
                        ki9.sendText(msg.to,"decided not to comment")
                        ki10.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done deleted")
                        ki1.sendText(msg.to,"Done deleted")
                        ki2.sendText(msg.to,"Done deleted")
                        ki3.sendText(msg.to,"Done deleted")
                        ki4.sendText(msg.to,"Done deleted")
                        ki5.sendText(msg.to,"Done deleted")
                        ki6.sendText(msg.to,"Done deleted")
                        ki7.sendText(msg.to,"Done deleted")
                        ki8.sendText(msg.to,"Done deleted")
                        ki9.sendText(msg.to,"Done deleted")
                        ki10.sendText(msg.to,"Done deleted")
                   
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki1.sendText(msg.to,"It is not in the black list")
                        ki2.sendText(msg.to,"It is not in the black list")
                        ki3.sendText(msg.to,"It is not in the black list")
                        ki4.sendText(msg.to,"It is not in the black list")
                        ki5.sendText(msg.to,"It is not in the black list")
                        ki6.sendText(msg.to,"It is not in the black list")
                        ki7.sendText(msg.to,"It is not in the black list")
                        ki8.sendText(msg.to,"It is not in the black list")
                        ki9.sendText(msg.to,"It is not in the black list")
                        ki10.sendText(msg.to,"It is not in the black list")
                
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Done already")
                        ki1.sendText(msg.to,"Done already")
                        ki2.sendText(msg.to,"Done already")
                        ki3.sendText(msg.to,"Done already")
                        ki4.sendText(msg.to,"Done already")
                        ki5.sendText(msg.to,"Done already")
                        ki6.sendText(msg.to,"Done already")
                        ki7.sendText(msg.to,"Done already")
                        ki8.sendText(msg.to,"Done already")
                        ki9.sendText(msg.to,"Done already")
                        ki10.sendText(msg.to,"Done already")

                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done done aded")
                        ki1.sendText(msg.to,"Done done aded")
                        ki2.sendText(msg.to,"Done done aded")
                        ki3.sendText(msg.to,"Done done aded")
                        ki4.sendText(msg.to,"Done done aded")
                        ki5.sendText(msg.to,"Done done aded")
                        ki6.sendText(msg.to,"Done done aded")
                        ki7.sendText(msg.to,"Done done aded")
                        ki8.sendText(msg.to,"Done done aded")
                        ki9.sendText(msg.to,"Done done aded")
                        ki10.sendText(msg.to,"Done done aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done deleted")
                        ki1.sendText(msg.to,"Done deleted")
                        ki2.sendText(msg.to,"Done deleted")
                        ki3.sendText(msg.to,"Done deleted")
                        ki4.sendText(msg.to,"Done deleted")
                        ki5.sendText(msg.to,"Done deleted")
                        ki6.sendText(msg.to,"Done deleted")
                        ki7.sendText(msg.to,"Done deleted")
                        ki8.sendText(msg.to,"Done deleted")
                        ki9.sendText(msg.to,"Done deleted")

                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki1.sendText(msg.to,"It is not in the black list")
                        ki2.sendText(msg.to,"It is not in the black list")
                        ki3.sendText(msg.to,"It is not in the black list")
                        ki4.sendText(msg.to,"It is not in the black list")
                        ki5.sendText(msg.to,"It is not in the black list")
                        ki6.sendText(msg.to,"It is not in the black list")
                        ki7.sendText(msg.to,"It is not in the black list")
                        ki8.sendText(msg.to,"It is not in the black list")
                        ki9.sendText(msg.to,"It is not in the black list")
                        ki10.sendText(msg.to,"It is not in the black list")

               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help","คำสั่ง","help"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Cmd"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage2 + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Help2","Sett"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage3 + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                     if msg.from_ == admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki1.findAndAddContactsByMid(invite)
                                         ki1.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
                if wait['ainvite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ki1.sendText(msg.to, _name + " สมาชิกอยู่ในกลุ่มเเล้ว")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ki1.findAndAddContactsByMid(target)
                                 ki1.inviteIntoGroup(msg.to,[target])
                                 ki1.sendText(msg.to,"Invite " + _name)
                                 wait['ainvite'] = False
                                 break                              
                             except:             
                                      ki1.sendText(msg.to,"Error")
                                      wait['ainvite'] = False
                                      break
            
            if msg.contentType == 13:
                if wait['binvite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ki2.sendText(msg.to, _name + " สมาชิกอยู่ในกลุ่มเเล้ว")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ki2.findAndAddContactsByMid(target)
                                 ki2.inviteIntoGroup(msg.to,[target])
                                 ki2.sendText(msg.to,"Invite " + _name)
                                 wait['binvite'] = False
                                 break                              
                             except:             
                                      ki2.sendText(msg.to,"Error")
                                      wait['binvite'] = False
                                      break

            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'hack bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid1}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid2}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid3}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid4}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid5}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid6}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid7}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid8}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid9}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid10}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid11}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid12}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid13}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid14}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid15}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid16}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid17}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid18}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid19}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid20}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid21}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid22}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid23}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid24}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid25}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid26}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid27}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid28}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid29}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid30}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid1}
                ki1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid2}
                ki2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid3}
                ki3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid4}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid5}
                ki5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid6}
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid7}
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid8}
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid9}
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid10}
                ki10.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid11}
                ki11.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid12}
                ki12.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid13}
                ki13.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid14}
                ki14.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid15}
                ki15.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid16}
                ki16.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid17}
                ki17.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid18}
                ki18.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid19}
                ki19.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid20}
                ki20.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid21}
                ki21.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid22}
                ki22.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid23}
                ki23.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid24}
                ki24.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid25}
                ki25.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid26}
                ki26.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid27}
                ki27.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid28}
                ki28.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid29}
                ki29.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid30}
                ki30.sendMessage(msg)
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "vdo:" in msg.text.lower():
                if msg.toType == 2:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'ยูทูป ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")



            elif msg.text in ["55"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }

                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
            elif "youname " in msg.text.lower():
                txt = msg.text.replace("youname ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"


            elif "Bl " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Banned")
                            print "[Command] Bannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#------------------------------- UNBAN BY TAG -------------------------------
            elif "Wl " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Unbanned")
                            print "[Command] Unbannad"
                        except:
                            pass
            elif "Mimic:" in msg.text:
                if msg.from_ in admin:
                    cmd = msg.text.replace("Mimic:","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            cl.sendText(msg.to,"Mimic on\n\nเปิดการเลียนเเบบ")
                        else:
                            cl.sendText(msg.to,"Mimic already on\n\nเปิดการเลียนเเบบ")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            cl.sendText(msg.to,"Mimic off\n\nปิดการเลียนเเบบ")
                        else:
                            cl.sendText(msg.to,"Mimic already off\n\nปิดการเลียนเเบบ")
                    elif "add:" in cmd:
                        target0 = msg.text.replace("Mimic:add:","")
                        target1 = target0.lstrip()
                        target2 = target1.replace("@","")
                        target3 = target2.rstrip()
                        _name = target3
                        gInfo = cl.getGroup(msg.to)
                        targets = []
                        for a in gInfo.members:
                            if _name == a.displayName:
                                targets.append(a.mid)
                        if targets == []:
                            cl.sendText(msg.to,"No targets\n\nเกิดผิดพลาด")
                        else:
                            for target in targets:
                                try:
                                    mimic["target"][target] = True
                                    cl.sendText(msg.to,"Success added target")
                                    cl.sendMessageWithMention(msg.to,target)
                                    break
                                except:
                                    cl.sendText(msg.to,"โปรเเกรมเลียนเเบบทำงาน")
                                    break
                    elif "del:" in cmd:
                        target0 = msg.text.replace("Mimic:del:","")
                        target1 = target0.lstrip()
                        target2 = target1.replace("@","")
                        target3 = target2.rstrip()
                        _name = target3
                        gInfo = cl.getGroup(msg.to)
                        targets = []
                        for a in gInfo.members:
                            if _name == a.displayName:
                                targets.append(a.mid)
                        if targets == []:
                            cl.sendText(msg.to,"No targets\n\nเกิดข้อผิดพลาด")
                        else:
                            for target in targets:
                                try:
                                    del mimic["target"][target]
                                    cl.sendText(msg.to,"Success deleted target")
                                    cl.sendMessageWithMention(msg.to,target)
                                    break
                                except:
                                    cl.sendText(msg.to,"คุณลบการเลียนเเบบผู้ใช้นี้")
                                    break
                    elif cmd == "list":
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"No target")
                        else:
                            lst = "<<List Target>>"
                            total = len(mimic["target"])
                            for a in mimic["target"]:
                                if mimic["target"][a] == True:
                                    stat = "On"
                                else:
                                    stat = "Off"
                                lst += "\n-> " + cl.getContact(a).displayName + " | " + stat
                            cl.sendText(msg.to,lst + "\nTotal: " + total)


#----------------------------------------------------------------------------
            elif msg.text.lower() in ["botkill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ki1.kickoutFromGroup(msg.to,[jj])
                        pass
            elif msg.text.lower() in ["admins","mee"]:
                msg.contentType = 13
                adm = 'u00f827ce6641038d7c9b6704a9777dfa'
                msg.contentMetadata = {'mid': adm}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"SELFBOT PHET HAXK BOT")


            elif msg.text in ["ของขวัญ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)

            #VPS STUFF - VPS NEEDED TO RUN THIS COMMAND :)
            elif msg.text in ["vps","kernel","Vps"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
                 else:
                     cl.sendText(msg.to,"Command denied.")
                     cl.sendText(msg.to,"Admin permission required.")
                     print "[Error]Command denied - Admin permission required"

            elif "Gc" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")
            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")

            elif "#set" in msg.text:
				cl.sendText(msg.to, "Let's see who lazy to type")
				try:
					del wait2['readPoint'][msg.to]
					del wait2['readMember'][msg.to]
				except:
					pass
				wait2['readPoint'][msg.to] = msg.id
				wait2['readMember'][msg.to] = ""
				wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				wait2['ROM'][msg.to] = {}
				print wait2
            elif "#read" in msg.text:
				if msg.to in wait2['readPoint']:
					if wait2["ROM"][msg.to].items() == []:
						chiya = ""
					else:
						chiya = ""
						for rom in wait2["ROM"][msg.to].items():
							print rom
							chiya += rom[1] + "\n"

					cl.sendText(msg.to, "people who reading%s\n is this\n\n\nDate and time I started it:\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
				else:
					cl.sendText(msg.to, "read point not set\nReading point setting you send it it will send an esxisting one")


            elif msg.text in ["Myginfoid"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)

            elif msg.text in ["P1 invite","P1 Invite"]:
                wait["ainvite"] = True
                ki.sendText(msg.to,"Send Contact")
            elif msg.text in ["P2 invite","P2 Invite"]:
                wait["binvite"] = True
                kk.sendText(msg.to,"Send Contact")
#==================================================
            elif "#nall" in msg.text:
                       nk0 = msg.text.replace("#nall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    cu = cl.channel.getCover(target)
                                    path = str(cu)
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    cl.sendText(msg.to,"Nama :\n" + contact.displayName  + "\n􀄃􀄷􏿿คนนี้น่ารักจัง􀄃􀄷􏿿")
                                except Exception as e:
                                    raise e
            elif "#botnall" in msg.text:
                       nk0 = msg.text.replace("#botnall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    cu = cl.channel.getCover(target)
                                    path = str(cu)
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15]
                                    kicker = random.choice(klist)
                                    kicker.sendText(msg.to,"Nama :\n" + contact.displayName  + "\n􀄃􀄷􏿿คนนี้น่ารักจัง􀄃􀄷􏿿")
                                except Exception as e:
                                    raise e
            elif "#ประกาศ:" in msg.text:
                bctxt = msg.text.replace("#ประกาศ:", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            elif msg.text.lower() == 'bann':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text in ["มาหำ","#Kicker","#kicker","Kicker","kicker","•••"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki21.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki22.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki23.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki24.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki25.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki26.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki27.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki28.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki29.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki30.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.sendText(msg.to,"[SELFBOT PHET HACK BOT]")
                        ki2.sendText(msg.to,"[Do not think  will try.]")
                        ki3.sendText(msg.to,"[☢Ŧ€₳M≈ನန้ণএ≈฿❂Ŧ☢]")
                        ki4.sendText(msg.to,"Hello " + str(ginfo.name) + "\n\n[By.เพชร ทีมมดลองบอท]")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text in ["kicker10in","Kicker10in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
            elif msg.text in ["ออก","บอทออก","Bye","#bye","bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki1.sendText(msg.to,"wait.....")
                        ki1.sendText(msg.to,"ok....")
                        ki1.sendText(msg.to,"good bye....")
                        ki1.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
                        ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                    except:
                        pass

            elif msg.text.lower() == '#byeall':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
                        ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                    except:
                        pass

            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["เชิญ"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")

            elif msg.text in ["Invite off"]:
                if msg.from_ in admin:
                 wait["winvite"] = False
                 cl.sendText(msg.to,"Done..")
            elif msg.text in ["Bot1 invite contact","1เชิญ"]:
                if msg.from_ in admin:
                 wait["ainvite"] = True
                 ki1.sendText(msg.to,"send contact")
            elif msg.text in ["Bot2 invite contact","2เชิญ"]:
                if msg.from_ in admin:
                 wait["binvite"] = True
                 ki2.sendText(msg.to,"send contact")
            elif ("Ktc " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                           ki3.inviteIntoGroup(msg.to,[target])
                           ki4.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif msg.text in ["#Link on"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == 'ginfo':
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
            elif msg.text in ["!Glist","Myginfo"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")


            elif msg.text in ["Selfbot"]:
				msg.contentType = 13
				msg.contentMetadata = {'mid': mid}
				cl.sendMessage(msg)
				cl.sendText(msg.to,"[SELFBOT PHET HACK BOT]")
            elif "Id" == msg.text:
                key = msg.to
                cl.sendText(msg.to, key)

            elif ("Hack " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" + key1)

            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif "Me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
            elif "#me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("#me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        ki1.sendMessage(msg)
                        ki2.sendMessage(msg)
                        ki3.sendMessage(msg)
                        ki4.sendMessage(msg)
                        ki5.sendMessage(msg)
                        ki6.sendMessage(msg)
                        ki7.sendMessage(msg)
                        ki8.sendMessage(msg)
                        ki9.sendMessage(msg)
                        ki10.sendMessage(msg)

                    else:
                         pass
            elif "#cb" in msg.text:
                       nk0 = msg.text.replace("#cb","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"😏")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"😏")
                                except:
                                    cl.sendText(msg.to,"😏")

            elif "#Banall" in msg.text:
                       nk0 = msg.text.replace("#Banall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "#Unbanall" in msg.text:
                       nk0 = msg.text.replace("#Unbanall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)			

            elif msg.text.lower() in ["Midd","midd"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                cl.sendText(msg.to,middd)


            elif msg.text == "กลุ่ม":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "ไม่พบผู้สร้างกลุ่ม"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                          u = "[ปิด]"
                        else:
                            u = "[เปิด]"
                        cl.sendText(msg.to,"[ชื่อของกลุ่ม]:\n" + str(ginfo.name) + "\n[Gid]:\n" + msg.to + "\n[ผู้สร้างกลุ่ม:]\n" + gCreator + "\n[ลิ้งค์รูปกลุ่ม]:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n[จำนวนสมาชิก]:" + str(len(ginfo.members)) + "คน\n[จำนวนค้างเชิญ]:" + sinvitee + "คน\n[สถานะลิ้งค์]:" + u + "URL [By: เพชร ทีมทดลองบอท]")
                    else:
                        cl.sendText(msg.to,"Nama Gourp:\n" + str(ginfo.name) + "\nGid:\n" + msg.to + "\nCreator:\n" + gCreator + "\nProfile:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                         cl.sendText(msg.to,"Not for use less than group")
            elif "Bot1@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*200 : (j+1)*200]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki1.sendMessage(msg)
            elif "Botall@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*200 : (j+1)*200]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki1.sendMessage(msg)
                    ki2.sendMessage(msg)
                    ki3.sendMessage(msg)
                    ki4.sendMessage(msg)
                    ki5.sendMessage(msg)
                    ki6.sendMessage(msg)
                    ki7.sendMessage(msg)
                    ki8.sendMessage(msg)
                    ki9.sendMessage(msg)
                    ki10.sendMessage(msg)
                    ki11.sendMessage(msg)
                    ki12.sendMessage(msg)
                    ki13.sendMessage(msg)
                    ki14.sendMessage(msg)
                    ki15.sendMessage(msg)

            elif msg.text in ["Bot?","เทส"]:
                ki1.sendText(msg.to,"Bot 1 􀜁􀅔􏿿")
                ki2.sendText(msg.to,"Bot 2 􀜁􀅔􏿿")
                ki3.sendText(msg.to,"Bot 3 􀜁􀅔􏿿")
                ki4.sendText(msg.to,"Bot 4 􀜁􀅔􏿿")
                ki5.sendText(msg.to,"Bot 5 􀜁􀅔􏿿")
                ki6.sendText(msg.to,"Bot 6 􀜁􀅔􏿿")
                ki7.sendText(msg.to,"Bot 7 􀜁􀅔􏿿")
                ki8.sendText(msg.to,"Bot 8 􀜁􀅔􏿿")
                ki9.sendText(msg.to,"Bot 9 􀜁􀅔􏿿")
                ki10.sendText(msg.to,"Bot 10 􀜁􀅔􏿿")

            elif "Phet Say " in msg.text:
                                bctxt = msg.text.replace("Phet Say ","")
                                ki1.sendText(msg.to,(bctxt))
                                ki2.sendText(msg.to,(bctxt))
                                ki3.sendText(msg.to,(bctxt))
                                ki4.sendText(msg.to,(bctxt))
                                ki5.sendText(msg.to,(bctxt))
                                ki6.sendText(msg.to,(bctxt))
                                ki7.sendText(msg.to,(bctxt))
                                ki8.sendText(msg.to,(bctxt))
                                ki9.sendText(msg.to,(bctxt))
                                ki10.sendText(msg.to,(bctxt))
                                ki11.sendText(msg.to,(bctxt))

            elif "All mid" == msg.text:
                ki1.sendText(msg.to,Amid1)
                ki2.sendText(msg.to,Amid2)
                ki3.sendText(msg.to,Amid3)
                ki4.sendText(msg.to,Amid4)
                ki5.sendText(msg.to,Amid5)
                ki6.sendText(msg.to,Amid6)
                ki7.sendText(msg.to,Amid7)
                ki8.sendText(msg.to,Amid8)
                ki9.sendText(msg.to,Amid9)
                ki10.sendText(msg.to,Amid10)
                ki11.sendText(msg.to,Amid11)

            elif msg.text in ["Protect:on","Protect on","เปิดป้องกัน"]:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))

                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกัน\n\n"+ datetime.today().strftime('%H:%M:%S'))

                    else:
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"มีการตั้งค่าป้องกันไว้อยู่แล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Qr:off","Qr off"]:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))

                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))

                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))

                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Qr:on","Qr on"]:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))

                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))

                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))

                    else:
                        cl.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"กลุ่มได้รับการตั้งค่าป้องกันQR\n\n"+ datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Protect:off","Protect off","ปิดป้องกัน"]:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))

                    else:
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))

                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))

                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki1.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki2.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki3.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki4.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki5.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki6.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki7.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki8.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki9.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        ki10.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))

            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                else:
                    cl.sendText(msg.to,"bone..")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"bone..")
					
            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"Done..")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"Done..")
				except:
					pass
            elif "Cn: " in msg.text:
                string = msg.text.replace("Cn: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif msg.text in ["invite:on"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif "Mc " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)

#-------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------#
            elif msg.text in ["K on","Contact:on","Contact on","K:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["contact v"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 random.choice(KAC).sendText(msg.to,"send contact")
            elif msg.text in ["K:off","Contact:off","Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif msg.text in ["Auto join on","Join on","Join:on","Auto join:on","Poin on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["Join off","Auto join off","Auto join:off","Join:off","Poin off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text in ["Leave:on","Auto leave on","Auto leave:on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")

            elif msg.text in ["Leave:off","Auto leave off","Auto leave:off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")

            elif msg.text in ["共有:オン","Share on","Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["共有:オフ","Share off","Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Auto like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Like off","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")

#========================================
#========================================
            elif msg.text in ["Set"]:
                print ("Setting pick up...")
                md = "─┅══ईह ㏒ Ᵽɧëȶ ㏒ ईह══┅─\n\n"
                if wait["likeOn"] == True: md+="􀔃􀅉􏿿 Auto like : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Auto like : off 􀜁􀄰􏿿\n"
                if wait["alwayRead"] == True: md+="􀔃􀅉􏿿 Read : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Read : off 􀜁􀄰􏿿\n"
                if wait["aalwayRead"] == True: md+="􀔃􀅉􏿿 Readbot : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Readbot : off 􀜁􀄰􏿿\n"
                if wait["detectMention"] == True: md+="􀔃􀅉􏿿 Autorespon : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Autorespon :􀜁􀄰􏿿\n"
                if wait["kickMention"] == True: md+="􀔃􀅉􏿿 Autokick: on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Autokick : off 􀜁􀄰􏿿\n"
                if wait["Notifed"] == True: md+="􀔃􀅉􏿿 Notifed : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Notifed : off 􀜁􀄰􏿿\n"
                if wait["Notifedbot"] == True: md+="􀔃􀅉􏿿 Notifedbot : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Notifedbot : off 􀜁􀄰􏿿\n"
                if wait["acommentOn"] == True: md+="􀔃􀅉􏿿 Hhx1 : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Hhx1 : off 􀜁􀄰􏿿\n"
                if wait["bcommentOn"] == True: md+="􀔃􀅉􏿿 Hhx2 : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Hhx2 : off 􀜁􀄰􏿿\n"
                if wait["ccommentOn"] == True: md+="􀔃􀅉􏿿 Hhx3 : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Hhx3 : off 􀜁􀄰􏿿\n"
                if wait["Protectcancl"] == True: md+="􀔃􀅉􏿿 Cancel : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Cancel : off 􀜁􀄰􏿿\n"
                if wait["winvite"] == True: md+="􀔃􀅉􏿿 Invite : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Invite : off 􀜁􀄰􏿿\n"
                if wait["pname"] == True: md+="􀔃􀅉􏿿 Namelock : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Namelock : off 􀜁􀄰􏿿\n"
                if wait["contact"] == True: md+="􀔃􀅉􏿿 Contact : on 􀜁􀄯􏿿\n"
                else: md+="􀔃􀅉􏿿 Contact : off 􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀔃􀅉􏿿 Auto join : on 􀜁􀄯􏿿\n"
                else: md +="􀔃􀅉􏿿 Auto join : off 􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀔃􀅉􏿿 Group cancel :" + str(wait["autoCancel"]["members"]) + " 􀜁􀄯􏿿\n"
                else: md+= "􀔃􀅉􏿿 Group cancel : off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀔃􀅉􏿿 Auto leave : on 􀜁􀄯􏿿\n"
                else: md+="􀔃􀅉􏿿 Auto leave : off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀔃􀅉􏿿 Share : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Share : off 􀜁􀄰􏿿\n"
                if wait["clock"] == True: md+="􀔃􀅉􏿿 Clock Name : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Clock Name : off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀔃􀅉􏿿 Auto add : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Auto add : off 􀜁􀄰􏿿\n"
                if wait["commentOn"] == True: md+="􀔃􀅉􏿿 Comment : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Comment : off 􀜁􀄰􏿿\n"
                if wait["Backup"] == True: md+="􀔃􀅉􏿿 Backup : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Backup : off 􀜁􀄰􏿿\n"
                if wait["qr"] == True: md+="􀔃􀅉􏿿 Protect QR : on 􀜁􀄯􏿿\n"
                else:md+="􀔃􀅉􏿿 Protect QR : off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
#========================================
#-----------------------------------------------
#------------------------------------------------
            elif msg.text in ["Gcreator:inv","เชิญเเอทมิน"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
            elif msg.text in ["Backup:on","Backup on","เปิดการเชิญกลับ"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off","Backup off","ปิดการเชิญกลับ"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Reject","ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Semua Spam Undangan Telah Di Tolak")
                else:
                    cl.sendText(msg.to,"Semua Spam Undangan Telah Di Tolak...")
            elif msg.text in ["Add:on","Auto add on","Auto add:on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah on Bosqu")
            elif msg.text in ["Add:off","Auto add off","Auto add:off","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah off Bosqu")
#========================================
#========================================
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Add message: " in msg.text:
                wait["message"] = msg.text.replace("Add message: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"done。\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Message","Com"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["message"])
            elif "Coms set:" in msg.text:
                c = msg.text.replace("Coms set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment: " in msg.text:
                c = msg.text.replace("Add comment: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)

            elif msg.text in ["Com on","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Com off","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Comment","Coms"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["HHX1","Hhx1"]:
                cl.sendText(msg.to,"[เช็คข้อความต้อนรับของคุณ]\n\n" + str(wait["acomment"]))

            elif msg.text in ["HHX2","Hhx2"]:
                cl.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนออกจากกลุ่ม]\n\n" + str(wait["bcomment"]))

            elif msg.text in ["HHX3","Hhx3"]:
                cl.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนลบสมาชิก]\n\n" + str(wait["ccomment"]))

            elif msg.text in ["Hhx1all4","hhx1all1"]:
                ki1.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
                ki2.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
                ki3.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
                ki4.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
                ki5.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
                ki6.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
                ki7.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
                ki8.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
                ki9.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
                ki10.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asacomment"]))
            elif msg.text in ["Hhx1all4","hhx1all1"]:
                ki1.sendText(msg.to,"[เช็คข้อความพิเศษออกกลุ่ม]\n\n" + str(wait["asbcomment"]))
                ki2.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asbcomment"]))
                ki3.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asbcomment"]))
                ki4.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asbcomment"]))
                ki5.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asbcomment"]))
                ki6.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asbcomment"]))
                ki7.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asbcomment"]))
                ki8.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asbcomment"]))
                ki9.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asbcomment"]))
                ki10.sendText(msg.to,"[เช็คข้อความพิเศษต้อนรับ]\n\n" + str(wait["asbcomment"]))
            elif msg.text in ["Hhx1all4","hhx1all1"]:
                ki1.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
                ki2.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
                ki3.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
                ki4.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
                ki5.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
                ki6.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
                ki7.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
                ki8.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
                ki9.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
                ki10.sendText(msg.to,"[เช็คข้อความพิเศษคนลบ]\n\n" + str(wait["asccomment"]))
            elif "Hhx1:" in msg.text:
                c = msg.text.replace("Hhx1:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["acomment"] = c
                    cl.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)

            elif "Hhx2:" in msg.text:
                c = msg.text.replace("Hhx2:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["bcomment"] = c
                    cl.sendText(msg.to,"➠ ตั้งค่าข้อความกล่าวถึงคนออกจากกลุ่ม👌\n\n" + c)

            elif "Hhx3:" in msg.text:
                c = msg.text.replace("Hhx3:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["ccomment"] = c
                    cl.sendText(msg.to,"➠ ตั้งค่าข้อความกล่าวถึงคนลบสมาชิก👌\n\n" + c)

            elif "Hhx1all:" in msg.text:
                c = msg.text.replace("Hhx1all:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["asacomment"] = c
                    ki1.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษต้อนรับ👌\n\n" + c)
                    ki2.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)
                    ki3.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)
                    ki4.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)
                    ki5.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)
                    ki6.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)
                    ki7.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)
                    ki8.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)
                    ki9.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)
                    ki10.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)
            elif "Hhx2all:" in msg.text:
                c = msg.text.replace("Hhx2all:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["asbcomment"] = c
                    ki1.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
                    ki2.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
                    ki3.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
                    ki4.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
                    ki5.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
                    ki6.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
                    ki7.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
                    ki8.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
                    ki9.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
                    ki10.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนออก👌\n\n" + c)
            elif "Hhx3all:" in msg.text:
                c = msg.text.replace("Hhx3all:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["asccomment"] = c
                    ki1.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
                    ki2.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
                    ki3.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
                    ki4.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
                    ki5.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
                    ki6.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
                    ki7.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
                    ki8.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
                    ki9.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
                    ki10.sendText(msg.to,"➠ ตั้งค่าข้อความพิเคษคนลบ👌\n\n" + c)
            elif msg.text in ["Hhx1 on"]:
                if wait["acommentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["acommentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Hhx2 on"]:
                if wait["bcommentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["bcommentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Hhx3 on"]:
                if wait["ccommentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["ccommentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already on")

            elif msg.text in ["Hhx1 off"]:
                if wait["acommentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["acommentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Hhx2 off"]:
                if wait["bcommentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["bcommentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Hhx3 off"]:
                if wait["ccommentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["ccommentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Hhx1all off"]:
                if wait["asacommentOn"] == False:
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                else:
                    wait["asacommentOn"] = False
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
            elif msg.text in ["Hhx2all off"]:
                if wait["asacommentOn"] == False:
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                else:
                    wait["asacommentOn"] = False
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Hhx3all off"]:
                if wait["asccommentOn"] == False:
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                else:
                    wait["asccommentOn"] = False
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
            elif msg.text in ["Hhx1all on"]:
                if wait["asacommentOn"] == True:
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki2.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki3.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki4.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki5.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki6.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki7.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki8.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki9.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki10.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                else:
                    wait["asacommentOn"] = True
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki2.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki3.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki4.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki5.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki6.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki7.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki8.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki9.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                        ki10.sendText(msg.to,"➠ เปิดข้อความพิเศษต้อนรับเเล้ว👌")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
            elif msg.text in ["Hhx2all on"]:
                if wait["asbcommentOn"] == True:
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki2.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki3.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki4.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki5.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki6.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki7.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki8.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki9.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki10.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                else:
                    wait["asbcommentOn"] = True
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki2.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki3.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki4.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki5.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki6.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki7.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki8.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki9.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                        ki10.sendText(msg.to,"➠ เปิดข้อความพิเศษคนออกเเล้ว👌")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
            elif msg.text in ["Hhx3all on"]:
                if wait["asccommentOn"] == True:
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki2.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki3.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki4.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki5.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki6.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki7.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki8.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki9.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki10.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
                else:
                    wait["asccommentOn"] = True
                    if wait["lang"] == "JP":
                        ki1.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki2.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki3.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki4.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki5.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki6.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki7.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki8.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki9.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                        ki10.sendText(msg.to,"➠ เปิดข้อความพิเศษคนลบเเล้ว👌")
                    else:
                        ki1.sendText(msg.to,"➠ Already on")
                        ki1.sendText(msg.to,"➠ Already on")
                        ki2.sendText(msg.to,"➠ Already on")
                        ki3.sendText(msg.to,"➠ Already on")
                        ki4.sendText(msg.to,"➠ Already on")
                        ki5.sendText(msg.to,"➠ Already on")
                        ki6.sendText(msg.to,"➠ Already on")
                        ki7.sendText(msg.to,"➠ Already on")
                        ki8.sendText(msg.to,"➠ Already on")
                        ki9.sendText(msg.to,"➠ Already on")
                        ki10.sendText(msg.to,"➠ Already on")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist s")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif msg.text in ["Clock:on","Clock on","Jam on","Jam:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")

            elif msg.text in ["Clock:off","Clock off","Jam off","Jam:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")

            elif "Cc: " in msg.text:
                n = msg.text.replace("Cc: ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Changed to:\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Refresh to update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

#========================================
            elif "Hack3 @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Hack3 @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithUrl(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Hack2mid:" in msg.text:
                umid = msg.text.replace("Hack2mid:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithUrl(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "Hack2 " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Hack2 ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithUrl(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")

#===============================================
            elif msg.text in ["Sp","sp","Speed"]:
                cl.sendText(msg.to, "Progress.......")
                start = time.time()
                time.sleep(0.001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
            elif msg.text in ["Bot Speed"]:
                ki1.sendText(msg.to, "Progress.......")
                start = time.time()
                time.sleep(0.001)
                elapsed_time = time.time() - start
                ki1.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki6.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki7.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki8.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki9.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki10.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki11.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki12.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki13.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki14.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki15.sendText(msg.to, "%sseconds" % (elapsed_time))

                print "[Command]Speed palsu executed"

            elif msg.text in ["Keybot"]:
                ki1.sendText(msg.to, "[SELFBOT PHET HACK BOT]\n\n❂͜͡☆➣ Namelock on\n❂͜͡☆➣ Namelock off\n❂͜͡☆➣ Blockinvite on\n❂��͜☆➣ Blockinvite off\n❂͜͡☆➣ Backup on\n❂͜͡☆➣ Backup off\n\n[By.เพชร ทีมทดลองบอท]")

#========================================
#========================================
            elif msg.text in ["Botcopyme"]:
                try:
                    ki1.updateDisplayPicture(mybackup.pictureStatus)
                    ki1.updateProfile(backup)
                    ki2.updateDisplayPicture(mybackup.pictureStatus)
                    ki2.updateProfile(backup)
                    ki3.updateDisplayPicture(mybackup.pictureStatus)
                    ki3.updateProfile(backup)
                    ki4.updateDisplayPicture(mybackup.pictureStatus)
                    ki4.updateProfile(backup)
                    ki5.updateDisplayPicture(mybackup.pictureStatus)
                    ki5.updateProfile(backup)
                    ki6.updateDisplayPicture(mybackup.pictureStatus)
                    ki6.updateProfile(backup)
                    ki7.updateDisplayPicture(mybackup.pictureStatus)
                    ki7.updateProfile(backup)
                    ki8.updateDisplayPicture(mybackup.pictureStatus)
                    ki8.updateProfile(backup)
                    ki9.updateDisplayPicture(mybackup.pictureStatus)
                    ki9.updateProfile(backup)
                    ki10.updateDisplayPicture(mybackup.pictureStatus)
                    ki10.updateProfile(backup)
                    ki11.updateDisplayPicture(mybackup.pictureStatus)
                    ki11.updateProfile(backup)
                    ki12.updateDisplayPicture(mybackup.pictureStatus)
                    ki12.updateProfile(backup)
                    ki13.updateDisplayPicture(mybackup.pictureStatus)
                    ki13.updateProfile(backup)
                    ki14.updateDisplayPicture(mybackup.pictureStatus)
                    ki14.updateProfile(backup)
                    ki15.updateDisplayPicture(mybackup.pictureStatus)
                    ki15.updateProfile(backup)
                    ki16.updateDisplayPicture(mybackup.pictureStatus)
                    ki16.updateProfile(backup)
                    ki17.updateDisplayPicture(mybackup.pictureStatus)
                    ki17.updateProfile(backup)
                    ki18.updateDisplayPicture(mybackup.pictureStatus)
                    ki18.updateProfile(backup)
                    ki19.updateDisplayPicture(mybackup.pictureStatus)
                    ki19.updateProfile(backup)
                    ki20.updateDisplayPicture(mybackup.pictureStatus)
                    ki20.updateProfile(backup)
                    ki21.updateDisplayPicture(mybackup.pictureStatus)
                    ki21.updateProfile(backup)
                    ki22.updateDisplayPicture(mybackup.pictureStatus)
                    ki22.updateProfile(backup)
                    ki23.updateDisplayPicture(mybackup.pictureStatus)
                    ki23.updateProfile(backup)
                    ki24.updateDisplayPicture(mybackup.pictureStatus)
                    ki24.updateProfile(backup)
                    ki25.updateDisplayPicture(mybackup.pictureStatus)
                    ki25.updateProfile(backup)
                    ki26.updateDisplayPicture(mybackup.pictureStatus)
                    ki26.updateProfile(backup)
                    ki26.updateDisplayPicture(mybackup.pictureStatus)
                    ki27.updateProfile(backup)
                    ki28.updateDisplayPicture(mybackup.pictureStatus)
                    ki28.updateProfile(backup)
                    ki29.updateDisplayPicture(mybackup.pictureStatus)
                    ki29.updateProfile(backup)
                    ki30.updateDisplayPicture(mybackup.pictureStatus)
                    ki30.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
            elif msg.text in ["Mebb"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

       #------------ Keluar Dari Semua Group------
            elif msg.text in ["phetallout"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in mid:
                gid = ki1.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = ki10.getGroupIdsJoined()
                gid = ki11.getGroupIdsJoined()
                gid = ki12.getGroupIdsJoined()
                gid = ki13.getGroupIdsJoined()
                gid = ki14.getGroupIdsJoined()
                gid = ki15.getGroupIdsJoined()
                gid = ki16.getGroupIdsJoined()
                gid = ki17.getGroupIdsJoined()
                gid = ki18.getGroupIdsJoined()
                gid = ki19.getGroupIdsJoined()
                gid = ki20.getGroupIdsJoined()
                gid = ki21.getGroupIdsJoined()
                gid = ki22.getGroupIdsJoined()
                gid = ki23.getGroupIdsJoined()
                gid = ki24.getGroupIdsJoined()
                gid = ki25.getGroupIdsJoined()
                gid = ki26.getGroupIdsJoined()
                gid = ki27.getGroupIdsJoined()
                gid = ki28.getGroupIdsJoined()
                gid = ki29.getGroupIdsJoined()
                gid = ki30.getGroupIdsJoined()
                for i in gid:
                  ki1.leaveGroup(i)
                  ki2.leaveGroup(i)
                  ki3.leaveGroup(i)
                  ki4.leaveGroup(i)
                  ki5.leaveGroup(i)
                  ki6.leaveGroup(i)
                  ki7.leaveGroup(i)
                  ki8.leaveGroup(i)
                  ki9.leaveGroup(i)
                  ki10.leaveGroup(i)
                  ki11.leaveGroup(i)
                  ki12.leaveGroup(i)
                  ki13.leaveGroup(i)
                  ki14.leaveGroup(i)
                  ki15.leaveGroup(i)
                  ki16.leaveGroup(i)
                  ki17.leaveGroup(i)
                  ki18.leaveGroup(i)
                  ki19.leaveGroup(i)
                  ki20.leaveGroup(i)
                  ki21.leaveGroup(i)
                  ki22.leaveGroup(i)
                  ki23.leaveGroup(i)
                  ki24.leaveGroup(i)
                  ki25.leaveGroup(i)
                  ki26.leaveGroup(i)
                  ki27.leaveGroup(i)
                  ki28.leaveGroup(i)
                  ki29.leaveGroup(i)
                  ki30.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Sayonara")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#=================================================
            elif msg.text == "#mid on":
                    cl.sendText(msg.to, "Done..")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "#mid off":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "%s\n\n%s\nReadig point creation:\n [%s]\n"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Lurking dulu dudul Baru bilang result Point.")
						
#========================================
#-------------------Fungsi spam finish----------------------------
            elif "Hackginfo" in msg.text:
              if msg.from_ in admin:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                        cl.sendImageWithUrl(msg.to,path)
            elif "#Turn off bots" in msg.text:
               if msg.from_ in admsa:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass

#-----------------------------------------------
            elif msg.text in ["Url","url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"[SELFBO PHET HACK BOT]\n\nline://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Notifed on","เปิดแจ้งเตือน","M on"]:
              if msg.from_ in admin:
                if wait["Notifed"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All Notifed On\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
                else:
                    wait["Notifed"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All Notifed On\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
            elif msg.text in ["Notifed off","ปิดแจ้งเตือน","M off"]:
              if msg.from_ in admin:
                if wait["Notifed"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All Notifed Off\n\nปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนของคุณเเล้ว")
                else:
                    wait["Notifed"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All Notifed Off\n\nปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนของคุณเเล้ว")

            elif msg.text in ["Notifedbot on","เปิดเเจ้งเตือนบอท","Mbot on"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed On\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                else:
                    wait["Notifedbot"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed On\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
            elif msg.text in ["Notifedbot off","ปิดแจ้งเตือนบอท","Mbot off"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed Off\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                else:
                    wait["Notifedbot"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed Off\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนบอทเเล้ว")

#=================================================
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
#-----------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-------------------------------------------------
            elif msg.text in ["Phet All on","Phet all on"]:
                        cl.sendText(msg.to,"─┅══ईह ㏒ Ᵽɧëȶ ㏒ ईह══┅─\n\n[SELF BOT PHET HACK BOT]")
                        cl.sendText(msg.to,"Please wait......")
                        cl.sendText(msg.to,"Turn on all protection")
                        cl.sendText(msg.to,"Qr:on")
                        cl.sendText(msg.to,"Backup:on")
                        cl.sendText(msg.to,"Read:on")
                        cl.sendText(msg.to,"Respon:on")
                        cl.sendText(msg.to,"Responkick:on")
                        cl.sendText(msg.to,"Protect:on")
                        cl.sendText(msg.to,"Namelock:on")
                        cl.sendText(msg.to,"Blockinvite:on")


            elif msg.text in ["Phet All off","Phet all off"]:
                        cl.sendText(msg.to,"─┅══ईह ㏒ Ᵽɧëȶ ㏒ ईह══┅─\n\n[SELF BOT PHET HACK BOT]")
                        cl.sendText(msg.to,"Please wait......")
                        cl.sendText(msg.to,"Turn off all protection")
                        cl.sendText(msg.to,"Qr:off")
                        cl.sendText(msg.to,"Backup:off")
                        cl.sendText(msg.to,"Read:off")
                        cl.sendText(msg.to,"Respon:off")
                        cl.sendText(msg.to,"Responkick:off")
                        cl.sendText(msg.to,"Protect:off")
                        cl.sendText(msg.to,"Namelock:off")
                        cl.sendText(msg.to,"Blockinvite:off")
                        cl.sendText(msg.to,"Link off")

 
            elif msg.text in ["ทีมงาน","ทีมทดลองบอท"]:
                msg.contentType = 13
                cl.sendText(msg.to, "[SELFBOT PHET HACK BOT]\n\n[☢Ŧ€₳M≈ನန้ণএ≈฿❂Ŧ☢]\n[By.ทีมงานทีมทดลองบอท]")
                cl.sendText(msg.to, "ผู้จัดการทีมงาน:🐯हईທຮຮๅજईह🐯")
                msg.contentMetadata = {'mid': 'u820d01252fdcf2a539fa194bcfc3400e'}
                cl.sendMessage(msg)
                cl.sendText(msg.to, "รองผู้จัดการทีมงาน:β•`BF.บั้ม•`")
                msg.contentMetadata = {'mid': 'u49974a7c78af9f3a8fec3e1dc7c646a9'}
                cl.sendMessage(msg)
                cl.sendText(msg.to, "ประธานใหญ่:เพชร ทีมทดลองบอท")
                msg.contentMetadata = {'mid': 'u00f827ce6641038d7c9b6704a9777dfa'}
                cl.sendMessage(msg)
                cl.sendText(msg.to, "ประธาน:ᴳᴜ ᵀᴇᵃᴍ ᴴa̴ᶜᴋ ᴮᴏᵀ")
                msg.contentMetadata = {'mid': 'u6eb517fae5d8de8d1845325e995196a7'}
                cl.sendMessage(msg)
                cl.sendText(msg.to, "รองประธาน:💫ীန้ສقัπั௭❁💫")
                msg.contentMetadata = {'mid': 'u765bec541d4f21cf0afdceb69b4b2ebd'}
                cl.sendMessage(msg)
                cl.sendText(msg.to, "รปภ.:✍Ŧ€₳M☬ж☬Ħ₳ʗҜ฿❂Ŧ✈๛")
                msg.contentMetadata = {'mid': 'u409892727431e6e682114336a3be2784'}
                cl.sendMessage(msg)
                cl.sendText(msg.to, "ตัวเเทนสมาชิก:🍃🍁NothingEid🍁🍃")
                msg.contentMetadata = {'mid': 'ue9e8dbdbfa31491ddc82ed73950b45f0'}
                cl.sendMessage(msg)
                cl.sendText(msg.to, "ตัวเเทนสมาชิก:Ĵöɱ💎Sтɪcκєʀᴸᶤᶰᵉ")
                msg.contentMetadata = {'mid': 'u76be42d134b394580644e1eed2bed029'}
                cl.sendMessage(msg)

#========================================
            elif "{}" in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to+"',"}
                cl.sendMessage(msg)
            elif "#####" in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to+"',"}
                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)

            elif '##########' in msg.text:
                if msg.toType == 2:
                    print "Kickall ok"
                    _name = msg.text.replace("##########","")
                    gs = ki1.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
                    gs = ki11.getGroup(msg.to)
                    gs = ki12.getGroup(msg.to)
                    gs = ki13.getGroup(msg.to)
                    gs = ki15.getGroup(msg.to)
                    gs = ki16.getGroup(msg.to)
                    gs = ki17.getGroup(msg.to)
                    gs = ki18.getGroup(msg.to)
                    gs = ki19.getGroup(msg.to)
                    gs = ki20.getGroup(msg.to)
                    gs = ki21.getGroup(msg.to)
                    gs = ki22.getGroup(msg.to)
                    gs = ki23.getGroup(msg.to)
                    gs = ki24.getGroup(msg.to)
                    gs = ki25.getGroup(msg.to)
                    gs = ki26.getGroup(msg.to)
                    gs = ki27.getGroup(msg.to)
                    gs = ki28.getGroup(msg.to)
                    gs = ki29.getGroup(msg.to)
                    gs = ki30.getGroup(msg.to)
                    ki1.sendText(msg.to, "พร้อมยังเทสแปป...😁😁 {}")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
#                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki1,ki2,ki3,ki4,ki5,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
#                                    ki3.sendText(msg,to,"Nuke Finish")
#                                    ki2.sendText(msg,to,"
            elif msg.text.lower() == '#rebot#':
                if msg.toType == 2:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"waitting...")
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
                        ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki21.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki22.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki23.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki24.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki25.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki26.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki27.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki28.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki29.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki30.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text.lower() == '#re#':
                if msg.toType == 2:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"waitting...")
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
                        ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki21.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki22.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki23.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki24.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki25.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki26.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki27.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki28.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki29.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki30.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
                        ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki21.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki22.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki23.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki24.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki25.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki26.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki27.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki28.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki29.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki30.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
                        ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki21.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki22.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki23.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki24.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki25.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki26.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki27.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki28.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki29.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki30.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
                        ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki21.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki22.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki23.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki24.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki25.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki26.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki27.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki28.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki29.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki30.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
                        ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki21.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki22.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki23.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki24.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki25.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki26.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki27.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki28.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki29.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki30.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
                        ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki21.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki22.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki23.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki24.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki25.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki26.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki27.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki28.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki29.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki30.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki30.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki30.updateGroup(G)

            elif ("PK4 " in msg.text):
				if msg.from_ in admin:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							ki6.kickoutFromGroup(msg.to,[target])
						except:
							ki6.sendText(msg.to,"Error")
							
            elif "KK2 " in msg.text:
                       nk0 = msg.text.replace("KK2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki2.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki2.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
							
            elif "KK1 " in msg.text:
                       nk0 = msg.text.replace("KK1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki1.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki1.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
#-----------------------------------------------

#-------------Fungsi Respon Start---------------------#
            elif msg.text in ["+++","..."]:
              if msg.from_ in admin:
                ki1.sendText(msg.to,"􀬁􀅴􏿿")
                ki2.sendText(msg.to,"􀬁􀅴􏿿􀬁􀅴􏿿")
                ki3.sendText(msg.to,"􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿")
                ki4.sendText(msg.to,"􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿")
                ki5.sendText(msg.to,"􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿")
                ki6.sendText(msg.to,"􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿")
                ki7.sendText(msg.to,"􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿")
                ki8.sendText(msg.to,"􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿")
                ki9.sendText(msg.to,"􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿")
                ki10.sendText(msg.to,"􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿􀬁􀅴􏿿")
#-------------Fungsi Respon Finish---------------------#
            elif ("PK2 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif ("PK3 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki3.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"Error")
            elif ("PK4 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki4.kickoutFromGroup(msg.to,[target])
                       except:
                           ki4.sendText(msg.to,"Error")
            elif ("PK5 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki5.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")
            elif ("PK6 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki6.kickoutFromGroup(msg.to,[target])
                       except:
                           ki6.sendText(msg.to,"Error")
            elif ("PK7 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki7.kickoutFromGroup(msg.to,[target])
                       except:
                           ki7.sendText(msg.to,"Error")
            elif ("PK8 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki8.kickoutFromGroup(msg.to,[target])
                       except:
                           ki8.sendText(msg.to,"Error")
            elif ("PK9 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki9.kickoutFromGroup(msg.to,[target])
                       except:
                           ki9.sendText(msg.to,"Error")
            elif ("PK10 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki10.kickoutFromGroup(msg.to,[target])
                       except:
                           ki10.sendText(msg.to,"Error")
            elif "Phet@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
            elif ("PK " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif "Blacklist @" in msg.text:
                _name = msg.text.replace("Blacklist @","")
                _kicktarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Success Boss")
                                except:
                                    cl.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Masuk daftar orang bejat Boss")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Sudah di keluarkan dari daftar bejat Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")
            elif msg.text in ["Clear ban","ล้างดำ"]:
				wait["blacklist"] = {}
				cl.sendText(msg.to,"clear")
				
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
			
            elif msg.text in ["Banlist","Mcheck"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[⎈]Blacklist [⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Me ban","Cekban","Mcheck mid"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[⎈]Mid Blacklist [⎈]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Pmcheck","เชคดำ","เช็คดำ"]:   
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="══════════List Blacklist═════════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n══════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
            elif msg.text in ["Mcheckcontact","Cb"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
#=============================================
                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Success deactive simisimi")
                
            elif msg.text in ["Read on","Read:on"]:
                wait['alwayRead'] = True
                cl.sendText(msg.to,"Auto Sider ON")
                
            elif msg.text in ["Read off","Read:off"]:
                wait['alwayRead'] = False
                cl.sendText(msg.to,"Auto Sider OFF")

            elif msg.text in ["Readbot on","Readbot:on"]:
                wait['aalwayRead'] = True
                cl.sendText(msg.to,"Auto Siderbot ON")
                
            elif msg.text in ["Readbot off","Readbot:off"]:
                wait['aalwayRead'] = False
                cl.sendText(msg.to,"Auto Siderbot OFF")
                
            elif msg.text in ["Tag on","Autorespon:on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                cl.sendText(msg.to,"Auto Respon ON")
                
            elif msg.text in ["Tag off","Autorespon:off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"Auto Respon OFF")
            
            elif msg.text in ["Kicktag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"Auto Kick ON")
                
            elif msg.text in ["Kicktag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"Auto Kick OFF")
            elif msg.text in ["Cancel on","cancel on","ปิดเชิญ"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off","เปิดเชิญ"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
#==============================================================================#
            elif msg.text in ["Blocklist","บร๊อก","Pbann"]: 
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["#Myginfoall"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["#Myginfogidall"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif "Gid" in msg.text:
                saya = msg.text.replace('Gid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
            elif "phet tag all" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "PHET TAG DONE :\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)

            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on\nเปิดการอ่านอัตโนมัต")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "เปิดการอ่านอัตโนมัต\nSet reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off\nปิดการอ่านอัตโนมัต")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ปิดการอ่านอัตโนมัต\nDelete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
            

            elif msg.text.lower() == 'gift1':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift2':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift3':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift4':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '4'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift5':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift6':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)

#------------------------------------------------
            elif msg.text in ["เวลา"]:
              if msg.from_ in admin:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'wc':
              if msg.from_ in mid:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#===========================================

            elif msg.text in ["เปิดอ่าน","R on","ตั้งเวลา"]:
                        cl.sendText(msg.to,"lurk on")
            elif msg.text in ["ปิดอ่าน","R off"]:
                        cl.sendText(msg.to,"lurk off")
            elif msg.text in ["อ่าน","Ry"]:
                        cl.sendText(msg.to,"lurkers")
            elif msg.text in ["Ry20"]:
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"llurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist","Heckmic"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "• "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Phetmic " in msg.text:
                cmd = msg.text.replace("Phetmic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
            elif "@pap:" in msg.text:
                wait["pap"] = msg.text.replace("@pap","")
                cl.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                cl.sendImageWithUrl(msg.to,wait["pap"])
            elif "@papvdo:" in msg.text:
                wait["pap"] = msg.text.replace("@papvdo:","")
                cl.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvdo","papvid"]:
                cl.sendVideoWithUrl(msg.to,wait["pap"])
#==============================================================================#
            elif msg.text in ["Sk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki2.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki3.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki3.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki4.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki5.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki6.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki7.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki8.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki9.sendMessage(msg)
            elif msg.text.lower() == 'mymid':
                cl.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Changed " + string + "")
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Changed " + string)
            elif "botallsts: " in msg.text:
                string = msg.text.replace("botallsts: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki1.getProfile()
                    profile.statusMessage = string
                    ki1.updateProfile(profile)
                    ki1.sendText(msg.to,"Changed " + string)
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"Changed " + string + "")
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"Changed " + string + "")
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"Changed " + string + "")
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"Changed " + string + "")
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"Changed " + string + "")
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"Changed " + string + "")
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"Changed " + string + "")
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"Changed " + string + "")
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"Changed " + string + "")
                    profile = ki11.getProfile()
                    profile.statusMessage = string
                    ki11.updateProfile(profile)
                    ki11.sendText(msg.to,"Changed " + string + "")
                    profile = ki12.getProfile()
                    profile.statusMessage = string
                    ki12.updateProfile(profile)
                    ki12.sendText(msg.to,"Changed " + string + "")
                    profile = ki13.getProfile()
                    profile.statusMessage = string
                    ki13.updateProfile(profile)
                    ki13.sendText(msg.to,"Changed " + string + "")
                    profile = ki14.getProfile()
                    profile.statusMessage = string
                    ki14.updateProfile(profile)
                    ki14.sendText(msg.to,"Changed " + string + "")
                    profile = ki15.getProfile()
                    profile.statusMessage = string
                    ki15.updateProfile(profile)
                    ki15.sendText(msg.to,"Changed " + string + "")
                    profile = ki16.getProfile()
                    profile.statusMessage = string
                    ki16.updateProfile(profile)
                    ki16.sendText(msg.to,"Changed " + string + "")
                    profile = ki17.getProfile()
                    profile.statusMessage = string
                    ki17.updateProfile(profile)
                    ki17.sendText(msg.to,"Changed " + string + "")
                    profile = ki18.getProfile()
                    profile.statusMessage = string
                    ki18.updateProfile(profile)
                    ki18.sendText(msg.to,"Changed " + string + "")
                    profile = ki19.getProfile()
                    profile.statusMessage = string
                    ki19.updateProfile(profile)
                    ki19.sendText(msg.to,"Changed " + string + "")
                    profile = ki20.getProfile()
                    profile.statusMessage = string
                    ki20.updateProfile(profile)
                    ki20.sendText(msg.to,"Changed " + string + "")
                    profile = ki21.getProfile()
                    profile.statusMessage = string
                    ki21.updateProfile(profile)
                    ki21.sendText(msg.to,"Changed " + string + "")
                    profile = ki22.getProfile()
                    profile.statusMessage = string
                    ki22.updateProfile(profile)
                    ki22.sendText(msg.to,"Changed " + string + "")
                    profile = ki23.getProfile()
                    profile.statusMessage = string
                    ki23.updateProfile(profile)
                    ki23.sendText(msg.to,"Changed " + string + "")
                    profile = ki24.getProfile()
                    profile.statusMessage = string
                    ki24.updateProfile(profile)
                    ki24.sendText(msg.to,"Changed " + string + "")
                    profile = ki25.getProfile()
                    profile.statusMessage = string
                    ki25.updateProfile(profile)
                    ki25.sendText(msg.to,"Changed " + string + "")
                    profile = ki26.getProfile()
                    profile.statusMessage = string
                    ki26.updateProfile(profile)
                    ki26.sendText(msg.to,"Changed " + string + "")
                    profile = ki27.getProfile()
                    profile.statusMessage = string
                    ki27.updateProfile(profile)
                    ki27.sendText(msg.to,"Changed " + string + "")
                    profile = ki28.getProfile()
                    profile.statusMessage = string
                    ki28.updateProfile(profile)
                    ki28.sendText(msg.to,"Changed " + string + "")
                    profile = ki29.getProfile()
                    profile.statusMessage = string
                    ki29.updateProfile(profile)
                    ki29.sendText(msg.to,"Changed " + string + "")
                    profile = ki30.getProfile()
                    profile.statusMessage = string
                    ki30.updateProfile(profile)
                    ki30.sendText(msg.to,"Changed " + string + "")
            elif "botallname: " in msg.text:
                string = msg.text.replace("botallname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki1.getProfile()
                    profile.displayName = string
                    ki1.updateProfile(profile)
                    ki1.sendText(msg.to,"Changed " + string + "")
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"Changed " + string + "")
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"Changed " + string + "")
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"Changed " + string + "")
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"Changed " + string + "")
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"Changed " + string + "")
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"Changed " + string + "")
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"Changed " + string + "")
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"Changed " + string + "")
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"Changed " + string + "")
                    profile = ki11.getProfile()
                    profile.displayName = string
                    ki11.updateProfile(profile)
                    ki11.sendText(msg.to,"Changed " + string + "")
                    profile = ki12.getProfile()
                    profile.displayName = string
                    ki12.updateProfile(profile)
                    ki12.sendText(msg.to,"Changed " + string + "")
                    profile = ki13.getProfile()
                    profile.displayName = string
                    ki13.updateProfile(profile)
                    ki13.sendText(msg.to,"Changed " + string + "")
                    profile = ki14.getProfile()
                    profile.displayName = string
                    ki14.updateProfile(profile)
                    ki14.sendText(msg.to,"Changed " + string + "")
                    profile = ki15.getProfile()
                    profile.displayName = string
                    ki15.updateProfile(profile)
                    ki15.sendText(msg.to,"Changed " + string + "")
                    profile = ki16.getProfile()
                    profile.displayName = string
                    ki16.updateProfile(profile)
                    ki16.sendText(msg.to,"Changed " + string + "")
                    profile = ki17.getProfile()
                    profile.displayName = string
                    ki17.updateProfile(profile)
                    ki17.sendText(msg.to,"Changed " + string + "")
                    profile = ki18.getProfile()
                    profile.displayName = string
                    ki18.updateProfile(profile)
                    ki18.sendText(msg.to,"Changed " + string + "")
                    profile = ki19.getProfile()
                    profile.displayName = string
                    ki19.updateProfile(profile)
                    ki19.sendText(msg.to,"Changed " + string + "")
                    profile = ki20.getProfile()
                    profile.displayName = string
                    ki20.updateProfile(profile)
                    ki20.sendText(msg.to,"Changed " + string + "")
                    profile = ki21.getProfile()
                    profile.displayName = string
                    ki21.updateProfile(profile)
                    ki21.sendText(msg.to,"Changed " + string + "")
                    profile = ki22.getProfile()
                    profile.displayName = string
                    ki22.updateProfile(profile)
                    ki22.sendText(msg.to,"Changed " + string + "")
                    profile = ki23.getProfile()
                    profile.displayName = string
                    ki23.updateProfile(profile)
                    ki23.sendText(msg.to,"Changed " + string + "")
                    profile = ki24.getProfile()
                    profile.displayName = string
                    ki24.updateProfile(profile)
                    ki24.sendText(msg.to,"Changed " + string + "")
                    profile = ki25.getProfile()
                    profile.displayName = string
                    ki25.updateProfile(profile)
                    ki25.sendText(msg.to,"Changed " + string + "")
                    profile = ki26.getProfile()
                    profile.displayName = string
                    ki26.updateProfile(profile)
                    ki26.sendText(msg.to,"Changed " + string + "")
                    profile = ki27.getProfile()
                    profile.displayName = string
                    ki27.updateProfile(profile)
                    ki27.sendText(msg.to,"Changed " + string + "")
                    profile = ki28.getProfile()
                    profile.displayName = string
                    ki28.updateProfile(profile)
                    ki28.sendText(msg.to,"Changed " + string + "")
                    profile = ki29.getProfile()
                    profile.displayName = string
                    ki29.updateProfile(profile)
                    ki29.sendText(msg.to,"Changed " + string + "")
                    profile = ki30.getProfile()
                    profile.displayName = string
                    ki30.updateProfile(profile)
                    ki30.sendText(msg.to,"Changed " + string + "")
            elif "botallname1: " in msg.text:
                string = msg.text.replace("botallname1: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki1.getProfile()
                    profile.displayName = string
                    ki1.updateProfile(profile)
                    ki1.sendText(msg.to,"Changed " + string + "")
            elif "botallname2: " in msg.text:
                string = msg.text.replace("botallname2: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"Changed " + string + "")
            elif "botallname3: " in msg.text:
                string = msg.text.replace("botallname3: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"Changed " + string + "")
            elif "botallname4: " in msg.text:
                string = msg.text.replace("botallname4: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"Changed " + string + "")
            elif "botallname5: " in msg.text:
                string = msg.text.replace("botallname5: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"Changed " + string + "")
            elif "botallname6: " in msg.text:
                string = msg.text.replace("botallname6: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"Changed " + string + "")
            elif "botallname7: " in msg.text:
                string = msg.text.replace("botallname7: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"Changed " + string + "")
            elif "botallname8: " in msg.text:
                string = msg.text.replace("botallname8: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"Changed " + string + "")
            elif "botallname9: " in msg.text:
                string = msg.text.replace("botallname9: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"Changed " + string + "")
            elif "botallname10: " in msg.text:
                string = msg.text.replace("botallname10: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"Changed " + string + "")
            elif "botallname11: " in msg.text:
                string = msg.text.replace("botallname11: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki11.getProfile()
                    profile.displayName = string
                    ki11.updateProfile(profile)
                    ki11.sendText(msg.to,"Changed " + string + "")
            elif "botallname12: " in msg.text:
                string = msg.text.replace("botallname12: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki12.getProfile()
                    profile.displayName = string
                    ki12.updateProfile(profile)
                    ki12.sendText(msg.to,"Changed " + string + "")
            elif "botallname13: " in msg.text:
                string = msg.text.replace("botallname13: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki13.getProfile()
                    profile.displayName = string
                    ki13.updateProfile(profile)
                    ki13.sendText(msg.to,"Changed " + string + "")
            elif "botallname14: " in msg.text:
                string = msg.text.replace("botallname14: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki14.getProfile()
                    profile.displayName = string
                    ki14.updateProfile(profile)
                    ki14.sendText(msg.to,"Changed " + string + "")
            elif "botallname15: " in msg.text:
                string = msg.text.replace("botallname15: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki15.getProfile()
                    profile.displayName = string
                    ki15.updateProfile(profile)
                    ki15.sendText(msg.to,"Changed " + string + "")
            elif "botallname16: " in msg.text:
                string = msg.text.replace("botallname16: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki16.getProfile()
                    profile.displayName = string
                    ki16.updateProfile(profile)
                    ki16.sendText(msg.to,"Changed " + string + "")
            elif "botallname17: " in msg.text:
                string = msg.text.replace("botallname17: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki17.getProfile()
                    profile.displayName = string
                    ki17.updateProfile(profile)
                    ki17.sendText(msg.to,"Changed " + string + "")
            elif "botallname18: " in msg.text:
                string = msg.text.replace("botallname18: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki18.getProfile()
                    profile.displayName = string
                    ki18.updateProfile(profile)
                    ki18.sendText(msg.to,"Changed " + string + "")
            elif "botallname19: " in msg.text:
                string = msg.text.replace("botallname19: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki19.getProfile()
                    profile.displayName = string
                    ki19.updateProfile(profile)
                    ki19.sendText(msg.to,"Changed " + string + "")
            elif "botallname20: " in msg.text:
                string = msg.text.replace("botallname20: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki20.getProfile()
                    profile.displayName = string
                    ki20.updateProfile(profile)
                    ki20.sendText(msg.to,"Changed " + string + "")
            elif "botallname21: " in msg.text:
                string = msg.text.replace("botallname21: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki21.getProfile()
                    profile.displayName = string
                    ki21.updateProfile(profile)
                    ki21.sendText(msg.to,"Changed " + string + "")
            elif "botallname22: " in msg.text:
                string = msg.text.replace("botallname22: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki22.getProfile()
                    profile.displayName = string
                    ki22.updateProfile(profile)
                    ki22.sendText(msg.to,"Changed " + string + "")
            elif "botallname23: " in msg.text:
                string = msg.text.replace("botallname23: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki23.getProfile()
                    profile.displayName = string
                    ki23.updateProfile(profile)
                    ki23.sendText(msg.to,"Changed " + string + "")
            elif "botallname24: " in msg.text:
                string = msg.text.replace("botallname24: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki24.getProfile()
                    profile.displayName = string
                    ki24.updateProfile(profile)
                    ki24.sendText(msg.to,"Changed " + string + "")
            elif "botallname25: " in msg.text:
                string = msg.text.replace("botallname25: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki25.getProfile()
                    profile.displayName = string
                    ki25.updateProfile(profile)
                    ki25.sendText(msg.to,"Changed " + string + "")
            elif "botallname26: " in msg.text:
                string = msg.text.replace("botallname26: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki26.getProfile()
                    profile.displayName = string
                    ki26.updateProfile(profile)
                    ki26.sendText(msg.to,"Changed " + string + "")
            elif "botallname27: " in msg.text:
                string = msg.text.replace("botallname27: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki27.getProfile()
                    profile.displayName = string
                    ki27.updateProfile(profile)
                    ki27.sendText(msg.to,"Changed " + string + "")
            elif "botallname28: " in msg.text:
                string = msg.text.replace("botallname28: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki28.getProfile()
                    profile.displayName = string
                    ki28.updateProfile(profile)
                    ki28.sendText(msg.to,"Changed " + string + "")
            elif "botallname29: " in msg.text:
                string = msg.text.replace("botallname29: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki29.getProfile()
                    profile.displayName = string
                    ki29.updateProfile(profile)
                    ki29.sendText(msg.to,"Changed " + string + "")
            elif "botallname30: " in msg.text:
                string = msg.text.replace("botallname30: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ki30.getProfile()
                    profile.displayName = string
                    ki30.updateProfile(profile)
                    ki30.sendText(msg.to,"Changed " + string + "")
            elif msg.text in ["Myname","Mename"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio","Mey1"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict","Mey2"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid","Mey3"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithUrl(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict","Mey4"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover","Mey5"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithUrl(msg.to, path)
            elif msg.text in ["Urlcover","Mey6"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
            elif "Ph2" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Ph" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "mh2" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithUrl(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithUrl(msg.to,path)
                except:
                    pass
            elif "#picall" in msg.text:
                       nk0 = msg.text.replace("#picall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    cl.sendImageWithUrl(msg.to, path)
                                except Exception as e:
                                    raise e
            elif "#botpicall" in msg.text:
                       nk0 = msg.text.replace("#botpicall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15]
                                    kicker = random.choice(klist)
                                    kicker.sendImageWithUrl(msg.to, path)
                                except Exception as e:
                                    raise e
            elif "#pictall" in msg.text:
                       nk0 = msg.text.replace("#pictall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    cu = cl.channel.getCover(target)
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    path = str(cu)
                                    cl.sendImageWithUrl(msg.to, path)
                                except Exception as e:
                                    raise e
            elif "#botpictall" in msg.text:
                       nk0 = msg.text.replace("#botpictall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    cu = cl.channel.getCover(target)
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    path = str(cu)
                                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15]
                                    kicker = random.choice(klist)
                                    kicker.sendImageWithUrl(msg.to, path)
                                except Exception as e:
                                    raise e
            elif "#phethackall" in msg.text:
                       nk0 = msg.text.replace("#phethackall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    cu = cl.channel.getCover(target)
                                    path = str(cu)
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    cl.sendText(msg.to,"Nama :\n" + contact.displayName)
                                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                    cl.sendImageWithUrl(msg.to,image)
                                    cl.sendText(msg.to,"Cover " + contact.displayName)
                                    cl.sendImageWithUrl(msg.to, path)
                                except Exception as e:
                                    raise e
            elif "#botphethackall" in msg.text:
                       nk0 = msg.text.replace("#botphethackall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    cu = cl.channel.getCover(target)
                                    path = str(cu)
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    cth.sendText(msg.to,"Nama :\n" + contact.displayName)
                                    cth.sendText(msg.to,"Profile Picture " + contact.displayName)
                                    cth.sendImageWithUrl(msg.to,image)
                                    cth.sendText(msg.to,"Cover " + contact.displayName)
                                    cth.sendImageWithUrl(msg.to, path)
                                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15]
                                    kicker = random.choice(klist)
                                    cth = kicker
                                    kicker.sendImageWithUrl(msg.to, path)
                                except Exception as e:
                                    raise e
            elif "เจ้งเตือน" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithUrl(msg.to,path)
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif "Botcopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Botcopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki1.CloneContactProfile(target)
                               ki1.sendText(msg.to, "Copied.")
                               ki2.CloneContactProfile(target)
                               ki2.sendText(msg.to, "Copied.")
                               ki3.CloneContactProfile(target)
                               ki3.sendText(msg.to, "Copied.")
                               ki4.CloneContactProfile(target)
                               ki4.sendText(msg.to, "Copied.")
                               ki5.CloneContactProfile(target)
                               ki5.sendText(msg.to, "Copied.")
                               ki6.CloneContactProfile(target)
                               ki6.sendText(msg.to, "Copied.")
                               ki7.CloneContactProfile(target)
                               ki7.sendText(msg.to, "Copied.")
                               ki8.CloneContactProfile(target)
                               ki8.sendText(msg.to, "Copied.")
                               ki9.CloneContactProfile(target)
                               ki9.sendText(msg.to, "Copied.")
                               ki10.CloneContactProfile(target)
                               ki10.sendText(msg.to, "Copied.")
                               ki11.CloneContactProfile(target)
                               ki11.sendText(msg.to, "Copied.")
                               ki12.CloneContactProfile(target)
                               ki12.sendText(msg.to, "Copied.")
                               ki13.CloneContactProfile(target)
                               ki13.sendText(msg.to, "Copied.")
                               ki14.CloneContactProfile(target)
                               ki14.sendText(msg.to, "Copied.")
                               ki15.CloneContactProfile(target)
                               ki15.sendText(msg.to, "Copied.")
                               ki16.CloneContactProfile(target)
                               ki16.sendText(msg.to, "Copied.")
                               ki17.CloneContactProfile(target)
                               ki17.sendText(msg.to, "Copied.")
                               ki18.CloneContactProfile(target)
                               ki19.sendText(msg.to, "Copied.")
                               ki18.CloneContactProfile(target)
                               ki18.sendText(msg.to, "Copied.")
                               ki19.CloneContactProfile(target)
                               ki19.sendText(msg.to, "Copied.")
                               ki20.CloneContactProfile(target)
                               ki20.sendText(msg.to, "Copied.")
                               ki20.CloneContactProfile(target)
                               ki20.sendText(msg.to, "Copied.")
                               ki21.CloneContactProfile(target)
                               ki21.sendText(msg.to, "Copied.")
                               ki22.CloneContactProfile(target)
                               ki22.sendText(msg.to, "Copied.")
                               ki23.CloneContactProfile(target)
                               ki23.sendText(msg.to, "Copied.")
                               ki24.CloneContactProfile(target)
                               ki24.sendText(msg.to, "Copied.")
                               ki25.CloneContactProfile(target)
                               ki25.sendText(msg.to, "Copied.")
                               ki26.CloneContactProfile(target)
                               ki26.sendText(msg.to, "Copied.")
                               ki27.CloneContactProfile(target)
                               ki27.sendText(msg.to, "Copied.")
                               ki28.CloneContactProfile(target)
                               ki28.sendText(msg.to, "Copied.")
                               ki29.CloneContactProfile(target)
                               ki29.sendText(msg.to, "Copied.")
                               ki30.CloneContactProfile(target)
                               ki30.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif "Google:" in msg.text:
                    a = msg.text.replace("Google:","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"Sedang Mencari...")
                    cl.sendText(msg.to, "https://www.google.com/" + b)
                    cl.sendText(msg.to,"Itu Dia Linknya. . .")     

#==============================================================================#
            elif "[Auto Respond]" in msg.text:
                cl.sendImageWithUrl(msg.to, "http://dl.profile.line.naver.jp/0hBUCWqWk8HXp-LjF_SHViLUJrExcJAAwyEB9QTAx7FxpbTVh_FkxSGg4uQkoAGAh4SxxaFFMtEU5Q")
            elif "Fancytext: " in msg.text:
                txt = msg.text.replace("Fancytext: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
            elif "Tx: " in msg.text:
                txt = msg.text.replace("Tx: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
            elif "Bx: " in msg.text:
                txt = msg.text.replace("Bx: ", "")
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)

                print "[Command] Kedapkedip"
            elif "Tx10: " in msg.text:
                txt = msg.text.replace("Tx10: ", "")
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
            elif "/vk " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("/vk ","")
                      wikipedia.set_lang("th")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithUrl(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
#==============================================#
            elif msg.text in ["in on"]:
              if msg.from_ in admin:
                if wait["pautoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["pautoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["in off"]:
              if msg.from_ in admin:
                if wait["pautoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["pautoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif "Hack4" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
#=============================================
            elif msg.text in ["!Sp"]:
                start = time.time()
                cl.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Bl " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned Bos")
                   except:
                      pass        
       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["#Cinvite"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact 😉")
            elif msg.text in ["Kill ban"]:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
#-------------------------------------------------------
            elif "Gift " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + "\nส่งให้เเล้วจร้าเช็คที่เเชทเลย..")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)
                                    cl.sendMessage(msg)

                                except:
                                    msg.contentMetadata = {'mid': target}

#========================================
#-------------------------------------------------------
            elif "Rungift " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Rungift ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + "\nรอแปปนะตะเองกำลังส่งไห้􀄃􀅹􏿿")
                                    ki1.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki2.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki3.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅��")
                                    ki4.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki5.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki6.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki7.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki8.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki9.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki10.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")

                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    ki1.sendMessage(msg)
                                    ki2.sendMessage(msg)
                                    ki3.sendMessage(msg)
                                    ki3.sendMessage(msg)
                                    ki4.sendMessage(msg)
                                    ki5.sendMessage(msg)
                                    ki6.sendMessage(msg)
                                    ki7.sendMessage(msg)
                                    ki8.sendMessage(msg)
                                    ki9.sendMessage(msg)
                                    ki10.sendMessage(msg)

                                    ki1.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki2.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki3.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki4.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki5.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki6.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki7.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki8.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki9.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")
                                    ki10.sendText(msg.to,_name + "\nส่งเรียบร้อยละจร้า􀄃􀇅􏿿")

                                except:
                                    msg.contentMetadata = {'mid': target}
#========================================
            elif msg.text in ["Name me","MeMe"]:
                G = cl.getProfile()
                X = G.displayName
                cl.sendText(msg.to,X)
            elif "siri:" in msg.text.lower():
                    query = msg.text.lower().replace("siri:","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)
            elif "พูด " in msg.text.lower():
                    query = msg.text.lower().replace("พูด ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)
            elif msg.text in ["1in","Bot1 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text in ["2in","Bot2 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
            elif msg.text in ["3in","Bot3 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
            elif msg.text in ["4in","Bot4 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki4.updateGroup(G)
            elif msg.text in ["5in","Bot5 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
            elif msg.text in ["6in","Bot6 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
            elif msg.text in ["7in","Bot7 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
            elif msg.text in ["8in","Bot8 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
            elif msg.text in ["9in","Bot9 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
            elif msg.text in ["10in","Bot10 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
#RUNTIME--------------------------------------
            elif msg.text.lower() == "runtime":
                cl.sendText(msg.to, "Wait....")
                cl.sendText(msg.to,str(datetime.now() - start_runtime)[:-7].split(":")[0]+" Hour "+str(datetime.now() - start_runtime)[:-7].split(":")[1]+" Minute "+str(datetime.now() - start_runtime)[:-7].split(":")[2]+" second")
#----------------------------------------------
#RUNTIME--------------------------------------
            elif msg.text.lower() == "ออน":
                cl.sendText(msg.to, "Wait....")
                cl.sendText(msg.to,str(datetime.now() - start_runtime)[:-7].split(":")[0]+" ชั่วโมง "+str(datetime.now() - start_runtime)[:-7].split(":")[1]+" นาที "+str(datetime.now() - start_runtime)[:-7].split(":")[2]+" วินาที")


            elif "#กูไปละ" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)

                    except:
                        pass

            elif "[Auto] " in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("[Auto] ","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
            elif "☜ʕ•ﻌ•ʔ " in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("☜ʕ•ﻌ•ʔ ","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                ki1.sendText(msg.to, "[ChatBOT] " + data['result']['response'].encode('utf-8'))
            elif msg.text in ["teston"]:
                        cl.sendText(msg.to,"SELFBOT PHETHACK BOT")
            elif msg.text in [".อยู่ไหม"]:
                        cl.sendText(msg.to,"อยู่...")
            elif msg.text in ["/อยู่ไหม"]:
                        cl.sendText(msg.to,"เรื่องของกู...")
            elif "/ตั้งเวลา" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on\nเปิดการอ่านอัตโนมัตกรุณาพิมพ์ ➠ /อ่าน")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "โปรเเกรมเปิดการอ่านอัตโนมัต\nSet reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "/ปิดการอ่าน" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off\nปิดการอ่านอัตโนมัต")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ปิดการอ่านอัตโนมัต\nDelete reading point:\n" + datetime.now().strftime('%H:%M:%S'))

                    
            elif "/อ่าน" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "SELFBOT PHET HACK BOT\n\nLurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "กรุณาตั้งเวลาการอ่านใหม่อีกครั้งโปรดพิมพ์ ➠ /ตั้งเวลา")
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to, "[อัตโนมัติ]: " + text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            			"STKID": "6",
            			"STKPKGID": "1",            						"STKVER": "100" }
            			cl.sendMessage(msg)
            elif msg.text.lower() in ["hi"]:
                    beb = "Hi Sayang 😘 " +cl.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    cl.sendText(msg.to,beb)
            elif msg.text.lower() in ["พี่เพชร","เพชร"]:
                    beb = "เรียกทำไม 😘 " +cl.getContact(msg.from_).displayName + "เหงาหรื่อเงี่ยน"
                    cl.sendText(msg.to,beb)
            elif msg.text.lower() in ["Mid","mid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                cl.sendText(msg.to,middd)

        if op.type == 15:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀄄􏿿 เเล้วพบใหม่นะ 􀜁􀄄􏿿")
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + " ☜ʕ•ﻌ•ʔ ")
                cl.sendText(op.param1, "􀜁􀄁􏿿 ยินดีต้อนรับครับ 􀜁􀄁􏿿\n􀄃􀅸􏿿 สวัสดีครับผม 􀄃􀅸􏿿\n􂜁􀆄􏿿 อย่าลืมปิดเสียงการเเจ้งเตือนด้วยนะ 􂜁􀆄􏿿\n\n[By.เพชร ทีมทดลองบอท]")
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 19:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.type == 15:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄄􏿿 Bye~bye 􀜁􀄄􏿿")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄄􏿿 Bye~bye 􀜁􀄄􏿿")
                print "MEMBER OUT GROUP"


        if op.type == 17:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄁􏿿􂘁􀄗􏿿􂘁􀄅􏿿􂘁􀄌􏿿􂘁􀄃􏿿􂘁􀄏􏿿􂘁􀄍􏿿􂘁􀄅􏿿􀜁􀄁􏿿\n\n[By. เพชร ทีมทดลองบอท]")

                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 19:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.type == 15:
            if wait["bcommentOn"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["bcomment"]))
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["acommentOn"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["acomment"]))
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 19:
            if wait["ccommentOn"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["ccomment"]))
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.type == 15:
            if wait["asbcommentOn"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,ki1.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                ki2.sendText(op.param1,ki2.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                ki3.sendText(op.param1,ki3.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                ki4.sendText(op.param1,ki4.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                ki5.sendText(op.param1,ki5.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                ki6.sendText(op.param1,ki6.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                ki7.sendText(op.param1,ki7.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                ki8.sendText(op.param1,ki8.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                ki9.sendText(op.param1,ki9.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                ki10.sendText(op.param1,ki10.getContact(op.param2).displayName + "\n" + str(wait["asbcomment"]))
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                ki1.sendImageWithUrl(op.param1,image)
                print "MEMBER OUT GROUP"
        if op.type == 17:
            if wait["asacommentOn"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,ki1.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                ki2.sendText(op.param1,ki2.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                ki3.sendText(op.param1,ki3.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                ki4.sendText(op.param1,ki4.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                ki5.sendText(op.param1,ki5.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                ki6.sendText(op.param1,ki6.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                ki7.sendText(op.param1,ki7.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                ki8.sendText(op.param1,ki8.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                ki9.sendText(op.param1,ki9.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                ki10.sendText(op.param1,ki10.getContact(op.param2).displayName + "\n" + str(wait["asacomment"]))
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                ki1.sendImageWithUrl(op.param1,image)
                print "MEMBER OUT GROUP"
        if op.type == 19:
            if wait["asccommentOn"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,ki1.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                ki2.sendText(op.param1,ki2.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                ki3.sendText(op.param1,ki3.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                ki4.sendText(op.param1,ki4.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                ki5.sendText(op.param1,ki5.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                ki6.sendText(op.param1,ki6.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                ki7.sendText(op.param1,ki7.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                ki8.sendText(op.param1,ki8.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                ki9.sendText(op.param1,ki9.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                ki10.sendText(op.param1,ki10.getContact(op.param2).displayName + "\n" + str(wait["asccomment"]))
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                ki1.sendImageWithUrl(op.param1,image)
                print "MEMBER OUT GROUP"
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)

        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error


def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autolike)
thread1.daemon = True
thread1.start()


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
    
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
