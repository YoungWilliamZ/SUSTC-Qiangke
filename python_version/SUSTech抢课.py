'''
Made by Github User 'CatFood-is-CatFood'
'''

import requests
import re
import time
import json
import random


data = {}
list = [] # 抢课列表
delay = random.random() * random.random() # 抢课失败后随机延迟
s = requests.Session()


# 预先设置
def set():
    # 输入CAS账号密码
    data['username'] = input("请输入您的CAS账号：").strip()
    data['password'] = input("请输入您的CAS密码：").strip()
    data['_eventId'] = 'submit'
    data['geolocation'] = ''
    list.append(tuple(re.split("[, ]",input('\n请输入待抢课程名称、id与分类号，以逗号分隔，名字任取，\n本学期计划分类号为1，专业内跨年级为2，其他为0，\n如" IELTS,201920201001718,0 "：'))))
    while(int(input("请问是否继续添加课程，不需要请输入0，需要请输入1：").strip())!=0):
        list.append(tuple(re.split("[, ]",input("请输入待抢课程名称、id与分类号：").strip())))
    if(int(input("\n请问是否需要固定抢课失败延迟，不需要请输入0，需要请输入1："))!=0):
        delay = int(input("请以毫秒为单位输入抢课失败后延迟："))
    print()


def prepare():
    # CAS登录并跳转教务系统
    r = s.get('https://cas.sustech.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustech.edu.cn%2Fjsxsd%2F')
    data['execution'] = re.findall('on" value="(.+?)"', r.text)[0]
    s.post('https://cas.sustech.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustech.edu.cn%2Fjsxsd%2F', data)

    # 查询选课页面链接
    r = s.get('http://jwxt.sustech.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL')
    
    key = re.findall('href="(.+)" target="blank">进入选课', r.text)
    k = key[0]

    # 这里前后cookies打印结果未发生变化，但是若省去上一条get则选课失败，提示“当前账号已在别处登录，请重新登录进入选课！”
    # print(s.cookies.get_dict()) 打印cookies
    s.get('http://jwxt.sustech.edu.cn' + k)
    # print(s.cookies.get_dict()) 打印cookies

    print("CAS验证成功")
    print("教务系统启动")
    print("开始抢课")


def rush_all(list):
    count = 1
    while len(list) > 0:
        print('\n开始第 %d 次喵喵喵' % count)
        count += 1
        for p in list:
            if rush(p):
                list.remove(p)


def rush(p):
    print('正在抢 %s' % p[0])
    if p[2] == '1':
        r = s.get("http://jwxt.sustech.edu.cn/jsxsd/xsxkkc/bxqjhxkOper?jx0404id=%s&xkzy=&trjf=" % p[1])
    elif p[2] == '2':
        r = s.get("http://jwxt.sustech.edu.cn/jsxsd/xsxkkc/knjxkOper?jx0404id=%s&xkzy=&trjf=" % p[1])
    else:
        r = s.get("http://jwxt.sustech.edu.cn/jsxsd/xsxkkc/fawxkOper?jx0404id=%s&xkzy=&trjf=" % p[1])
    result = str(r.content, 'utf-8')
    if result.find("true", 0, len(result)) >= 1:
        print("抢到 "+ p[0] + " 啦")
        return True
    if delay <= 0:
        print(result + "继续加油!")
    else:
        print(result + "继续加油!等待%fs" % (delay/1000))
    time.sleep(delay/1000)
    return False


def main():
    set()
    prepare()
    rush_all(list)
    s.close()


if __name__ == '__main__':
    main()
