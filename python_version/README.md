# Python 版本抢课说明

> Update on 2018-09-05\
> 选课系统由 湖南强智科技发展有限公司 所有版权，理论上可以通用

## 运行环境

* python 版本： 3.7.0
* 需要的包: requests

## 使用前必做

1. 在第12行 data 中添加 `username` 和 `password`, 即 账号 和 密码， 用于 CAS 认证

![添加账号密码](https://i.imgur.com/ZMx2uOx.png)

2. 添加修改你要抢的课的 `名字` 和 `id`, 查看 id 的方法下面会讲

![添加修改你要抢的课](https://i.imgur.com/IL5phhC.png)

## 运行

``` bash
python3 SUSTC-qiangke.py
```

## 如何查看课程 id ？

1. 进入选课系统
2. 右键 `选课` 按钮，检查
3. 右侧或左侧出现 id , 如下

![查找 id](https://i.imgur.com/aPU8Yki.png)