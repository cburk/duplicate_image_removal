from subprocess import check_output
from PIL import Image
from random import randint
from math import sqrt

R, G, B = 0, 1, 2

# Given a path to a directory, returns a list of the paths of all files in that directory
def get_file_names(dir_path):
    file_names = check_output(["ls", dir_path]).split("\n")[:-1]
    if dir_path[-1] == '/':
        return [dir_path + file_name for file_name in file_names]
    return [dir_path + '/' + file_name for file_name in file_names]

# Returns the minimum height and width of a list of files
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

# Returns a list of random (x,y) pairs that would be valid pixel coordinates in the given set of files
def create_pixel_set(files):
    minx, miny = min_file_size(files)
    return [(randint(0,minx - 1), randint(0,miny - 1)) for x in range(10)]

# Given a path to a picture and a series of pixels to check, returns the product of the R values of those pixels
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

# Given a list of file paths, rm all of them
def remove_images(img_list):
    for img in img_list:
        check_output(["rm", img])