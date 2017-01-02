from utilities import get_file_names, small_pixel_mult, create_pixel_set, compare_group_exhaustively

def search_directory(dir_name):
    file_names = get_file_names(dir_name)

    # Psuedo hash function, sums rgb values of 15 different pixels.
    # Goal is to create small groups of similar pics to compare exhaustively
    val_to_pic = {}
    small_pixel_set = create_pixel_set(file_names)
    print small_pixel_set
    for pic_name in file_names:
        hash = small_pixel_mult(pic_name, small_pixel_set)
        if hash in val_to_pic:
            val_to_pic[hash].append(pic_name)
        else:
            val_to_pic[hash] = [pic_name]

    # Compare images w/ the same "hash" values to see if they're truly identical.  If so, flag them
    for val in val_to_pic:
        compare_group_exhaustively(val_to_pic[val])

