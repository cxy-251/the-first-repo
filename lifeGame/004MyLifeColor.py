import cv2
import numpy as np

HEIGHT, WIDTH = 500, 500
img = np.random.random((HEIGHT, WIDTH, 3))
_, img = cv2.threshold(img, 0.5, 1, cv2.THRESH_BINARY)
# 全1是白色; 全0是黑色
ker3 = np.ones((3, 3))


def hhh(scr, fil):
    for y in range(np.shape(scr)[1]):
        for x in range(np.shape(scr)[0]):
            if scr[y][x] == 1:
                if fil[y][x] == 3 or fil[y][x] == 4:
                    pass
                else:
                    scr[y][x] = 0
            else:
                if fil[y][x] == 3:
                    scr[y][x] = 1
    return scr


mul = 5  # 放大系数 对应1个像素
prune = 6  # 2的倍数 剪裁留中间去四周


def bit_bloat(img):
    img_bloat = np.ones(((HEIGHT - prune) * mul, (WIDTH - prune) * mul))
    for y in range(prune // 2, np.shape(img)[1] - prune // 2):
        for x in range(prune // 2, np.shape(img)[0]-prune // 2):
            if img[y][x] == 1:
                for b in range((y - prune // 2) * mul, (y + 1 - prune // 2) * mul):
                    for a in range((x - prune // 2) * mul, (x + 1 - prune // 2) * mul):
                        img_bloat[b][a] = 1
            else:
                for b in range((y - prune // 2) * mul, (y + 1 - prune // 2) * mul):
                    for a in range((x - prune // 2) * mul, (x + 1 - prune // 2) * mul):
                        img_bloat[b][a] = 0
    return img_bloat


delayCountNum = 1  # 为1全速运行
delayCount = delayCountNum - 1
generation = 0  # 迭代次数
theNightTime = 20  # 模拟灭绝周期
theNightmare = -1  # 生物大灭绝开关 theNightmare in range(theNightTime) == True 为开启大灭绝

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

        img00 = hhh(img[:, :, 0], img0)
        img11 = hhh(img[:, :, 1], img1)
        img22 = hhh(img[:, :, 2], img2)
        # img0 = bit_bloat(img0)
        img[:, :, 0] = img00
        img[:, :, 1] = img11
        img[:, :, 2] = img22
        cv2.imshow('img', img)
        generation += 1
        print('generation', generation)
        if generation % theNightTime == theNightmare:
            print('hhhh')
            img = cv2.add(img, np.random.random((HEIGHT, WIDTH)))
            _, img = cv2.threshold(img, 0.5, 1, cv2.THRESH_BINARY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
