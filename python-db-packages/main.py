import sys
sys.path.insert(0, './libs')
# import helper
# from helper import greeting # to bring in only the greeting function
import helper as h

def render():
    # print(helper.greeting('Tiffany', 'Hudgens')) # pulling in full helper library
    # print(greeting('Tiffany', 'Hudgens')) # using from helper import greeting
    print(h.greeting('Tiffany', 'Hudgens')) # using alias for helper library


render()


# import numpy as np

# num_range = np.arange(16)

# num_range

# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

# num_range.reshape(4, 4)

# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12, 13, 14, 15]])

# JSON Javascript Object Notation