# -*- coding: utf-8 -*-

import cv2

cascade = cv2.CascadeClassifier('cascade_filter/haarcascade_frontalface_default.xml')

def CamCapture(mirror = False, size = (1200, 900)):
    cap = cv2.VideoCapture(0)

    while(1):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        face = cascade.detectMultiScale(gray, 1.1, 3)

        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 50, 255), 3)


        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)
            
        if ret == True:
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        else:
            print "capture error"

    cap.release()
    cv2.destroyAllWindows()

def main():
    CamCapture()

if __name__ == '__main__':
    main()