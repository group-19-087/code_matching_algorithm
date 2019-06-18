from difflib import SequenceMatcher
import argparse
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
