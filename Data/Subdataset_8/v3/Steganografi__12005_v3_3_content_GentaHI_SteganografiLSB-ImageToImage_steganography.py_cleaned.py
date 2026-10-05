import click
from PIL import Image
class Steganography:
    @staticmethod
    def int_to_bin(rgb):
        r, g, b = rgb
        return tuple('{0:08b}'.format(c) for c in (r, g, b))
    @staticmethod
    def bin_to_int(rgb):
        return tuple(int(c, 2) for c in rgb)
    @staticmethod
    def merge_rgb(rgb1, rgb2):
        return tuple(r1[:4] + r2[:4] for r1, r2 in zip(rgb1, rgb2))
    @staticmethod
    def merge(img1, img2):
        if img2.size[0] > img1.size[0] or img2.size[1] > img1.size[1]:
            raise ValueError('Image 2 must not be larger than Image 1!')
        pixel_map1 = img1.load()
        pixel_map2 = img2.load()
        new_image = Image.new(img1.mode, img1.size)
        pixels_new = new_image.load()
        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                rgb1 = Steganography.int_to_bin(pixel_map1[i, j])
                rgb2 = Steganography.int_to_bin(pixel_map2[i, j]) if i < img2.size[0] and j < img2.size[1] else ('00000000', '00000000', '00000000')
                rgb = Steganography.merge_rgb(rgb1, rgb2)
                pixels_new[i, j] = Steganography.bin_to_int(rgb)
        return new_image
    @staticmethod
    def unmerge(img):
        pixel_map = img.load()
        new_image = Image.new(img.mode, img.size)
        pixels_new = new_image.load()
        original_size = img.size
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = Steganography.int_to_bin(pixel_map[i, j])
                rgb = (r[4:] + '0000', g[4:] + '0000', b[4:] + '0000')
                pixels_new[i, j] = Steganography.bin_to_int(rgb)
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