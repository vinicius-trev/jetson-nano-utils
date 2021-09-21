#!/usr/bin/env python

"""
This code converts absolute bounding box coordinates (x,y) in the following order: [top_left bottom_left bottom_right top_right]
to YOLO relative bb coordinates [class_index x_center y_center width height] 
"""

import os
import argparse
import glob

from PIL import Image

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--input", required=True, help="Input folder path")
    argparser.add_argument("-o", "--output", required=True, help="Output folder path")
    argparser.add_argument("-c", "--class_index", required=False, default=0, help="YOLO class index")
    args = vars(argparser.parse_args())

    # Reading all scene*.mercosul*.txt files
    print("Reading files from: " + os.path.join(args["input"], "scene*.mercosul*.txt"))
    for file in glob.glob(os.path.join(args["input"], "scene*.mercosul*.txt")):
        f = open(file, "r")

        # Eliminate number plate, split input text and convert it to integers that represent the pixel coordinate
        content = [int(float(i)) for i in f.read().split(",")[1:]]
        
        # Converting YOLO coordinate based on the input file and respective image reloution
        image = Image.open(file.replace(".txt", ".png"))

        # Just a little math to get the left and right points since the image can't be an exact rectagle
        left_x = min(content[0], content[2])    # Minimum value for left coord
        right_x = max(content[4], content[6])   # Maximum value for right coord

        bottom_y = max(content[3], content[5])  # Maximum value for bottom y coord
        top_y = min(content[1], content[7])     # Minimum value for top y coord

        bb_width = right_x - left_x
        bb_height = top_y - bottom_y

        center_point = (left_x + (bb_width / 2), bottom_y + (bb_height / 2))
        center_point_relative = (center_point[0] / image.size[0], center_point[1] / image.size[1])

        # Formating the output text
        output_str = str(args["class_index"]) + " " + str(center_point_relative[0]) + " " + str(center_point_relative[1]) + " " + str(abs(bb_width) / image.size[0]) + " " + str(abs(bb_height) / image.size[1])
        
        # Saving it on a new file on the output dir
        if not os.path.exists(args["output"]):
            os.mkdir(args["output"])

        out_f = open(os.path.join(args["output"], file.split(os.sep)[-1]), "w")
        out_f.write(output_str)
        out_f.close()

    print("Done!")
        
__author__ = "Vinicius Trevisan"
__copyright__ = "Copyright 2021, Instituto de Pesquisas Eldorado"