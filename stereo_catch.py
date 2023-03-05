import cv2
import time

counter = 1
AUTO = True  # 自动拍照，或手动按s键拍照
INTERVAL = 2 # 自动拍照间隔
cameral = cv2.VideoCapture(0)#也许你可能要capture两次
camerar = cv2.VideoCapture(1)#也许你可能要capture两次
cameral.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)#设置分辨率
cameral.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)#
camerar.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)#设置分辨率
camerar.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)#
utc = time.time()
folder = "D:/image" # 拍照文件目录

def shot( framel, framer):
    leftpath = folder +"/left/"+"left_" + str(counter) + ".jpg"
    rightpath=folder + "/right/"+ "right_" + str(counter) + ".jpg"
    leftframe=framel#这里是为了将合在一个窗口显示的图像分为左右摄像头
    rightframe=framer
    cv2.imwrite(leftpath, leftframe)

    cv2.imwrite(rightpath, rightframe)
    print("snapshot saved into: " + leftpath)
    print("snapshot saved into: " + rightpath)

while True:
    retl, framel = cameral.read()
    retr, framer = camerar.read()


    cv2.imshow("originall", framel)
    cv2.imshow("originalr", framer)

    now = time.time()
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        shot( framer, framel)
        counter += 1

cameral.release()
camerar.release()
cv2.destroyWindow("originall")
cv2.destroyWindow("originalr")