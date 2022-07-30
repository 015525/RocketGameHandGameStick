import cv2
import time
import HandTrackingModule as hm
import math



class GameStick:
    def __init__(self):
        self.detector = hm.HandDetector(min_detection_confidence=0.75)

    def get_direction_and_shoot(self, img):
        img = self.detector.findHands(img, draw=False)
        lm_list = self.detector.find_position(img, draw=False)

        direction = ""
        shoot = False
        if len(lm_list) > 17 :
            xu, yu= lm_list[5][1], lm_list[5][2]
            xl, yl= lm_list[17][1], lm_list[17][2]

            if (xu - xl) >= 75 :
                direction = "hard left"
            elif (xu - xl) >= 25 :
                direction = "left"
            elif (xl - xu) >= 75 :
                direction = "hard right"
            elif (xl - xu) >= 25 :
                direction = "right"


            xs1, ys1 = lm_list[6][1], lm_list[6][2]
            xs2, ys2 = lm_list[4][1], lm_list[4][2]
            #xs3, ys3 = lm_list[3][1], lm_list[3][2]
            length = math.hypot(xs2 - xs1, ys2 - ys1)
            #print(length)
            #print(ys3, ys2)
            if length < 40 :# and ys3-ys2 <= 20 :
                #print(length)
                shoot = True
            else:
                shoot = False

        return direction, shoot, lm_list


def main() :
    wCam, hCam = 720, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0

    stick = GameStick()

    while True:
        success, img = cap.read()
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        stick.get_direction_and_shoot(img)

        #cv2.putText(img, f'FPS : {int(fps)}', (350, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        ch = cv2.waitKey(1)

if __name__ == "__main__" :
    main()


'''
    def get_direction_and_shoot(self, img):
        img = self.detector.findHands(img)
        lm_list = self.detector.find_position(img, draw=False)

        direction = ""
        shoot = False
        if len(lm_list) > 17 :
            xu, yu= lm_list[5][1], lm_list[5][2]
            xl, yl= lm_list[17][1], lm_list[17][2]

            xh1, yh1 = lm_list[10][1], lm_list[10][2]
            xh2, yh2 = lm_list[9][1], lm_list[9][2]

            if xh1 < xh2 :
                print("xu : "+ str(xu) + " xl : " + str(xl))
                if (xu - xl) >= 25 :
                    print("left")
                    direction = "left"
                elif (xl - xu) >= 25 :
                    print("right")
                    direction = "right"

            elif xh1 > xh2 :
                xs1, ys1 = lm_list[16][1], lm_list[16][2]
                xs2, ys2 = lm_list[0][1], lm_list[0][2]
                length = math.hypot(xs2-xs1, ys2-ys1)
                if length < 60:
                    shoot = True
                    print(shoot)
                else :
                    shoot = False
                    print(shoot)

        return direction, shoot
'''