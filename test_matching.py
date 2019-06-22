import os
import argparse
import time

import match_code

ap = argparse.ArgumentParser()
ap.add_argument("--codefile", required=True,
    help="path to code file")
ap.add_argument("--video", required=True,
    help="path to input video")
ap.add_argument("--image_path", 
    help="path to input images to be OCR'd", default="images")
ap.add_argument("-p", "--preprocess", type=str,
	help="type of preprocessing to be done", default="thresh")
ap.add_argument("--framepath",
	help="path to OCR output of frames", default="output")
args = vars(ap.parse_args())

start = time.perf_counter()
match_code.match(args["codefile"], args["framepath"])
code_match_time = time.perf_counter() - start

print("\n")
print("Code matching completed in : ", code_match_time)
