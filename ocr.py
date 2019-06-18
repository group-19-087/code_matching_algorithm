from PIL import Image # import the necessary packages
import pytesseract
import argparse
import cv2
import os
import re

ap = argparse.ArgumentParser()
ap.add_argument("--path", required=True,
	help="path to input images to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

# ============================================================================================

# ============================================================================================


def extract_text(mpath_to_File, mpreprocess):
	# load the example image and convert it to grayscale
	image = cv2.imread(mpath_to_File)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# check to see if we should apply thresholding to preprocess the image
	if mpreprocess == "thresh":
		gray = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	# make a check to see if median blurring should be done to remove
	# noise
	elif mpreprocess == "blur":
		gray = cv2.medianBlur(gray, 3)

	# write the grayscale image to disk as a temporary file so we can
	# apply OCR to it
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)
	return text

# ============================================================================================

# ============================================================================================

def write_to_disk(string, filename):
	output_filename = filename.replace("jpg", "txt")
	save_path = "./output"
	if not (os.path.exists(save_path)):
		try:  
			os.mkdir(save_path)
		except OSError:  
			print ("Creation of the directory %s failed" % save_path)
		else:  
			print ("Successfully created the directory %s " % save_path)
	with open(os.path.join(save_path, output_filename), "w") as ocr_file:
		# ocr_file.write(re.sub('\s+',' ',string))
		ocr_file.write(string)
	return

# ============================================================================================

# ============================================================================================

files = os.listdir(args["path"])
preprocess = args["preprocess"]
for file in files:
	path_to_File = os.path.join(args["path"], file)
	print(path_to_File)
	write_to_disk(extract_text(path_to_File, preprocess), file)

# ============================================================================================
