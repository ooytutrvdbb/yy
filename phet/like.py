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

#cl = LINETCR.LINE()
#cl.login(token="EpmVUtWixr5UaRv8ouka.apGNZMzba418M2CeQxD9/G.C7YCDezGGrclGv0gQ2BtuPZjpQiJV/YIQO33i2NFCVo=")
#cl.loginResult()

ki1 = LINETCR.LINE()
ki1.login(token="EpGlIbYdgQW2erQ6wp32.Tp+2DgIZ3zX4aseyVxboKG.uIjAIA9biyjnxYd4Wnf4OcZW+uKoKqjAduqKfvPIcdI=")
ki1.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EpDQLePnfYjbvmZhqZ99.8zdD5KVVm93F+f9Qbktt/q.OmG0vvUoVPQSm5qJwbFud+0LjRbf8bBHz4TCG0AYBiQ=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Ep3Q9zAki1nhm2Zjy9uf.dNBs/Ys/puxDk2XazUUBRW.2USaVCXWhDHEIOz+/Ad07CKBswrUXYokOf+H97DnXc0=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EpIq85Gmh715l0JHUzxd.rHmdTXsLiNLo2z/kRLt+hq.fpL+7vZVZl8HUACmeO3VfJBufCpvbYYq9SvN8nBGOsw=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="Ep3g3gBquE39hoZYcvBc.EZg/zoOGM6cbGX3GoOipxa.fAI+CESfsdcj+y2UbuXFp2fvmRTc0Pw7z2aYeQLnkBA=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EpdVZCeA6ZiS7srNIG73.Qt4DQz3PcTDk9RXedVuBOW.zY9shkw5X73Q2xMefYFobH5GffgwLXTZTVvFvatepzk=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="EpBcE4Q6vB9OhAldwPy1.dAbFu5qDJ6YPw1jeyKhVKq.meyZtt2mMNlK11k9rp9xtF/nBnsnk1cO6GPiyjkJdiQ=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EpqqBUZ3n7ufK3GmK0i9.fgus0a7u5LoEfs9YS70wwq.0vHUpZog9/3RfsjOFBVpjvnQa3wzDWf9Y4WRRZOzqs4=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EpR0pUOPbxVj6FeLf16b.4ajeBU5zEw8GFrMR1B9yUW.eGXpKGPQAemELp0922KEiDx3MxCZDioRSn1ayjeTf8s=")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="EpMlcLJEjHCwfragPt5a.+snuuxSMcQBLjXVJitdSEG.BZVdZC/xrC0GNuGY5az/2PN4u8dEKiyyCTDV9ZncKFQ=")
ki10.loginResult()

ki11 = LINETCR.LINE()
ki11.login(token="EpZkjNCbabdXXAGwBEsc.pGCREjIcGYFHnnvOIUtTda.2PO3LYz84+hqH6szf4S4Ykfv3kx5wbWIz94s5/YATfY=")
ki11.loginResult()

ki12 = LINETCR.LINE()
ki12.login(token="EpDHAYrDDaHUJaAcODW6.1rfIy/E83J50WHhH6XYgbG.yql8FCD39vqu8KPCgMTTT1Xy1c6KXBGZ6j5802MxUxc=")
ki12.loginResult()

ki13 = LINETCR.LINE()
ki13.login(token="Epw8urfgei10EBpn6vb9.S3plAjwW+0enAh9WB20YYq.Gf15l1jSz5agPShOrTHlzFi/ldHvLeG9rvw20mrdzjw=")
ki13.loginResult()

ki14 = LINETCR.LINE()
ki14.login(token="EpzbDu3lUUJ5vIHOgQSc.GyqJDAN7UOhmlSK1F0bKFa.uvYS8XuRJSPICGkr/lXePkK6JpJMgyko4C3OYx3UUC8=")
ki14.loginResult()

ki15 = LINETCR.LINE()
ki15.login(token="Epx9eNT1H9lSKzqCphJ0.YQgIMwLeV3oxvR5G0dnHya.cyXqADq5zmM3sR3dChGVgVNPqRwy/eLSsuhaMOhWORo=")
ki15.loginResult()

ki16 = LINETCR.LINE()
ki16.login(token="EpkgMkhmsJLrsIicBhte.vABFWhFVuF9fRmkg6+bVFG.ney2nljoFtspw3i0Sb7MxBCuRYdqAIgVd2SKPer4xEo=")
ki16.loginResult()

ki17 = LINETCR.LINE()
ki17.login(token="Ep3i0GjYwZDRrBe6MrPc.ZHFtUEUDt3xzxAUi6j9PJa.nOSD9OVCLphubSfSS8x7g0hz3KNXwUpS7RxzC500OvU=")
ki17.loginResult()

ki18 = LINETCR.LINE()
ki18.login(token="Ep3x4ALCULw0Y1eJIJu3.AFjFi3Id/gpOgrtYTfhSyW.5ChJ94ytRhiwyDUhRPveZp+4ucr3DNlR/gJ6xVZuxhA=")
ki18.loginResult()

ki19 = LINETCR.LINE()
ki19.login(token="EpWainlUJ7YNBqLnui04.d7q7Ld0cvCtKVuAIRXmATa.gOBnvvB6+WPNKvoet6QTqa21z33HXMpoAbFna0IwK60=")
ki19.loginResult()

ki20 = LINETCR.LINE()
ki20.login(token="EpYgveLYkIDIAeHvSoG3.B0swIiVnBEVbkClvmS4KaW.SgSlTmaIAqowccUuWVaGieLrkrK54B1Sv8+Ukyrg8B4=")
ki20.loginResult()

ki21 = LINETCR.LINE()
ki21.login(token="Ep6lBQXHOOTqueldOEp9.wJ+pQr0LE4r+B8fQrUJGsq.nbxijXWEbYZuKszATf/s7tr4VAdAZ/otPudQw3BErd8=")
ki21.loginResult()

ki22 = LINETCR.LINE()
ki22.login(token="EpB7HumURI9w8WhiSYEa.MfTKqhz+PM+X2QRY9830AG.BRFBlH2b7hR/fvs5q3n6tbpSQS0JfQoEmq/4D4MmEsU=")
ki22.loginResult()

ki23 = LINETCR.LINE()
ki23.login(token="EpzUl3lnvKgRcOizQK78.97UN36ECvAYPTrF82bSAMa.Shnhoc5pmq50sVArxHXZxLzOnotxWdJ/0a5Qml1ATv8=")
ki23.loginResult()

ki24 = LINETCR.LINE()
ki24.login(token="EpgUMMr7Hglvb4gRRJB7.8WXlhPISVfvSwZVCMm8trW.pZ3vfgVaNrmz4nq+RewwaCANQMNBpq7eOvvNfz4gOf8=")
ki24.loginResult()

ki25 = LINETCR.LINE()
ki25.login(token="EpkUpViWvSLaAeCWlai6.3gbXCx+35kvbr3Aa1GclLG.puD8ZTCKFHau1u3jRXGh/BaVhvglbHreUdAnV1sx+qA=")
ki25.loginResult()

ki26 = LINETCR.LINE()
ki26.login(token="EpbVjzWcbIa52c0SnA87.yiVhtGqFXEogTBSsvAEAjW.L7n20m9UTK4+RF5nGSpvpMzIEaI2wfmVYOqdFj04Hyg=")
ki26.loginResult()

ki27 = LINETCR.LINE()
ki27.login(token="Ep6RMvftIv7pMjC1FEsd.UPsHSev3CJF/OIop2wEMhq.2o0+hm+QqH+NFPAYyg18KZjNp4iVfOoMj8GZjF5+nE4=")
ki27.loginResult()

ki28 = LINETCR.LINE()
ki28.login(token="EpWkNKk46RyHzhnd0A7b.PNd7qLcczJW00ek2Ow2qMW.p+tMHblhZ7BqdZwDKTi4lPHTac+CIzq7G90thYeP6HY=")
ki28.loginResult()

ki29 = LINETCR.LINE()
ki29.login(token="EpqRYjTPkbivUkKL0LO6.O3P+/622/qxgUZ4VNaxKbG.2e7UBliAdmZvDiUgwNLsx2bIpp88jkQo5RAMYvMmgA8=")
ki29.loginResult()

ki30 = LINETCR.LINE()
ki30.login(token="Ep4srgZX7WihOEQQRmW6.wuRsY0/V927nD9OY59WnPG.KW5uBuLKLUwbvlvuKaPnqmM15ezLlQfqszfL3vo7D/A=")
ki30.loginResult()
cl = ki30
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
    'autoJoin':False,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':True,
    'timeline':False,
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
    "clock":False,
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
	"posts":True,
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
            if msg.contentType == 16:
                url = msg.contentMetadata['postEndUrl']
                ki1.like(url[25:58], url[66:], likeType=1001)
                ki1.comment(url[25:58], url[66:], wait["comment1"])
                ki2.like(url[25:58], url[66:], likeType=1001)
                ki2.comment(url[25:58], url[66:], wait["comment1"])
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki4.comment(url[25:58], url[66:], wait["comment1"])
                ki5.like(url[25:58], url[66:], likeType=1001)
                ki5.comment(url[25:58], url[66:], wait["comment1"])
                ki6.like(url[25:58], url[66:], likeType=1001)
                ki6.comment(url[25:58], url[66:], wait["comment1"])
                ki7.like(url[25:58], url[66:], likeType=1001)
                ki7.comment(url[25:58], url[66:], wait["comment1"])
                ki8.like(url[25:58], url[66:], likeType=1001)
                ki8.comment(url[25:58], url[66:], wait["comment1"])
                ki9.like(url[25:58], url[66:], likeType=1001)
                ki9.comment(url[25:58], url[66:], wait["comment1"])
                ki10.like(url[25:58], url[66:], likeType=1001)
                ki10.comment(url[25:58], url[66:], wait["comment1"])
                ki11.like(url[25:58], url[66:], likeType=1001)
                ki11.comment(url[25:58], url[66:], wait["comment1"])
                ki12.like(url[25:58], url[66:], likeType=1001)
                ki12.comment(url[25:58], url[66:], wait["comment1"])
                ki13.like(url[25:58], url[66:], likeType=1001)
                ki13.comment(url[25:58], url[66:], wait["comment1"])
                ki14.like(url[25:58], url[66:], likeType=1001)
                ki14.comment(url[25:58], url[66:], wait["comment1"])
                ki15.like(url[25:58], url[66:], likeType=1001)
                ki15.comment(url[25:58], url[66:], wait["comment1"])
                ki16.like(url[25:58], url[66:], likeType=1001)
                ki16.comment(url[25:58], url[66:], wait["comment1"])
                ki17.like(url[25:58], url[66:], likeType=1001)
                ki17.comment(url[25:58], url[66:], wait["comment1"])
                ki18.like(url[25:58], url[66:], likeType=1001)
                ki18.comment(url[25:58], url[66:], wait["comment1"])
                ki19.like(url[25:58], url[66:], likeType=1001)
                ki19.comment(url[25:58], url[66:], wait["comment1"])
                ki20.like(url[25:58], url[66:], likeType=1001)
                ki20.comment(url[25:58], url[66:], wait["comment1"])
                ki21.like(url[25:58], url[66:], likeType=1001)
                ki21.comment(url[25:58], url[66:], wait["comment1"])
                ki22.like(url[25:58], url[66:], likeType=1001)
                ki23.comment(url[25:58], url[66:], wait["comment1"])
                ki23.like(url[25:58], url[66:], likeType=1001)
                ki24.comment(url[25:58], url[66:], wait["comment1"])
                ki24.like(url[25:58], url[66:], likeType=1001)
                ki25.comment(url[25:58], url[66:], wait["comment1"])
                ki26.like(url[25:58], url[66:], likeType=1001)
                ki26.comment(url[25:58], url[66:], wait["comment1"])
                ki27.like(url[25:58], url[66:], likeType=1001)
                ki27.comment(url[25:58], url[66:], wait["comment1"])
                ki28.like(url[25:58], url[66:], likeType=1001)
                ki28.comment(url[25:58], url[66:], wait["comment1"])
                ki29.like(url[25:58], url[66:], likeType=1001)
                ki29.comment(url[25:58], url[66:], wait["comment1"])
                ki30.like(url[25:58], url[66:], likeType=1001)
                ki30.comment(url[25:58], url[66:], wait["comment1"])
                print ("AUTO LIKE SELFBOT")
                print ("Auto Like By. เพชร ทีมทดลองบอท")
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
