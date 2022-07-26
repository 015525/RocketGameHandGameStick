import cv2
#import os
import time
import GameStick as gs

class Rocket :
    def __init__(self):
        self.rocket_path = "Images/Rocket.png"
        self.missle_path = "Images/missle.png"
        self.y = 380
        self.x = 200

    def load_rocket(self, img):
        rocket_img = cv2.imread(self.rocket_path)
        h,w,c = rocket_img.shape
        #print(str(h)+" "+str(w))
        #print(rocket_img)
        for i in range(h) :
            for j in range(w) :
                for k in range(c) :
                    if rocket_img[i, j, k] == 0:
                        continue
                    else:
                        #if j+self.x > 640 :
                        #    self.x = 640-j
                        img[i+self.y, j+self.x, k] = rocket_img[i,j,k]

        return img

    def move(self, img, direction):
        if direction == "left" :
            self.x-=5
        elif direction == "right" :
            self.x+=5
        self.load_rocket(img)

    def shoot(self, img, move):
        self.load_missle(img, move)

    def load_missle(self, img, move):
        missle_img = cv2.imread(self.missle_path)
        h,w,c = missle_img.shape
        #print(str(h)+" "+str(w))
        #print(rocket_img)
        #for move in range(300) :
        for i in range(h) :
            for j in range(w) :
                for k in range(c) :
                    if missle_img[i, j, k] == 0:
                        continue
                    else:
                        #if j+self.x > 640 :
                        #    self.x = 640-j
                        img[i+self.y-55-move, j+self.x-20, k] = missle_img[i,j,k]

        return img





def main():
    wCam, hCam = 720, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0

    rocket = Rocket()
    stick = gs.GameStick()
    move=0

    while True:
        success, img = cap.read()
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        img = rocket.load_rocket(img)
        direction, shoot = stick.get_direction_and_shoot(img)
        rocket.move(img, direction)
        if shoot :
            rocket.shoot(img,move)

        cv2.putText(img, f'FPS : {int(fps)}', (350, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        ch = cv2.waitKey(1)
        move+=5

if __name__ == "__main__":
    main()