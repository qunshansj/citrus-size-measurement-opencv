python


class ImageBlender:
    def __init__(self, img1_path, img2_path):
        self.img1 = Image.open(img1_path).convert('RGBA')
        self.img2 = Image.open(img2_path).convert('RGBA')
        self.img2 = self.img2.resize(self.img1.size)
    
    def blend_images(self, alpha):
        return Image.blend(self.img1, self.img2, alpha)
    
    def save_blend_image(self, output_path, alpha):
        img = self.blend_images(alpha)
        img.save(output_path)
    
.......

