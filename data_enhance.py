python

class ImageProcessing:
    def __init__(self, path, savepath):
        self.path = path
        self.savepath = savepath

    def process_images(self):
        if not os.path.exists(self.savepath):
            os.mkdir(self.savepath)
        list = os.listdir(self.path)
        for i in list:
            img = cv2.imread(self.path + '/' + i)
            imgcopy1 = img.copy()
            imgcopy2 = img.copy()
            imgcopy3 = img.copy()
            imgcopy4 = img.copy()
            imgcopy5 = img.copy()
            cv2.imwrite(self.savepath + '/' + 'original-' + i, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            res = cv2.resize(imgcopy1, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(self.savepath + '/' + '2x-' + i, res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            res = cv2.resize(res, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(self.savepath + '/' + '4x-' + i, res, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            rows, cols, ch = img.shape
            M = np.float32([[1, 0, 100], [0, 1, 50]])
            dst = cv2.warpAffine(imgcopy2, M, (cols, rows))
            cv2.imwrite(self.savepath + '/' + 'move-' + i, dst, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            rows, cols, ch = img.shape
            M = cv2.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
            dst = cv2.warpAffine(imgcopy3, M, (cols, rows))
            cv2.imwrite(self.savepath + '/' + '90-' + i, dst, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            rows, cols, ch = img.shape
            pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
            pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
            M = cv2.getAffineTransform(pts1, pts2)
  ......
