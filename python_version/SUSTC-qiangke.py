import requests
import re
import time
import json
import random


# 个人设置，使用前请先进行简单设置
data = {
    # 记得写CAS账号和密码
    # 样例：'username': '116110000', 'password': 'abcdefg'
    'username': '',
    'password': ''
}
# 样例：list = [("TOEFL",'201920201001153'),('机器学习','201820191000216')]
list = [()] # 抢课列表
delay = 50 # 抢课失败后随机延迟，以毫秒为单位，若不需要则设为0

def rush_all(s, list):
    count = 1
    while len(list) > 0:
        print('\n开始第 %d 次喵喵喵' % count)
        count += 1
        for p in list:
            if rush(s, p):
                list.remove(p)


def rush(s, p):
    print('正在抢 %s' % p[0])
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
    # CAS登录并跳转教务系统
    s = requests.Session()
    r = s.get('https://cas.sustech.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustech.edu.cn%2Fjsxsd%2F')
    data['execution'] = re.findall('on" value="(.+?)"', r.text)[0]
    data['_eventId'] = 'submit'
    data['geolocation'] = ''
    s.post('https://cas.sustech.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustech.edu.cn%2Fjsxsd%2F', data)
    print("CAS验证成功")

    # 查询选课页面链接
    r = s.get('http://jwxt.sustech.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL')
    print("教务系统启动")
    key = re.findall('href="(.+)" target="blank">进入选课', r.text)
    k = key[0]

    # 这里前后cookies打印结果未发生变化，但是若省去上一条get则选课失败，提示“当前账号已在别处登录，请重新登录进入选课！”
    # print(s.cookies.get_dict()) 打印cookies
    s.get('http://jwxt.sustech.edu.cn' + k)
    # print(s.cookies.get_dict()) 打印cookies

    print("开始抢课")

    rush_all(s, list)
    s.close()


if __name__ == '__main__':
    main()
