python

class ImageCutout:
    def __init__(self, image_path1, image_path2):
        self.im = cv2.imread(image_path1)
        self.im2 = cv2.imread(image_path2)
    
    def cutout(self):
        p1 = (random.randint(0, self.im.shape[1]), random.randint(0, self.im.shape[0]))
        p2 = (random.randint(0, self.im.shape[1]), random.randint(0, self.im.shape[0]))
        im2resize = cv2.resize(self.im2, (abs(p1[0] - p2[0]), abs(p1[1] - p2[1])))
        self.im[min(p1[1], p2[1]):max(p1[1], p2[1]), min(p1[0], p2[0]):max(p1[0], p2[0])] = im2resize
        cv2.imshow('cutout', self.im)
        cv2.waitKey(0)
.......
