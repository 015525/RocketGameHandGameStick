import cv2
from Rocket import Rocket
import GameStick as gs
import monster as ms
import Choice as ch
import time
import random

choice = ch.Choice()

def rocket_game_loop(highScore):
    wCam, hCam = 720, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    #pTime = 0
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
    first_enter_q = True
    #locked=False
    while True:
        success, img = cap.read()
        #user_choice = choice.get_choice(img)
        # print(user_choice)
        '''
        if user_choice == "rocket game" :
            
        elif user_choice == "quit" :
        '''


        #cTime = time.time()
        #fps = 1 / (cTime - pTime)
        #pTime = cTime




        if noMonster :
            message_box[1] = 1

        #loading monster
        if message_box[1] :
            noMonster=False
            if mFirst_enter :
                mX= random.randint(30,530)
                mY= random.randint(15,100)
                mFirst_enter=False
            if monStatus == "start" or monStatus == "continue" :
                #print(monStatus)
                xMissPosInit, yMissPosInit = rocket.get_miss_position()
                xRocPosInit, yRocPosInit = rocket.get_roc_position()
                monStatus = monster.load_monster(img, monMove, mX,mY, xMissPosInit, yMissPosInit, xRocPosInit, yRocPosInit)
                if score < 10 :
                    monMove+=5
                elif score < 25 :
                    monMove+=8
                else :
                    monMove += 12
            else :
                if monStatus == "killed the rocket" :
                    #print(monStatus)
                    lives-=1
                elif monStatus == "killed by missle":
                    #print(monStatus)
                    score+=1
                    message_box[0] = 0
                    first_enter = True
                    missStatus = True
                    missMove = 0
                else :
                    lives-=1
                noMonster=True
                message_box[1]=0
                mFirst_enter=True
                monStatus="start"
                monMove=0


        #loading rocket
        img = rocket.load_rocket(img, rocMove)
        direction, shoot, lm_lsit = stick.get_direction_and_shoot(img)
        num_fingures = choice.get_num_of_fingures(lm_lsit)
        if num_fingures == 5 :
            if first_enter_q:
                pTime = time.time()
                first_enter_q = False
            cTime = time.time()
            if (cTime - pTime) >= 2:
                lives = 0
        else :
            first_enter_q = True

        if direction == "left":
            rocMove -= 5
        elif direction == "hard left":
            #print("iam here")
            rocMove -= 15
        elif direction == "right":
            rocMove += 5
        elif direction == "hard right":
            #print("iam here")
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
            return score

            #locked=True

        # cv2.putText(img, f'FPS : {int(fps)}', (350, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

        cv2.putText(img, f'Score : {score}', (10,35),  cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
        cv2.putText(img, f'High Score : {highScore}', (370, 35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(img, f'Live : {lives}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.imshow("Rocket Game", img)
        ch = cv2.waitKey(1)

if __name__ == "__main__":
    rocket_game_loop()