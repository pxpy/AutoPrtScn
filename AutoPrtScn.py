import time,datetime
from PIL import ImageGrab
import os 
import uuid
import numpy as np
import math

uuidName = uuid.uuid4().hex
d1 = datetime.date.today() #获取当前时间
end_h = 17 #结束时间
end_m = 55 #结束分钟
base_dir = 'C:/logs' #图片保存地址
IMGNUM=15 #图片对比缓存数量
imgList = [] # 截图图片列表
startTime = datetime.datetime(2023, int(d1.month), int(d1.day), end_h, end_m, int(d1.day)+1) #自动截图到16:25
print(startTime)
i = 0
# 判断两个图片是否相似，不相似返回true
def dif(lim, limg):
    pix = lim.load()
    afterPix = limg.load()
    if lim != limg : #界面发现变化了才保存图片
        sum = 0
        for m in range(1920):
            for n in range(100,980):
                sum = sum + (pix[m,n]-afterPix[m,n]) ** 2
        print(math.sqrt(sum)//1)
        return math.sqrt(sum)/1920 > 10
#最新的图片如果不相似返回true,有时候老师不停上下翻页
def comList():
    flag = True
    for img in imgList[0:-2]:
        limg = img.convert('L')
        if dif(limg, imgList[-1].convert('L')) == False:
            flag=False
    return flag
while  datetime.datetime.now() < startTime:
    # im =ImageGrab.grab()
    # lim = im.convert('L')
    time.sleep(3) #0.5秒一截
    img = ImageGrab.grab()
    imgList.append(img)
    if len(imgList) == 1:
        imgList[0].save(os.sep.join([base_dir, uuidName +'-' +str(i)+'.png']))
    else:
        if len(imgList) > IMGNUM:
            imgList = imgList[-IMGNUM:-1]
        if comList():
            imgList[-1].save(os.sep.join([base_dir, uuidName +'-' +str(i)+'.png']))
    i+=1
print('finish')