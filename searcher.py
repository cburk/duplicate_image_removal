from utilities import get_file_names, small_pixel_mult, create_pixel_set, remove_images
from imgcheckpopup import Popup

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
        seemingly_identical = val_to_pic[val]
        set_size = len(seemingly_identical)
        to_remove = []
        print seemingly_identical
        for i in range(set_size):
            for j in range(i + 1, set_size):
                print "Is " + seemingly_identical[i] + " = to " + seemingly_identical[j]
                # TODO: Spawn command prompt obj(thing1, thing2)
                pop = Popup()
                res = pop.spawn_popup(seemingly_identical[i], seemingly_identical[j])
                print "Answer: " + str(res)
                # if user responds yes
                if res:
                    to_remove.append(seemingly_identical[i])
                    break

        remove_images(to_remove)