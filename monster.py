import cv2
import math

class monster :
    def __init__(self):
        self.moster_path = "Images/monster.png"

    def load_monster(self, img, move, x, y, xMissPos = None, yMissPos = None, xRocPos = None, yRocPos = None):
        monster_img = cv2.imread(self.moster_path)
        h,w,c = monster_img.shape
        ##print(h, w, c)
        for i in range(h):
            for j in range(w):
                for k in range(c):
                    if monster_img[i, j, k] == 255:
                        continue
                    else:
                        if i+y+move >= 460 :
                            return "ground hit"
                        if j+x >= 600 :
                            x =  630-j
                        #print(xRocPos, yRocPos)
                        if xMissPos and yMissPos and abs((i+y+move) - yMissPos) <= 10 and abs((j+x) - xMissPos) <= 10:
                            return "killed by missle"
                        if xRocPos and yRocPos and abs((i+y+move) - yRocPos) <= 10 and abs((j+x) - xRocPos) <= 10:
                            #print("iam here")
                            return "killed the rocket"

                        img[i+y+move, j+x, k] = monster_img[i,j,k]
                        #print(i+y+move)
        self.xMonsPos = j + x - 27  # 27 is half the width of the missle
        self.yMonsPos = i + y + move - 27  # 27 is half the height of the missle

        return "continue"

    def get_position (self):
        return self.xMonsPos, self.yMonsPos


