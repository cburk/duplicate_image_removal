from PIL import Image
from subprocess import check_output
from re import split

def get_file_names(dir_path):
    file_names = check_output(["ls", dir_path]).split("\n")[:-1]
    if dir_path[-1] == '/':
        return [dir_path + file_name for file_name in file_names]
    return [dir_path + '/' + file_name for file_name in file_names]

#file_names = get_file_names("test_images")
#print file_names

#im = Image.open("test_images/flavortown.jpg")

#print "Hello world"