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

    def load_rocket(self, img):
        rocket_img = cv2.imread(self.rocket_path)
        h,w,c = rocket_img.shape
        for i in range(h) :
            for j in range(w) :
                for k in range(c) :
                    if rocket_img[i, j, k] == 0:
                        continue
                    else:
                        if j+self.x >= 630 :
                            self.x = 630-j
                        elif j + self.x <= 30 :
                            self.x = 30-j
                        img[i+self.y, j+self.x, k] = rocket_img[i,j,k]

        return img

    def move(self, img, direction):
        if direction == "left" :
            self.x-=5
        elif direction == "right" :
            self.x+=5
        self.load_rocket(img)

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

        return True

    def get_dimensions(self):
        return self.x, self.y


def main():
    wCam, hCam = 720, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0

    message_box = [0,0,0,0,0]
    rocket = Rocket()
    stick = gs.GameStick()
    monster = ms.monster()
    move=0
    first_enter = True
    status = True

    mMove = 0
    mFirst_enter=True
    mStatus=True
    noMonster=True
    #locked=False
    while True:
        success, img = cap.read()
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        if noMonster :
            message_box[1] = 1

        #loading monster
        if message_box[1] :
            noMonster=False
            if mFirst_enter :
                mX= random.randint(30,640)
                mY= random.randint(15,200)
                mFirst_enter=False
            if mStatus :
                mStatus = monster.load_monster(img, mMove, mX,mY)
                mMove+=5
            else:
                noMonster=True
                message_box[1]=0
                mFirst_enter=True
                mStatus=True
                mMove=0

        #loading rocket
        img = rocket.load_rocket(img)
        direction, shoot = stick.get_direction_and_shoot(img)
        rocket.move(img, direction)
        if shoot :
            message_box[0]=1

        if message_box[0]:
            if first_enter:
                x,y = rocket.get_dimensions()
                first_enter = False
            if status:
                status = rocket.shoot(img,move,x,y)
                move += 15
            else:
                message_box[0]=0
                first_enter=True
                status=True
                move=0


            #locked=True

        cv2.putText(img, f'FPS : {int(fps)}', (350, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        ch = cv2.waitKey(1)

if __name__ == "__main__":
    main()