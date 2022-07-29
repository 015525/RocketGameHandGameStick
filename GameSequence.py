from choiceLoop import choice
from RocketGameLoop import rocket_game_loop
import json
import cv2
import time
import Choice as cho

with open('high_score.json') as f :
    high_score = json.load(f)

user_choice = choice()


def quit_screen():
    wCam, hCam = 720, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    first_enter = True
    while True:
        if first_enter :
            pTime = time.time()
            first_enter = False
        cTime = time.time()
        if (cTime-pTime) >= 3 :
            break
        success, img = cap.read()
        cv2.putText(img, f'Thank You For Your Time :)', (100, 230), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.imshow("Image", img)
        ch = cv2.waitKey(1)

def quit_game_screen(highScore, score):
    wCam, hCam = 720, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    choice = cho.Choice()
    first_enter_1 = True
    first_enter_2 = True
    pTime = 0
    while True:
        success, img = cap.read()
        cTime = time.time()
        img_1 = cv2.imread("Images/1.png")
        img_2 = cv2.imread("Images/2.png")
        h1, w1, c1 = img_1.shape
        h2, w2, c2 = img_2.shape
        img[90:90 + h1, 380: 380 + w1] = img_1
        img[130:130 + h2, 340: 340 + w2] = img_2

        cv2.putText(img, f'Your Score : {score}', (200, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(img, f'High Score : {highScore}' ,(200, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(img, f'To Replay ', (200, 120), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(img, f'To Quit ', (200, 160), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(img, (180, 180), (470, 470), (255, 0, 255), 3)

        total_fingures, xb1, xb2, yb1 = choice.get_choice(img)

        if total_fingures == 1 and xb1 < 470 and xb2 > 180 and yb1 > 180:  # and yb2<470 :
            if first_enter_1:
                pTime = cTime
                first_enter_1 = False
            if (cTime - pTime) >= 2:
                return "rocket_game"
        else:
            first_enter_1 = True

            # return "rocket game"
        if total_fingures == 2 and xb1 < 470 and xb2 > 180 and yb1 > 180:  # and yb2<470 :
            if first_enter_2:
                pTime = cTime
                first_enter_2 = False
            if (cTime - pTime) >= 2:
                return "quit_game"
        else:
            first_enter_2 = True
        cv2.imshow("Image", img)
        ch = cv2.waitKey(1)

while user_choice == "rocket_game" :
    score = rocket_game_loop(high_score['high_score'])
    if score > high_score['high_score'] :
        with open('high_score.json', 'r+') as f:
            high_score = json.load(f)
            high_score['high_score'] = score
        with open('high_score.json', 'w') as f:
            json.dump(high_score, f,indent = 4)
    user_choice = quit_game_screen(high_score['high_score'], score)


quit_screen()


'''
        if first_enter :
            pTime = time.time()
            first_enter = False
        cTime = time.time()
        if (cTime-pTime) >= 3 :
            break
'''


