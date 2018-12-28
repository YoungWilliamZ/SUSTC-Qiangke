import random

import re
import time
import requests

# Config
# 学号和密码
SID = "请在此输入学号"
PWD = "请在此输入密码"

# 课程列表
# 课程名可以选择填写，course_id 必须填写
C_LIST = [
    ["课程名1", "course_id 1"],
    ["课程名2", "course_id 2"],
]


# 程序开始
LOGIN_URL = 'http://jxgl.gdufs.edu.cn/jsxsd/'
VCODE_SRC = 'verifycode.servlet'

s = requests.Session()
r = s.get(LOGIN_URL)
v_code = s.get(LOGIN_URL + VCODE_SRC)
with open("v_code.png", "wb") as v_code_png:
    v_code_png.write(v_code.content)
v_code_value = input("请输入验证码：")
# 学号和密码
data = {
    "USERNAME": SID,
    "PASSWORD": PWD,
    "RANDOMCODE": v_code_value
}

# 进入教务系统
r = s.post('http://jxgl.gdufs.edu.cn/jsxsd/xk/LoginToXkLdap', data)
print("验证成功")
# 查看选课是否开始
r = s.get("http://jxgl.gdufs.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL")
# r = s.get('http://jwxt.sustc.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL')
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
    time.sleep(2)
k = key[0]
print('榴莲启动完成')
print("开始抢课")


s.get('http://jxgl.gdufs.edu.cn' + k)

course_list = C_LIST


def add_class(one_class):
    course_list.append(one_class)


def rush_all(c_list):
    count2 = 1
    while c_list:
        print('开始第 %d 次喵喵喵' % count2)
        for p in c_list:
            count2 += 1
            if rush(p):
                c_list.remove(p)
    print("Tasks clear！")


def rush(p):
    print('正在抢 %s' % p[0])
    r = s.get("http://jxgl.gdufs.edu.cn/jsxsd/xsxkkc/xxxkOper?jx0404id=%s" % p[1])
    result = r.content.decode("utf8")
    print(result)
    # print(result.find("true", 0, len(result)))
    if result.find("true", 0, len(result)) >= 1:
        print("抢到 " + p[0] + " 啦")
        return True
    # print(str(json.loads(result)['success']) + "····\n正在继续加油！\n")
    delay = random.random()*random.random()
    print(result + "\n正在继续加油!\n············%f s 后" % delay)
    time.sleep(random.random()*random.random())
    time.sleep(0.1)
    return False


rush_all(course_list)
s.close()
