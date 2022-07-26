import cv2

class monster :
    def __init__(self):
        self.moster_path = "Images/monster.png"

    def load_monster(self, img, move, x, y):
        monster_img = cv2.imread(self.moster_path)
        h,w,c = monster_img.shape
        for i in range(h) :
            for j in range(w) :
                for k in range(c) :
                    if monster_img[i, j, k] == 0:
                        continue
                    else:
                        if i+y+move >= 460 :
                            return False
                        img[i+y+move, j+x, k] = monster_img[i,j,k]

        return True
