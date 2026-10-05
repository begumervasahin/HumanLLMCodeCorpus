import click
from PIL import Image
class class1(object):
    @staticmethod
    def fonk1(b6):
        """merubah tuple integer ke binary (string) tuple.
        :param b6: An integer tuple (e.g. (220, 110, 96))
        :return: A string tuple (e.g. ("00101010", "11101011", "00010110"))
        merubah binary (string) tuple ke integer tuple.
        :param b6: A string tuple (e.g. ("00101010", "11101011", "00010110"))
        :return: Return an int tuple (e.g. (220, 110, 96))
        menggabungkan kedua RGB tuples.
        :param rgb1: A string tuple (e.g. ("00101010", "11101011", "00010110"))
        :param rgb2: Another string tuple
        (e.g. ("00101010", "11101011", "00010110"))
        :return: An integer tuple with the two RGB values merged.
        menggambungkan kedua citra.Citra kedua yang akan digabungkan ke citra pertama.
        :param img1: First image
        :param img2: Second image
        :return: new merged image.
        memisahkan foto tadi.
        :param img: The input image.
        :return: The unmerged/extracted image.
        """
        b1 = img.load()
        b2 = Image.new(img.mode, img.size)
        b3 = b2.load()
        b4 = img.size
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b5 = class1.fonk1(b1[i, j])
                b6 = (r[4:] + '0000',
                       g[4:] + '0000',
                       b5[4:] + '0000')
                b3[i, j] = class1.__bin_to_int(b6)
                if b3[i, j] != (0, 0, 0):
                    b4 = (i + 1, j + 1)
        b2 = b2.crop((0, 0, b4[0], b4[1]))
        return b2
@click.group()
def fonk2():
    pass
@cli.command()
@click.option('--img1', b7 = True, type=str, help='Image that will hide another image')
@click.option('--img2', b7 = True, type=str, help='Image that will be hidden')
@click.option('--output', b7 = True, type=str, help='Output image')
def fonk3(img1, img2, output):
    b8 = class1.fonk3(Image.open(img1), Image.open(img2))
    b8.save(output)
@cli.command()
@click.option('--img', b7 = True, type=str, help='Image that will be hidden')
@click.option('--output', b7 = True, type=str, help='Output image')
def fonk4(img, output):
    b9 = class1.fonk4(Image.open(img))
    b9.save(output)
if b10 = = '__main__':
    fonk2()