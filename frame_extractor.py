import os

def extract_frames(input_video):
    if not os.path.exists('images'):
        os.makedirs('images')
    os.system("ffmpeg -i {0} -vf fps=fps=0.2 images/%04d.tiff -hide_banner".format(input_video))
    return
