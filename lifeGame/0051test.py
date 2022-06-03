import cv2
import numpy as np

HEIGHT, WIDTH = 102, 102
imgTrue = np.ones((HEIGHT, WIDTH), dtype=bool)
imgFalse = np.zeros((HEIGHT, WIDTH), dtype=bool)

# img00 = np.ones((HEIGHT, WIDTH))
img1 = np.ones((HEIGHT, WIDTH))
img2 = np.ones((HEIGHT, WIDTH)) * 2
img3 = np.ones((HEIGHT, WIDTH)) * 3
img4 = np.ones((HEIGHT, WIDTH)) * 4
img5 = np.ones((HEIGHT, WIDTH)) * 5
img6 = np.ones((HEIGHT, WIDTH)) * 6
img7 = np.ones((HEIGHT, WIDTH)) * 7
img8 = np.ones((HEIGHT, WIDTH)) * 8
img9 = np.ones((HEIGHT, WIDTH)) * 9


img = np.random.random((HEIGHT, WIDTH))
_, img = cv2.threshold(img, 0.5, 1, cv2.THRESH_BINARY)
# 全1是白色; 全0是黑色
ker3 = np.ones((3, 3))

# img00 = np.ones((HEIGHT, WIDTH, 3))
# cv2.multiply(img3, img2, img)  # 矩阵元素值相乘
# cv2.add(img3, img2, img)  # 矩阵元素值相加
# cv2.divide(img3, img2, img)  # 矩阵元素值相除
# cv2.subtract(img3, img2, img)  # 矩阵元素值相减

# img = cv2.bitwise_and(img, 2)


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


img00 = cv2.filter2D(img, -1, ker3)
img00[[0, -1], :] = 3
img00[:, [0, -1]] = 3

img0 = hhh(img, img00)
# print(img, 'img')
# print(img0, 'img0')

# img01 = cv2.subtract(img00, 3)  # 矩阵元素值相减
# img02 = np.copy(img00)
# img02[img02 > 4] = 0
# img02[img02 < 4] = 0
# img02[img02 == 4] = 1
# # results = np.where(condition, [x, y])
# # 当条件为真时，对应位置返回x中的值，条件不成立则返回y中的值
# img03 = np.where(img00 == 4, 1, 0)  #满足大于0的值保留，不满足的设为0
# print(img00, 'img00')
# print(img01, 'img01')
# print(img02, 'img02')
# print(img03, 'img03')

def uuu(scr, fil):
    num3 = np.where(fil == 3., 1., 0.)
    num4 = np.where(fil == 4., 1., 0.)
    num31 = cv2.bitwise_or(scr, num3)
    num41 = cv2.bitwise_and(scr, num4)
    scr = cv2.bitwise_or(num31, num41)  # 必须是浮点数
    print(scr, 'uuu-scr')
    return scr

#
# img03 = np.where(img00 == 3., 1., 0.)
# img04 = np.where(img00 == 4., 1., 0.)
# img030 = cv2.bitwise_or(img, img03)
# img040 = cv2.bitwise_and(img, img04)
# # print(img03, 'img03')
# # print(img04, 'img04')
# # print(img030, 'img030')
# # print(img040, 'img040')
# img05 = cv2.bitwise_or(img030, img040)  # 必须是浮点数
# # print(img05, 'img05')

img05 = hhh(img, img00)  # #############################################大问题
img_diff = cv2.absdiff(img0, img05)
print('hhh:', cv2.countNonZero(img_diff))
print(img0, 'img0', np.shape(img0), type(img0))
print(img05, 'img05', np.shape(img05), type(img05))


# img = np.hstack((img, img9[:, 1:-1]))
# img02 = np.hstack((img02, img9[:, 1:-1]))
# print(np.hstack((np.hstack((img, img02)), img0)))
cv2.waitKey(0)

