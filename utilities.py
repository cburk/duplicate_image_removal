from subprocess import check_output
from PIL import Image
from random import randint
from math import sqrt

R, G, B = 0, 1, 2

def get_file_names(dir_path):
    file_names = check_output(["ls", dir_path]).split("\n")[:-1]
    if dir_path[-1] == '/':
        return [dir_path + file_name for file_name in file_names]
    return [dir_path + '/' + file_name for file_name in file_names]

def min_file_size(files):
    minx = float("inf")
    miny = float("inf")
    for file in files:
        im = Image.open(file)
        if im.size[0] < minx:
            minx = im.size[0]
        if im.size[1] < miny:
            miny = im.size[1]
        im.close()

    return minx, miny

def create_pixel_set(files):
    minx, miny = min_file_size(files)
    return [(randint(0,minx - 1), randint(0,miny - 1)) for x in range(10)]


def small_pixel_mult(pic_name, small_pixel_set):
    im = Image.open(pic_name)
    rgb_im = im.convert('RGB')

    rval = 1
    for pixel in small_pixel_set:
        rval *= (1 + rgb_im.getpixel(pixel)[R])
    rval = int(sqrt(rval))

    print "rval: " + str(rval)

    im.close()
    return rval

# TODO: May not be necessary
def compare_group_exhaustively(group):
    return 0

# TODO: May not be necessary
def compare_image_pair():
    return 0