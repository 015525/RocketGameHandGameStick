import cv2
import Choice as cho
import time

def choice() :
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
        img_1 = cv2.imread("Images/1.png")
        img_2 = cv2.imread("Images/2.png")
        img_5 = cv2.imread("Images/5.png")
        h1, w1, c1 = img_1.shape
        h2, w2, c2 = img_2.shape
        h5, w5, c5 = img_5.shape

        img[50:50 + h1, 330: 330 + w1] = img_1
        img[130:130 + h2, 190: 190 + w2] = img_2
        img[85:85 + h5, 560: 560 + w5] = img_5
        cv2.putText(img, f'Please Pick a Choice', (40, 40), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, f'1- Rocket Game', (40, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.putText(img, f'You can quit at any time by opening the five fingures', (80, 110), cv2.FONT_HERSHEY_PLAIN, 1,
                    (0, 255, 0), 2)
        cv2.putText(img, f'2- Quit', (40, 160), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.rectangle(img, (180, 180), (470, 470), (255, 0, 255), 3)

        cTime = time.time()
        total_fingures, xb1, xb2, yb1 = choice.get_choice(img)


        if total_fingures == 1 and xb1<470 and  xb2>180 and yb1>180:# and yb2<470 :
            if first_enter_1 :
                pTime = cTime
                first_enter_1 = False
            if (cTime-pTime) >= 2 :
                return "rocket_game"
        else :
            first_enter_1 = True


            #return "rocket game"
        if total_fingures == 2 and xb1<470 and  xb2>180 and yb1>180:# and yb2<470 :
            if first_enter_2:
                pTime = cTime
                first_enter_2 = False
            if (cTime - pTime) >= 2:
                return "quit_game"
        else:
            first_enter_2 = True

        cv2.imshow("Image", img)
        ch = cv2.waitKey(1)

if __name__ == "__main__" :
    choice()