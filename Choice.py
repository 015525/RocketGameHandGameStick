import cv2
import time
import HandTrackingModule as hm



class Choice :
    def __init__(self) :
        self.detector = hm.HandDetector(min_detection_confidence=0.75)
        self.target_lm = [8,12,16,20]


    def get_choice(self, img):
        img = self.detector.findHands(img)
        lm_list = self.detector.find_position(img, draw=False)

        if len(lm_list) > 0 :
            fingures=[]
            if (lm_list[4][1] > lm_list[3][1]) :
                fingures.append(1)
            else :
                fingures.append(0)

            for lm in self.target_lm :
                if (lm_list[lm][2] < lm_list[lm-2][2]):
                    fingures.append(1)
                else:
                    fingures.append(0)

            total_fingures = fingures.count(1)

        return total_fingures



def main() :
    wCam, hCam = 720, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0
    while True:
        success, img = cap.read()
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS : {int(fps)}', (350, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        ch = cv2.waitKey(1)

if __name__ == "__main__" :
    main()