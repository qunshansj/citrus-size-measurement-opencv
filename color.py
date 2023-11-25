python

class ImageProcessing:
    def __init__(self):
        self.work_book = xlwt.Workbook()
        self.work_sheet = self.work_book.add_sheet('Test')

    def mosaic(self, img, p1, p2):
        im = img
        im2 = cv2.flip(im, 0, im)
        im2resize = cv2.resize(im2, (abs(p1[0] - p2[0]), abs(p1[1] - p2[1])))
        im[min(p1[1], p2[1]):max(p1[1], p2[1]), min(p1[0], p2[0]):max(p1[0], p2[0])] = im2resize
        return im

......
