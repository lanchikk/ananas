from PIL import Image
from PIL import ImageFilter


class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print("Файл не зайдено!")

    def do_bw(self):
        pic_gray = self.original.convert('L')
        self.changed.append(pic_gray)
        pic_gray.save('gray.jpg')

        pic_gray.save(new_filename)

    # бонус. Обрізати фотографію
    def do_cropped(self):
        box = (250, 100, 600, 400)  # ліво, верх, право, низ
        cropped = self.original.crop(box)

        # бонус. Автоматичний неймінг відредагованих картинок
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'
        cropped.save(new_filename)

    def do_left(self):
        pic_up = original.transpose(Image.ROTATE_90)
        self.changed.append(pic_up)
        pic_up.save('rotate.jpg')

MyImage = ImageEditor('original.jpg')
MyImage.open()

MyImage.do_bw()
MyImage.do_cropped()
MyImage.do_left()

for im in MyImage.changed:
    im.show()
