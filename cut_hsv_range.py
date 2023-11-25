python

class ImageProcessor:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.imagecopy = self.image.copy()
        self.list1 = []
        self.list2 = []
        self.num = 0

    def resize_image(self):
        self.image = cv2.resize(self.image, (0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_NEAREST)

    def getpos(self, event, x, y, flags, param):
        HSV3 = self.HSV2.copy()
        if event == cv2.EVENT_MOUSEMOVE:
            self.HSV = HSV3
            cv2.line(self.HSV, (0, y), (self.HSV.shape[1] - 1, y), (255, 255, 255), 1, 4)
            cv2.line(self.HSV, (x, 0), (x, self.HSV.shape[0] - 1), (255, 255, 255), 1, 4)
            cv2.imshow("imageHSV", self.HSV)
        elif event == cv2.EVENT_LBUTTONDOWN:
            self.num += 1
            self.HSV = HSV3
            if self.num == 1:
                self.list1.append([x, y])
                print('请点击HSV图片上第二个点')
            if self.num == 2:
                self.num = 0
                self.list2.append([x, y])
                for i in range(min(self.list1[-1][0], self.list2[-1][0]), max(self.list1[-1][0], self.list2[-1][0])):
                    for j in range(min(self.list1[-1][1], self.list2[-1][1]), max(self.list1[-1][1], self.list2[-1][1])):
                        self.hlist.append(self.HSV[j, i][0])
                        self.slist.append(self.HSV[j, i][1])
                        self.vlist.append(self.HSV[j, i][2])
                self.hlist.sort()
                self.slist.sort()
                self.vlist.sort()
                print(self.hlist)
                print(self.slist)
                print(self.vlist)
                print('请点击HSV图片上第一个点')
                print((self.hlist[0], self.slist[0], self.vlist[0]), (self.hlist[-1], self.slist[-1], self.vlist[-1]))

    def process_image(self):
        self.resize_image()
        self.HSV = self.image.copy()
        self.HSV2 = self.image.copy()
        self.num = 0
        self.hlist = []
        self.slist = []
        self.vlist = []

        cv2.imshow("imageHSV", self.HSV)
        cv2.setMouseCallback("imageHSV", self.getpos)
        cv2.waitKey(0)
......
