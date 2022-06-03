import cv2
import numpy as np

HEIGHT, WIDTH = 602, 602
# HEIGHT, WIDTH = 102, 102
img = np.random.random((HEIGHT, WIDTH))
_, img = cv2.threshold(img, 0.5, 1, cv2.THRESH_BINARY)
# 全1是白色; 全0是黑色
img0 = np.copy(img)
img3 = np.ones((HEIGHT, WIDTH)) * 3


def num_alive(x, y):
    sum1 = 0
    sum1 += img0[y - 1][x - 1]
    sum1 += img0[y - 1][x]
    sum1 += img0[y - 1][x + 1]
    sum1 += img0[y][x - 1]
    sum1 += img0[y][x + 1]
    sum1 += img0[y + 1][x - 1]
    sum1 += img0[y + 1][x]
    sum1 += img0[y + 1][x + 1]
    return sum1


def next_pic(img0, img3, generation):
    next_field = np.zeros((HEIGHT, WIDTH))
    DEAD, ALIVE, MARKED, NON_MARKED, NEW_ALIVE, DIED_OUT = 0, 1, 2, 3, 4, 5
    for y in range(1, HEIGHT - 1):
        for x in range(1, WIDTH - 1):
            num_alive_count = num_alive(x, y)
            # print(num_alive_count)
            if img0[y][x] == ALIVE or img3[y][x] == DIED_OUT:
                img3[y][x] = MARKED
            if num_alive_count == 2:
                next_field[y][x] = img0[y][x]
            elif num_alive_count == 3:
                if img0[y][x] == DEAD:
                    img3[y][x] = NEW_ALIVE
                next_field[y][x] = ALIVE
            else:
                if img0[y][x] == ALIVE:
                    img3[y][x] = DIED_OUT
                next_field[y][x] = DEAD
    for y in range(1, HEIGHT - 1):
        for x in range(1, WIDTH - 1):
            if next_field[y][x] == ALIVE or img3[y][x] == NEW_ALIVE:
                # img[y][x] = 1
                img0[y][x] = 1
            else:
                # img[y][x] = 0
                img0[y][x] = 0
    generation += 1
    # print(img)
    # print(img3)
    return img0, generation


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


delayCountNum = 10
delayCount = delayCountNum - 1
generation = 0  # 迭代次数
theNightTime = 100  # 模拟灭绝周期
theNightmare = 1  # 模拟生物大灭绝 theNightmare in range(theNightTime) == True 为开启大灭绝


while True:
    delayCount += 1
    if delayCount == delayCountNum:
        delayCount = 0
        img, generation = next_pic(img0, img3, generation)
        # img = bit_bloat(img)
        cv2.imshow('img', img)
        print('generation', generation)
        if generation % theNightTime == theNightmare:
            print('hhhh')
            img0 = cv2.add(img0, np.random.random((HEIGHT, WIDTH)))
            _, img0 = cv2.threshold(img0, 0.5, 1, cv2.THRESH_BINARY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
