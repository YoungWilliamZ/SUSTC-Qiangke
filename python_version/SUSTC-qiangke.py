import random

import requests
import re
import time
import json

s = requests.Session()
r = s.get('https://cas.sustc.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustc.edu.cn%2Fjsxsd%2F')
# print(str(r.content, 'utf-8'))
#记得写账号和密码
data = {
    'username': '',
    # 'username': '116110000',
    'password': '',
    # 'password': 'abcdefg',
    'execution': re.findall('on" value="(.+?)"', r.text)[0],
    '_eventId': 'submit',
    'geolocation': ''
}



#进入教务系统
r = s.post('https://cas.sustc.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustc.edu.cn%2Fjsxsd%2F', data)
# print(str(r.content, 'utf-8'))
print("CAS验证成功")
#查看选课是否开始
r = s.get('http://jwxt.sustc.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL')
print("教务系统启动")


count = 1
while True:
    count += 1
    key = re.findall('href="(.+)" target="blank">进入选课', r.text)
    # print(r.text)
    print(str(key))
    if len(key) == 1:
        break
    print('喵喵祈祷中……开始第 %d 次祈祷' % count)
    time.sleep(random.random()*random.random())
k = key[0]
print('榴莲启动完成')
print("开始抢课")


s.get('http://jwxt.sustc.edu.cn' + k)


list = [["微观",'201820191000655'],['机器学习',"201820191000216"]]

def add_class(oneclass):
    list.append(oneclass)


def rush_all(list):
    count2 = 1
    while True:
        print('开始第 %d 次喵喵喵' % count2)
        for p in list:
            count2 += 1
            if rush(p):
                list.remove(p)


def rush(p):
    print('正在抢 %s' % p[0])
    r = s.get("http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/fawxkOper?jx0404id=%s&xkzy=&trjf=" % p[1])
    result = str(r.content, 'utf-8')
    # print(result.find("true", 0, len(result)))
    if result.find("true", 0, len(result)) >= 1:
        print("抢到 "+ p[0] + " 啦")
        return True
    # print(str(json.loads(result)['success']) + "····\n正在继续加油！\n")
    delay = random.random()*random.random()
    print(result + "\n正在继续加油!\n············%f s 后" % delay)
    time.sleep(delay)
    return False

# print("空气动力学")
# r = s.get("http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/fawxkOper?jx0404id=201820191000460&xkzy=&trjf=")
# print(str(r.content, 'utf-8'))
# print("\n退课")
# r = s.get("http://jwxt.sustc.edu.cn/jsxsd/xsxkjg/xstkOper?jx0404id=201820191000460")
# print(str(r.content, 'utf-8'))


rush_all(list)


s.close()

