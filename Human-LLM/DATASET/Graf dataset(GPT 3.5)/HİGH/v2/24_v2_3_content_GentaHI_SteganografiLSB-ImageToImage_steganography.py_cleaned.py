import click
from PIL import Image
class class1:
    @staticmethod
    def fonk1(b4):
        r, g, b3 = b4
        return ('{0:08b}'.format(r),
                '{0:08b}'.format(g),
                '{0:08b}'.format(b3))
    @staticmethod
    def fonk2(b4):
        r, g, b3 = b4
        return (int(r, 2),
                int(g, 2),
                int(b3, 2))
    @staticmethod
    def fonk3(b9, b10):
        r1, g1, b3 = b9
        r2, g2, b3 = b10
        b4 = (r1[:4] + r2[:4],
               g1[:4] + g2[:4],
               b3[:4] + b3[:4])
        return b4
    @staticmethod
    def fonk4(img1, img2):
        if img2.size[0] > img1.size[0] or img2.size[1] > img1.size[1]:
            raise ValueError('Image 2 must not be larger than Image 1!')
        b5 = img1.load()
        b6 = img2.load()
        b7 = Image.new(img1.mode, img1.size)
        b8 = b7.load()
        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                b9 = class1.fonk1(b5[i, j])
                b10 = class1.fonk1((0, 0, 0))
                if i < img2.size[0] and j < img2.size[1]:
                    b10 = class1.fonk1(b6[i, j])
                b4 = class1.fonk3(b9, b10)
                b8[i, j] = class1.fonk2(b4)
        return b7
    @staticmethod
    def fonk5(img):
        b11 = img.load()
        b7 = Image.new(img.mode, img.size)
        b8 = b7.load()
        b12 = img.size
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b3 = class1.fonk1(b11[i, j])
                b4 = (r[4:] + '0000',
                       g[4:] + '0000',
                       b3[4:] + '0000')
                b8[i, j] = class1.fonk2(b4)
                if b8[i, j] != (0, 0, 0):
                    b12 = (i + 1, j + 1)
        b7 = b7.crop((0, 0, b12[0], b12[1]))
        return b7
@click.group()
def fonk6():
    pass
@cli.command()
@click.option('--img1', b13 = True, type=str, help='Image that will hide another image')
@click.option('--img2', b13 = True, type=str, help='Image that will be hidden')
@click.option('--output', b13 = True, type=str, help='Output image')
def fonk7(img1, img2, output):
    b14 = class1.fonk7(Image.open(img1), Image.open(img2))
    b14.save(output)
@cli.command()
@click.option('--img', b13 = True, type=str, help='Image that will be hidden')
@click.option('--output', b13 = True, type=str, help='Output image')
def fonk8(img, output):
    b15 = class1.fonk8(Image.open(img))
    b15.save(output)
if b16 = = '__main__':
    fonk6()