import cv2
import numpy as np

HEIGHT, WIDTH = 800, 800
# HEIGHT, WIDTH = 1080, 1920
# HEIGHT, WIDTH = 102, 102
img = np.random.random((HEIGHT, WIDTH))
_, img = cv2.threshold(img, 0.5, 1, cv2.THRESH_BINARY)
# 全1是白色; 全0是黑色
ker3 = np.ones((3, 3))

def hhh(scr, fil):
    for y in range(np.shape(scr)[1]):
        for x in range(np.shape(scr)[0]):
            if fil[y][x] == 3:
                if scr[y][x] == 0:
                    scr[y][x] = 1
                else:
                    scr[y][x] = 1
            elif fil[y][x] == 4:
                if scr[y][x] == 1:
                    scr[y][x] = 1
            else:
                scr[y][x] = 0
    # print(scr, 'hhh-scr', type(scr[0, 0]))
    return scr


def uuu(scr, fil):
    num3 = np.where(fil == 3., 1., 0.)
    num4 = np.where(fil == 4., 1., 0.)
    scrB = cv2.bitwise_or(num3, num4)
    scrB = cv2.bitwise_and(scr, scrB)
    num31 = cv2.bitwise_or(scrB, num3)
    num41 = cv2.bitwise_and(scrB, num4)
    scr = cv2.bitwise_or(num31, num41)  # 必须是浮点数
    # print(scr, 'uuu-scr', type(scr[0, 0]))
    return scr


delayCountNum = 1  # 为1全速运行
delayCount = delayCountNum - 1
generation = 0  # 迭代次数

while True:
    delayCount += 1
    if delayCount == delayCountNum:
        delayCount = 0

        img2 = cv2.filter2D(img, -1, ker3)
        img2[[0, -1], :] = 3
        img2[:, [0, -1]] = 3
        img = uuu(img, img2)
        cv2.imshow('img', img)
        generation += 1
        print('generation', generation)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
