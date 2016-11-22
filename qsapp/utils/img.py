from PIL import Image
import os


def convert_img(path):
    images = os.listdir(path)
    for i in images:
        print i
        img = Image.open(os.path.join(path, i))
        w, h = img.size
        max_width = 800
        max_height = 800
        if w > max_width or h > max_height:
            re_scal = min(max_width / float(w), max_height / float(h))
            re_w = int(round(w * re_scal))
            re_h = int(round(h * re_scal))
            re_size = (re_w, re_h)
            new_img = img.resize(re_size, Image.ANTIALIAS)
            try:
                p = Image.new('RGB', new_img.size, (255, 255, 255))
                p.paste(new_img)
            except Exception, e:
                img.convert("RGB")
                img.save(os.path.join(path, i.split(".")[0] + "_small"+".jpg"))
            else:
                p.save(os.path.join(path, i.split(".")[0] + "_small"+".jpg"))

if __name__ == '__main__':
    convert_img(r"C:\pyPrograms\qingquans\qsapp\static\img\portfolio")