# Before running this project, please call
# python setup.py build_ext --inplace
# in the "darkflow" directory.

from darkflow.net.build import TFNet
import numpy as np
import cv2
import time

def drawTextWithCv2Text(img, text, left, top):
    cv2.putText(img, text, (left, top + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, text, (left, top + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

def darkflowWithCamera(mirror=False, size=None):
    cap = cv2.VideoCapture(0)
    options = {"model": "./cfg/yolo.cfg", "load": "./bin/yolo.weights", "threshold": 0.1}
    tfnet = TFNet(options)
    boxColor = (0, 0, 255)
    elapsed = time.time()
    fps = 0.0

    while True:
        elapsedPrevious = elapsed
        elapsed = time.time()
        fps = 0.7 * fps + 0.3 * (elapsed - elapsedPrevious)

        ret, frame = cap.read()
        if mirror is True:
            frame = frame[:,::-1]
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        boxInfoList = tfnet.return_predict(frame)
        for boxInfo in boxInfoList:
            confidence = boxInfo["confidence"]
            if (confidence < 0.5): continue

            topLeft = boxInfo["topleft"]
            bottomRight = boxInfo["bottomright"]
            left = topLeft["x"]
            top = topLeft["y"]
            right = bottomRight["x"]
            bottom = bottomRight["y"]
            centerX = (left + right) / 2
            centerY = (top + bottom) / 2
            width = (right - left)
            height = (bottom - top)
            description = "[%s] Center:(%d,%d) Size:(%d,%d) Conf:%5.3f" % (boxInfo["label"], centerX, centerY, width, height, confidence)
            cv2.rectangle(frame, (left, top), (right, bottom), boxColor, 2)
            drawTextWithCv2Text(frame, description, left, top)

        drawTextWithCv2Text(frame, "FPS: %.3f" % fps, 0, 0)
        cv2.imshow("Result", frame)

        k = cv2.waitKey(1)
        if k == 27: break

    cap.release()
    cv2.destroyAllWindows()

darkflowWithCamera()
