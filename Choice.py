import cv2
import time
import HandTrackingModule as hm



class Choice :
    def __init__(self) :
        self.detector = hm.HandDetector(min_detection_confidence=0.75)
        self.target_lm = [8,12,16,20]


    def get_choice(self, img):
        total_fingures = 0
        img = self.detector.findHands(img, draw=False)
        lm_list = self.detector.find_position(img, draw=False)
        xb1,xb2,yb1=None,None,None

        if len(lm_list) > 0 :
            total_fingures = self.get_num_of_fingures(lm_list)
            xb1 = lm_list[4][1]
            xb2 = lm_list[20][1]
            yb1 = lm_list[12][2]

        return total_fingures, xb1, xb2, yb1

    def get_num_of_fingures(self, lm_list):
        total_fingures = 0
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


'''
img = detector.findHands(img, draw = False)
        lm_list = detector.find_position(img, draw=False)

        if len(lm_list) > 0:
            fingures = []
            if (lm_list[4][1] > lm_list[3][1]):
                fingures.append(1)
            else:
                fingures.append(0)

            for lm in target_lm:
                if (lm_list[lm][2] < lm_list[lm - 2][2]):
                    fingures.append(1)
                else:
                    fingures.append(0)

            total_fingures = fingures.count(1)
            xb1 = lm_list[4][1]
            xb2 = lm_list[20][1]
            yb1 = lm_list[12][2]
            
    #fps = 1 / (cTime - pTime)
        #pTime = cTime
        if first_enter :
            pTime = cTime
            first_enter=False
        if (cTime-pTime) >= 5 :
            print(cTime-pTime)
        #res = choice.get_choice(img)
        #print(res)
        
     #return "quit"
        #cv2.putText(img, f'FPS : {int(fps)}', (350, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        
                #yb2 = lm_list[0][2]
            #print(xb1)
'''