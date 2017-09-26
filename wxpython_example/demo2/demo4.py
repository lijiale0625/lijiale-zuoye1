# -*- coding: cp936 -*-
import os
import random
import wx


def opj(path):
    st = apply(os.path.join, tuple(path.split('/')))
    if path.startswith('/'):
        st = '/' + st
    return st


imgTypeDict = {
    'bmp': wx.BITMAP_TYPE_BMP,
    'gif': wx.BITMAP_TYPE_GIF,
    'png': wx.BITMAP_TYPE_PNG,
    'jpg': wx.BITMAP_TYPE_JPEG
}


# 获取后缀
def getType(o):
    if o.rfind(".") > -1:
        idx = o.rindex(".") + 1
        return o[idx:].lower()
    else:
        return ""


p1 = opj('photos/right.bmp')
p2 = opj('photos/wrong.bmp')
p3 = opj('photos/no response.bmp')
response = {
    'right': p1,
    'wrong': p2,
    'timeout': p3
}

sep = (2, '+', 1000)
sep0 = (2, '', 1000)
trialConf = (
    (1, 'photos/welcome.bmp'),
    (1, 'photos/instruction.bmp'),
    (2, '+', 1),  # 1000ms 文本
    (3, 'photos/practice/face1', 400, 200, 1500),
    # 探测的文件目录时间（面空时间，探测点时间，等待回答时间）
    (0, 'photos/goodbye.bmp', 5000)
)
testConf = (
    (1, 'photos/welcome.bmp'),
    (1, 'photos/instruction.bmp'),
    (2, '+', 1000),  # 1000ms 文本
    (3, 'photos/donghua', 400, 50, 1500),
    # 探测的文件目录时间（面空时间，探测点时间，等待回答时间）
    (0, 'photos/goodbye.bmp', 5000)
)


def getSteps(conf):
    steps = []
    for x in conf:
        type = x[0]
        img = x[1]
        if type == 0:  # end
            item = (0, opj(x[1]), -1)
            steps.append(item)

        if type == 1:  # 单个图片
            item = (1, opj(x[1]), -1)  # -1 means infinate
            steps.append(item)
        elif type == 2:  #
            item = (2, x[1], x[2])  # 内容，时间
            steps.append(item)
        elif type == 3:
            dir1 = x[1]
            t1 = x[2]
            t2 = x[3]
            t3 = x[4]
            face = []
            probe = []
            for root, dirs, files in os.walk(dir1, topdown=False):
                for name in files:
                    if name.endswith(".gif") or name.endswith(".bmp"):
                        face.append(opj(os.path.join(root, name)))
            face.sort()
            print face
            count = len(face)
            i = 0
            while (i < count):
                curImg = face[i]
                i += 1
                nextImg = face[i]
                if nextImg.find("_2") > 0:  # 存在2，就是下面有点
                    answer = 2
                else:
                    answer = 1
                i += 1
                curItem = (curImg, nextImg, answer)
                probe.append(curItem)
                # print face
            random.shuffle(probe)

            i = 0
            count = len(probe)
            #  print probe
            while (i < count):
                curItem = probe[i]
                item = (3, curItem[0], t1)
                steps.append(item)
                item = (9, curItem[1], t2, curItem[2])
                # 马上要激活keyboard反应,并置相应的时间处理函数

                # (类型4需要响应,图片路径，呈现时间，正确答案，超时时间，
                steps.append(item)
                item = (4, curItem[0], t3)
                steps.append(item)
                steps.append(sep0)

                steps.append(sep)
                i += 1

    return steps
