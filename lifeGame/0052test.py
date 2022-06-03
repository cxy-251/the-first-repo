import cv2
import numpy as np

HEIGHT, WIDTH = 500, 500
img = np.random.random((HEIGHT, WIDTH))
_, img = cv2.threshold(img, 0.5, 1, cv2.THRESH_BINARY)
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


def uuu(scr, fil):
    num3 = np.where(fil == 3., 1., 0.)
    num4 = np.where(fil == 4., 1., 0.)
    num31 = cv2.bitwise_or(scr, num3)
    num41 = cv2.bitwise_and(scr, num4)
    scr = cv2.bitwise_or(num31, num41)  # 必须是浮点数
    print(scr, 'uuu-scr')
    return scr


# while True:
img00 = cv2.filter2D(img, -1, ker3)
img00[[0, -1], :] = 3
img00[:, [0, -1]] = 3


imgA = np.copy(img)
imgB = np.copy(img)
imgA0 = np.copy(img00)
imgB0 = np.copy(img00)

img0 = hhh(imgA, imgA0)
img05 = uuu(imgB, imgB0)

img_diff = cv2.absdiff(img0, img05)
print('hhh:', cv2.countNonZero(img_diff))
print(img0, 'img0', np.shape(img0), type(img0))
print(img05, 'img05', np.shape(img05), type(img05))
cv2.imshow('img1', img0)
cv2.imshow('img0', img05)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindows()
cv2.waitKey(0)

