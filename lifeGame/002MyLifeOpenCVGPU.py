import cv2
import numpy as np

# print(cv2.getBuildInformation())
cv2.cuda.getCudaEnabledDeviceCount()

gpu_frame = cv2.cuda_GpuMat()
HEIGHT, WIDTH = 102, 102
screenshot = np.random.random((HEIGHT, WIDTH))

# gpu_frame.upload(screenshot)
# screenshot = cv2.cuda.resize(screenshot, (200, 200))
#
# hhh = gpu_frame.download()
# cv2.imshow('hhh', hhh)
