# import numpy as np
# import cv2


# camera = cv2.VideoCapture(Vilib.video_source)

# camera.set(3,320)
# camera.set(4,240)
 
# width = int(camera.get(3))
# height = int(camera.get(4))

# M = cv2.getRotationMatrix2D((width / 2, height / 2), 180, 1)
# camera.set(cv2.CAP_PROP_BUFFERSIZE,1)
# cv2.setUseOptimized(True)

# while True:
#     # start_time = time.time()
#     _, img = camera.read()
#     # img = cv2.warpAffine(img, M, (320, 240))
#     img = cv2.resize(img, (8,8), interpolation=cv2.INTER_LINEAR)
#     img = Vilib.human_detect_func(img)
#     Vilib.img_array[0] = Vilib.color_detect_func(img)   