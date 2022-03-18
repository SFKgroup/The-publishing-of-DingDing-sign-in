import os
import time
from random import *
import xml.dom.minidom
from datetime import datetime
def desktop():
    os.system('adb shell input tap 539 2275')
    time.sleep(random()+0.5)
    os.system('adb shell input tap 539 2275')
    time.sleep(random()+0.5)
    os.system('adb shell input tap 539 2275')
    time.sleep(random()+0.5)

def kill():
    os.system('adb shell input tap 777 2275')
    time.sleep(random()+0.3)
    os.system('adb shell input tap 533 1960')
    time.sleep(random()+0.3)

def open_ding(wlist):
    for w in wlist:
        if w[0] == 'findclick':
            find_click(w[1],my=-100,way=w[2])
        elif w[0] == 'click':
            get_xml('D:\\xml.xml')
            dtl,bdl = read_xml('D:\\xml.xml')
            click(w[1],dtl,bdl,my=-100)

def get_xml(save):
    os.system('adb shell /system/bin/uiautomator dump /data/local/tmp/liukangUi.xml')
    if os.system('adb pull /data/local/tmp/liukangUi.xml '+save) == 1:
        grand = open(save,'w')
        grand.close()
        if os.system('adb pull /data/local/tmp/liukangUi.xml '+save) == 1:print('Wrong dir:',save)

def read_xml(save):
    data_list = []
    bound_list = []
    DOMTree = xml.dom.minidom.parse(save)
    collection = DOMTree.documentElement
    for tag in collection.getElementsByTagName("node"):
        data = tag.getAttribute("text")
        if data == '':data = tag.getAttribute("content-desc")
        if data != '':
            bound = tag.getAttribute("bounds").replace('][',',').replace(']','').replace('[','').split(',')
            bound_list.append([int(bound[0]),int(bound[1]),int(bound[2]),int(bound[3])])
            data_list.append(data)
    return data_list,bound_list


def find_click(string,way='up',mx=0,my=0,lim=3):#way为翻页方向(与滑动方向反向)
    get_xml('D:\\xml.xml')
    dtl,bdl = read_xml('D:\\xml.xml')
    old = dtl
    while click(string,dtl,bdl,mx,my) == 1:
        if way == 'up':os.system('adb shell input swipe 550 900 540 1700')
        elif way == 'down':os.system('adb shell input swipe 540 1600 550 800')
        elif way == 'left':os.system('adb shell input swipe 200 1077 966 1077')
        elif way == 'right':os.system('adb shell input swipe 966 1077 200 1077')
        time.sleep(random()+0.5)
        get_xml('D:\\xml.xml')
        dtl,bdl = read_xml('D:\\xml.xml')
        if len(list(set(old).difference(set(dtl)))) + len(list(set(dtl).difference(set(old)))) <= lim:return 1
        old = dtl
    return 0

def click(string,data,bound,mx=0,my=0,t=0.3):
    x = ''
    y = ''
    for d,b in zip(data,bound):
        if d == string:
            x = str(round((b[0]+b[2])/2)+mx)
            y = str(round((b[1]+b[3])/2)+my)
            break
    if x != '' and y != '':
        os.system('adb shell input tap ' + x + ' ' + y)
        time.sleep(random()+t)
        return 0
    else:return 1

def getact(save):
    os.system('adb shell dumpsys window policy > ' + save)
    grand = open(save)
    data = grand.readlines()
    grand.close()
    ret = {}
    for i in data:
        d = i.replace('\n','').replace('  ','')
        if '=' in d and not('#' in d) and not('(' in d):
            dl = d.split('=')
            if dl[1] == 'true':dv = True
            elif dl[1] == 'false':dv = False
            elif dl[1] == 'null':dv = None
            else:
                try:dv = int(dl[1])
                except:dv = dl[1]
            ret[dl[0]] = dv
    return ret

def unlock(key):
    act = getact('D:\\data.txt')
    
    if act['showing'] and act['mIsShowing']:
        os.system('adb shell input keyevent 26')
        time.sleep(random()+0.6)
        os.system('adb shell input swipe 540 1600 550 800')
        time.sleep(random()+0.3)
        get_xml('D:\\xml.xml')
        dtl,bdl = read_xml('D:\\xml.xml')
        for k in key.split('-'):
            for a in k:click(a,dtl,bdl,t=0.1)
            click('!?#',dtl,bdl)
            get_xml('D:\\xml.xml')
            dtl,bdl = read_xml('D:\\xml.xml')
            click('-',dtl,bdl)
            get_xml('D:\\xml.xml')
            dtl,bdl = read_xml('D:\\xml.xml')
        os.system('adb shell input tap 965 1953')
        time.sleep(random()+0.3)
        os.system('adb shell input tap 895 2115')
        time.sleep(random()+0.3)
    else:print('Already unlocked')

def make_check(pass_word,way):
    unlock(pass_word)
    desktop()
    kill()
    open_ding(way)
    time.sleep(random()+4)
    find_click('一年级4班','down')
    time.sleep(random()+0.5)
    get_xml('D:\\xml.xml')
    dtl,bdl = read_xml('D:\\xml.xml')
    click('更多',dtl,bdl,my=10)
    find_click('群接龙','right',my=-100)
    get_xml('D:\\xml.xml')
    dtl,bdl = read_xml('D:\\xml.xml')
    click('点名接龙',dtl,bdl)
    get_xml('D:\\xml.xml')
    dtl,bdl = read_xml('D:\\xml.xml')
    click('到',dtl,bdl)
    click('发送',dtl,bdl)

def check(pass_word,way):
    #for ip in ips:connect(ip)
    unlock(pass_word)
    desktop()
    kill()
    open_ding(way)
    time.sleep(random()+4)
    find_click('一年级4班','down')
    time.sleep(random()+0.5)
    find_click('到','up')
    os.system('adb shell input swipe 540 1600 550 800')
    time.sleep(random()+0.5)
    find_click('到','down')
    print('-------Done--------')
hide= False
path = []
grand = open('./setting.txt','r',encoding='utf-8')
psd = grand.readline().replace('\n','').replace(' ','').replace('\t','')
while True:
    data = grand.readline().replace('\n','').replace(' ','').replace('\t','')
    if data == '':break
    elif '#' in data:pass
    elif '$$$' in data:hide = True
    else:path.append(data.split(','))
grand.close()
tb = []
grand = open('./timetable.txt','r',encoding='utf-8')
while True:
    data = grand.readline().replace('\n','').replace(' ','').replace('\t','')
    if data == '':break
    elif '#' in data:pass
    else:tb.append(data.split(':'))
grand.close()
#make_check(psd,path)
t = datetime.now()
run = False
while True:
    for i in tb:
        if int(t.hour) == int(i[0]) and int(t.minute) == int(i[1]):
            run = True
            break
    if run:
        if hide:check(psd,path)
        else:make_check(psd,path)
        run = False
    time.sleep(50)
    t = datetime.now()