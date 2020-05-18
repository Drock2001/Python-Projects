import pyautogui
from PIL import Image, ImageGrab
import time
import numpy as asarray

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(330, 370):
            for j in range(620, 670):
                if data[i, j] < 120:
                    hit('up')
                    return
    
    for i in range(350, 400):
            for j in range(575, 615):
                if data[i, j] < 120:
                    hit('up')
                    return

    for i in range(250, 330):
            for j in range(450, 570):
                if data[i, j] < 120:
                    hit('down')
                    return


if __name__ == "__main__":
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        '''for i in range(330, 370):
            for j in range(620, 670):
                data[i, j] = 100

        for i in range(350, 400):
            for j in range(575, 615):
                data[i, j] = 171

        for i in range(250, 330):
            for j in range(450, 570):
                data[i, j] = 0
                          
        #print(asarray(image))
        image.show()
        break'''
    