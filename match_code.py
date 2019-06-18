from PIL import Image # import the necessary packages
from difflib import SequenceMatcher
import pytesseract
import argparse
import cv2
import os
import time

ap = argparse.ArgumentParser()
ap.add_argument("--path", required=True,
	help="path to OCR output of frames")
ap.add_argument("--codefile", required=True,
    help="path to code file")
args = vars(ap.parse_args())

# ============================================================================================
def extract_timestamp(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return h, m, s
# ============================================================================================


# def extract_text(mpath_to_File, mpreprocess):
# 	# load the example image and convert it to grayscale
# 	image = cv2.imread(mpath_to_File)
# 	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 	# check to see if we should apply thresholding to preprocess the image
# 	if mpreprocess == "thresh":
# 		gray = cv2.threshold(gray, 0, 255,
# 			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# 	# make a check to see if median blurring should be done to remove
# 	# noise
# 	elif mpreprocess == "blur":
# 		gray = cv2.medianBlur(gray, 3)

# 	# write the grayscale image to disk as a temporary file so we can
# 	# apply OCR to it
# 	filename = "{}.png".format(os.getpid())
# 	cv2.imwrite(filename, gray)

# 	# load the image as a PIL/Pillow image, apply OCR, and then delete
# 	# the temporary file
# 	text = pytesseract.image_to_string(Image.open(filename))
# 	os.remove(filename)
# 	return text

# ============================================================================================

# ============================================================================================

# def write_to_disk(string, filename):
# 	output_filename = filename.replace("jpg", "txt")
# 	save_path = "./output"
# 	if not (os.path.exists(save_path)):
# 		try:  
# 			os.mkdir(save_path)
# 		except OSError:  
# 			print ("Creation of the directory %s failed" % save_path)
# 		else:  
# 			print ("Successfully created the directory %s " % save_path)
# 	with open(os.path.join(save_path, output_filename), "w") as ocr_file:
# 		ocr_file.write(string)
# 	return

# ============================================================================================

# ============================================================================================
def process(line):
    return

# ============================================================================================

# ============================================================================================

lines_in_source_code = list()       
 
path_to_code_file = args["codefile"]
with open(path_to_code_file) as code:
    for line in code:
        lines_in_source_code.append(line.strip())

# lines_in_source_code.reverse()
frames = os.listdir(args["path"])
sorted_frames = sorted(frames, reverse = True) # read frames in reverse

start = time.clock()
for idx, sc_line in enumerate(lines_in_source_code):
    # print("LINE: ", idx, " : ", sc_line[0:10])
    max_ratio = 0.0
    cur_ratio = 0.0
    max_ratio_frame = ""
    if len(sc_line) < 3:
        # print("continue : ", sc_line)
        continue

    for file in sorted_frames:
        path_to_File = os.path.join(args["path"], file)
        with open(path_to_File) as f:
            for i, line in enumerate(f):
                cur_ratio = SequenceMatcher(None, sc_line, line).ratio()
                if(cur_ratio >= max_ratio):
                    max_ratio = cur_ratio
                    max_ratio_frame = file
                # # print("line ", i, " ratio: ", SequenceMatcher(None, sc_line, line).quick_ratio())
                # print("line ", i, " ratio: ", cur_ratio)

    seconds = int(max_ratio_frame.split(".")[0]) - 10
    h, m, s = extract_timestamp(seconds)
    timestamp = '{:d}:{:02d}:{:02d}'.format(h, m, s)

    print("max ratio for line ", idx, " = ", max_ratio, " at time : ", timestamp)
print("\n")
print("TIME TAKEN : ", time.clock() - start)
# ============================================================================================
