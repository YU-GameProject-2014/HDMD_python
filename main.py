# -*- coding: utf-8 -*-

import cv2

def CamCapture(mirror = False, size = (1280, 720)):
    cascade = cv2.CascadeClassifier('cascade_filter/haarcascade_frontalface_default.xml')
  
    dst = cv2.imread('image/megane.png', -1)

    cap = cv2.VideoCapture(0)

    while(1):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        face = cascade.detectMultiScale(gray, 1.1, 3)

        for (x, y, w, h) in face:
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 50, 255), 3)

            dst2 = cv2.resize(dst, (w,h))
            d_w, d_h = dst2.shape[:2]
            mask = dst2[:,:,3]
            mask = cv2.cvtColor(mask, cv2.cv.CV_GRAY2BGR)
            mask = mask / 255.0
            dst2 = dst2[:, :, :3]
            try:
                frame[y:d_h + y:, x:d_w + x] *= 1 - mask
                frame[y:d_h + y:, x:d_w + x] += dst2 * mask
            except Exception, e:
                pass
        
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        if ret == True:
            cv2.imshow(u'鼻眼鏡君'.encode('shift-jis'), frame)
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