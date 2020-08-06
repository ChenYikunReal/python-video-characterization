import os
import cv2

# 字符表
chars = 'mqpka89045321@#$%^&*()_=||||}'
# 读取视频
video = cv2.VideoCapture('freedom.mp4')
# 读取帧
ret, frame = video.read()
# 逐帧读取
while ret:
    # 字符画
    str_img = ''
    # 灰度转换
    grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # 该表大小
    grey = cv2.resize(grey, (100, 40))
    # 遍历每个像素点
    for i in grey:
        for j in i:
            # 获取字符坐标
            index = int(j / 256 * len(chars))
            # 将字符添加到字符画中
            str_img += chars[index]
        str_img += '\n'
    # 清除上一帧输出的内容
    os.system('cls')
    # 输出字符画
    print(str_img)
    # 读取下一帧
    ret, frame = video.read()
    cv2.waitKey(5)
