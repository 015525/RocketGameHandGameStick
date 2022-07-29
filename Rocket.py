import cv2
import time
import GameStick as gs
import monster as ms
import random


class Rocket :
    def __init__(self):
        self.rocket_path = "Images/Rocket.png"
        self.missle_path = "Images/missle.png"
        self.y = 380
        self.x = 200
        self.xMissPosInit = None
        self.yMissPosInit = None
        self.xRocPosInit = None
        self.yRocPosInit = None

    def load_rocket(self, img, move):
        rocket_img = cv2.imread(self.rocket_path)
        h,w,c = rocket_img.shape
        for i in range(h) :
            for j in range(w) :
                for k in range(c) :
                    if rocket_img[i, j, k] == 0:
                        continue
                    else:
                        if j+self.x+move >= 630 :
                            self.x = 630-j-move
                        elif j + self.x+move <= 30 :
                            self.x = 30-j-move

                        img[i+self.y, j+self.x+move, k] = rocket_img[i,j,k]

        self.xRocPosInit = j+self.x+move-15 #15 is half the width of the rocket
        self.yRocPosInit = i+self.y-45 #45 is half the height of the rocket

        return img

    '''
        def move(self, img, direction):
        if direction == "left" :
            self.xRocPosInit-=5
            self.x-=5
        elif direction == "right" :
            self.xRocPosInit+=5
            self.x+=5
        self.load_rocket(img)
    '''


    def shoot(self, img, move, x, y):
        status = self.load_missle(img, move, x, y)
        return status

    def load_missle(self, img, move, x, y):
        missle_img = cv2.imread(self.missle_path)
        h,w,c = missle_img.shape
        for i in range(h) :
            for j in range(w) :
                for k in range(c) :
                    if missle_img[i, j, k] == 0:
                        continue
                    else:
                        if i+y-55-move <= 30 :
                            return False
                        img[i+y-55-move, j+x-20, k] = missle_img[i,j,k]

        self.xMissPosInit = j + x - 20  - 35  # 35 is half the width of the missle
        self.yMissPosInit = i + y - 55 - move - 35  # 35 is half the height of the missle

        return True

    def get_dimensions(self):
        return self.x, self.y

    def get_roc_position(self):
        return self.xRocPosInit, self.yRocPosInit

    def get_miss_position(self):
        return self.xMissPosInit, self.yMissPosInit