import cv2
import numpy
import random
import time

def showmood():
    blink=cv2.VideoCapture('normalmood45.gif')
    happy0=cv2.VideoCapture('happy.gif')

    while True:
        if blink.isOpened():
            ret1,img1=blink.read()
            if ret1 == True:
                k=cv2.waitKey(50)
                cv2.imshow('my moo1',img1)
                if k==27 :
                    break
                if k==ord('h'):
                    cv2.imshow('my moo1',cv2.imread('hapstill.PNG'))
                    blink=cv2.VideoCapture('happy.gif')
                if k==ord('c'):
                    cv2.imshow('my moo1',cv2.imread('crystill.PNG'))
                    blink=cv2.VideoCapture('crymore.gif')
                if k==ord('j'):
                    cv2.imshow('my moo1',cv2.imread('judgystill.PNG'))
                    blink=cv2.VideoCapture('judgy.gif')
                if k==ord('a'):
                    cv2.imshow('my moo1',cv2.imread('angrystill.PNG'))
                    blink=cv2.VideoCapture('angry.gif')
                if k==ord('b'):
                    cv2.imshow('my moo1',cv2.imread('blushstill.PNG'))
                    blink=cv2.VideoCapture('blush.gif')

            else:
                blink=cv2.VideoCapture('normalmood45.gif')

    blink.release()
    cv2.destroyAllWindows()

def main():
    showmood()
if __name__=='__main__':
    main()

            


