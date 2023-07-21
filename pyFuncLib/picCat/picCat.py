import cv2
import numpy as np
import os
import sys

ACCEPTABLE_IMG_FORMAT = [".png", ".jpg", "jpeg"]
ALIGN_POS = ["l", "c", "r"] # left, centre, right alignment
PADDINGS = ["b", "w"] # black and white paddings

# Arguments
directory = "./"
pos = ALIGN_POS[-1]
padding = PADDINGS[-1]

"""
NOTE:
Please place the figures under the directory above, and make sure the figures are of the acceptable formats.
"""

def appendFiles(directory):
    cat_array = []
    for filename in os.listdir(directory):
        if filename[-4:] in ACCEPTABLE_IMG_FORMAT:
            f = os.path.join(directory, filename)
            cat_array.append(f)
        else:
            continue

    if len(cat_array) < 1:
        raise Exception("No image under current directory")  

    return cat_array

def catFig(fig1, fig2, pos, padding):

    match padding:
        case "w":
            padding = 255
        case "b":
            padding = 0.0
        case _: # default padding is white
            padding = 255

    new_height = fig1.shape[0] + fig2.shape[0]
    new_width = max(fig1.shape[1], fig2.shape[1])
    new_fig = padding * np.ones((new_height, new_width, 3)) # white paddings
    width_disparity = fig1.shape[1] - fig2.shape[1] # [1] stands for width of the figure 
    
    if pos not in ALIGN_POS:
        raise Exception("Params: Align position undefined")
    
    match pos:
        case "l": # images left align
            if(width_disparity == 0):
                new_fig[:fig1.shape[0], :, :] = fig1
                new_fig[fig1.shape[0]:, :, :] = fig2
            elif(width_disparity > 0):
                new_fig[:fig1.shape[0], :, :] = fig1
                new_fig[fig1.shape[0]:, :-width_disparity, :] = fig2
            else:
                new_fig[:fig1.shape[0], :width_disparity, :] = fig1
                new_fig[fig1.shape[0]:, :, :] = fig2

        case "c": # images centre align
            if(width_disparity == 0):
                new_fig[:fig1.shape[0], :, :] = fig1
                new_fig[fig1.shape[0]:, :, :] = fig2
            elif(width_disparity > 0):
                new_fig[:fig1.shape[0], :, :] = fig1
                new_fig[fig1.shape[0]:, width_disparity//2: width_disparity//2 - width_disparity, :] = fig2
            else:
                new_fig[:fig1.shape[0], -width_disparity//2 : width_disparity - width_disparity//2, :] = fig1
                new_fig[fig1.shape[0]:, :, :] = fig2

        case "r": # images right align
            if(width_disparity >= 0):
                new_fig[:fig1.shape[0], :, :] = fig1
                new_fig[fig1.shape[0]:, width_disparity:, :] = fig2
            else:
                new_fig[:fig1.shape[0], -width_disparity:, :] = fig1
                new_fig[fig1.shape[0]:, :, :] = fig2

        case _ : # Exceptions
            raise Exception("Params: Align position undefined")
        
    return new_fig

def picCat(dir=directory, pos = ALIGN_POS[-1], padding = PADDINGS[-1]):
    cat_files = appendFiles(dir)
    index = 0

    fig1 = cv2.imread(cat_files[index])

    while index < len(cat_files) - 1:
        index += 1
        fig2 = cv2.imread(cat_files[index])
        fig1 = catFig(fig1, fig2, pos, padding)

    cv2.imwrite("output.png", fig1)

    print("Cat end.")

        
if __name__ == '__main__':

    if len(sys.argv) > 1:
        pos = sys.argv[1]

    if len(sys.argv) > 2:
        padding = sys.argv[2]

    if len(sys.argv) > 3:
        directory = sys.argv[3]

    picCat(directory, pos, padding)
