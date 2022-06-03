import cv2
import numpy as np

times = 10
HEIGHT, WIDTH = 1080//times, 1920//times
img = np.random.random((HEIGHT, WIDTH, 3))
_, img = cv2.threshold(img, 0.5, 1, cv2.THRESH_BINARY)
ker3 = np.ones((3, 3))

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


def life(scr, fil):
    num3 = np.where(fil == 3., 1., 0.)
    num4 = np.where(fil == 4., 1., 0.)
    scrB = cv2.bitwise_or(num3, num4)
    scrB = cv2.bitwise_and(scr, scrB)
    num31 = cv2.bitwise_or(scrB, num3)
    num41 = cv2.bitwise_and(scrB, num4)
    scr = cv2.bitwise_or(num31, num41)  # 必须是浮点数
    return scr


delayCountNum = 1  # 为1全速运行
delayCount = delayCountNum - 1
generation = 0  # 迭代次数
theNightTime = 2000  # 模拟灭绝周期
theNightmare = 1  # 生物大灭绝开关 theNightmare in range(theNightTime) == True 为开启大灭绝


while True:
    delayCount += 1
    if delayCount == delayCountNum:
        delayCount = 0

        img0 = cv2.filter2D(img[:, :, 0], -1, ker3)
        img0[[0, -1], :] = 3
        img0[:, [0, -1]] = 3
        img1 = cv2.filter2D(img[:, :, 1], -1, ker3)
        img1[[0, -1], :] = 3
        img1[:, [0, -1]] = 3
        img2 = cv2.filter2D(img[:, :, 2], -1, ker3)
        img2[[0, -1], :] = 3
        img2[:, [0, -1]] = 3
        img00 = life(img[:, :, 0], img0)
        img11 = life(img[:, :, 1], img1)
        img22 = life(img[:, :, 2], img2)
        img[:, :, 0] = img00
        img[:, :, 1] = img11
        img[:, :, 2] = img22

        cv2.imshow('img', img)
        generation += 1
        print('generation', generation)
        if generation % theNightTime == theNightmare:
            print('hhhh')
            a = np.random.randint(0, 3)
            print(a)
            img[:, :, a] = cv2.add(img[:, :, a], np.random.random((HEIGHT, WIDTH)))
            _, img[:, :, a] = cv2.threshold(img[:, :, a], 0.5, 1, cv2.THRESH_BINARY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
