python

class Cutout:
    def __init__(self, image_path):
        self.image_path = image_path
        self.im = cv2.imread(image_path)

    def generate_mask(self):
        p1 = (random.randint(0, self.im.shape[1]), random.randint(0, self.im.shape[0]))
        p2 = (random.randint(0, self.im.shape[1]), random.randint(0, self.im.shape[0]))
        cv2.rectangle(self.im, (min(p1[0], p2[0]), min(p1[1], p2[1])), (max(p1[0], p2[0]), max(p1[1], p2[1])), [0, 0, 0], -1)

    def show_image(self):
        cv2.imshow('cutout', self.im)
        cv2.waitKey(0)

