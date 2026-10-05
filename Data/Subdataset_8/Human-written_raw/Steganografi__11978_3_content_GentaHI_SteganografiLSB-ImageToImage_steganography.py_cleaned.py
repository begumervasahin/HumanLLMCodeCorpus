import click
from PIL import Image
class Steganography(object):
    @staticmethod
    def __int_to_bin(rgb):
        """merubah tuple integer ke binary (string) tuple.
        :param rgb: An integer tuple (e.g. (220, 110, 96))
        :return: A string tuple (e.g. ("00101010", "11101011", "00010110"))
        merubah binary (string) tuple ke integer tuple.
        :param rgb: A string tuple (e.g. ("00101010", "11101011", "00010110"))
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
        pixel_map = img.load()
        new_image = Image.new(img.mode, img.size)
        pixels_new = new_image.load()
        original_size = img.size
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = Steganography.__int_to_bin(pixel_map[i, j])
                rgb = (r[4:] + '0000',
                       g[4:] + '0000',
                       b[4:] + '0000')
                pixels_new[i, j] = Steganography.__bin_to_int(rgb)
                if pixels_new[i, j] != (0, 0, 0):
                    original_size = (i + 1, j + 1)
        new_image = new_image.crop((0, 0, original_size[0], original_size[1]))
        return new_image
@click.group()
def cli():
    pass
@cli.command()
@click.option('--img1', required=True, type=str, help='Image that will hide another image')
@click.option('--img2', required=True, type=str, help='Image that will be hidden')
@click.option('--output', required=True, type=str, help='Output image')
def merge(img1, img2, output):
    merged_image = Steganography.merge(Image.open(img1), Image.open(img2))
    merged_image.save(output)
@cli.command()
@click.option('--img', required=True, type=str, help='Image that will be hidden')
@click.option('--output', required=True, type=str, help='Output image')
def unmerge(img, output):
    unmerged_image = Steganography.unmerge(Image.open(img))
    unmerged_image.save(output)
if __name__ == '__main__':
    cli()