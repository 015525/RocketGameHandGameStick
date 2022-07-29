import cv2
from Rocket import Rocket
import GameStick as gs
import monster as ms
import time
import random

def main():
    wCam, hCam = 720, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0
    rocMove=0

    message_box = [0,0]
    rocket = Rocket()
    stick = gs.GameStick()
    monster = ms.monster()
    missMove=0
    first_enter = True
    missStatus = True

    monMove = 0
    mFirst_enter=True
    monStatus="start"
    noMonster=True

    lives = 5
    score = 0
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
                mX= random.randint(30,600)
                mY= random.randint(15,100)
                mFirst_enter=False
            if monStatus == "start" or monStatus == "continue" :
                #print(monStatus)
                xMissPosInit, yMissPosInit = rocket.get_miss_position()
                xRocPosInit, yRocPosInit = rocket.get_roc_position()
                monStatus = monster.load_monster(img, monMove, mX,mY, xMissPosInit, yMissPosInit, xRocPosInit, yRocPosInit)
                monMove+=5
            else :
                if monStatus == "killed the rocket" :
                    print(monStatus)
                    lives-=1
                elif monStatus == "killed by missle":
                    #print(monStatus)
                    score+=1
                    missStatus = False
                else :
                    lives-=1
                noMonster=True
                message_box[1]=0
                mFirst_enter=True
                monStatus="start"
                monMove=0


        #loading rocket
        img = rocket.load_rocket(img, rocMove)
        direction, shoot = stick.get_direction_and_shoot(img)
        if direction == "left":
            rocMove -= 5
        elif direction == "hard left":
            print("iam here")
            rocMove -= 15
        elif direction == "right":
            rocMove += 5
        elif direction == "hard right":
            print("iam here")
            rocMove += 15

        if shoot :
            message_box[0]=1

        if message_box[0]:
            if first_enter:
                x,y = rocket.get_dimensions()
                x+=rocMove
                first_enter = False
            if missStatus:
                missStatus = rocket.shoot(img,missMove,x,y)
                missMove += 15
            else:
                message_box[0]=0
                first_enter=True
                missStatus=True
                missMove=0

        if lives == 0:
            break

            #locked=True

        # cv2.putText(img, f'FPS : {int(fps)}', (350, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

        cv2.putText(img, f'Score : {score}', (10,35),  cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
        cv2.putText(img, f'Live : {lives}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.imshow("Image", img)
        ch = cv2.waitKey(1)

if __name__ == "__main__":
    main()