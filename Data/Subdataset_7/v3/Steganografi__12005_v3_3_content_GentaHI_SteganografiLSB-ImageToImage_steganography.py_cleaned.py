import click
from PIL import Image
class class1:
    @staticmethod
    def fonk1(b8):
        r, g, b1 = b8
        return tuple('{0:08b}'.format(c) for c in (r, g, b1))
    @staticmethod
    def fonk2(b8):
        return tuple(int(c, 2) for c in b8)
    @staticmethod
    def fonk3(b6, b7):
        return tuple(r1[:4] + r2[:4] for r1, r2 in zip(b6, b7))
    @staticmethod
    def fonk4(img1, img2):
        if img2.size[0] > img1.size[0] or img2.size[1] > img1.size[1]:
            raise ValueError('Image 2 must not be larger than Image 1!')
        b2 = img1.load()
        b3 = img2.load()
        b4 = Image.new(img1.mode, img1.size)
        b5 = b4.load()
        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                b6 = class1.fonk1(b2[i, j])
                b7 = class1.fonk1(b3[i, j]) if i < img2.size[0] and j < img2.size[1] else ('00000000', '00000000', '00000000')
                b8 = class1.fonk3(b6, b7)
                b5[i, j] = class1.fonk2(b8)
        return b4
    @staticmethod
    def fonk5(img):
        b9 = img.load()
        b4 = Image.new(img.mode, img.size)
        b5 = b4.load()
        b10 = img.size
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b1 = class1.fonk1(b9[i, j])
                b8 = (r[4:] + '0000', g[4:] + '0000', b1[4:] + '0000')
                b5[i, j] = class1.fonk2(b8)
                if b5[i, j] != (0, 0, 0):
                    b10 = (i + 1, j + 1)
        b4 = b4.crop((0, 0, b10[0], b10[1]))
        return b4
@click.group()
def fonk6():
    pass
@cli.command()
@click.option('--img1', b11 = True, type=str, help='Image that will hide another image')
@click.option('--img2', b11 = True, type=str, help='Image that will be hidden')
@click.option('--output', b11 = True, type=str, help='Output image')
def fonk7(img1, img2, output):
    b12 = class1.fonk7(Image.open(img1), Image.open(img2))
    b12.save(output)
@cli.command()
@click.option('--img', b11 = True, type=str, help='Image that will be hidden')
@click.option('--output', b11 = True, type=str, help='Output image')
def fonk8(img, output):
    b13 = class1.fonk8(Image.open(img))
    b13.save(output)
if b14 = = '__main__':
    fonk6()