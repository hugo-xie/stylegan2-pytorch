from glob import glob
import os

resize = 256

img_paths = glob(os.path.join("./sample", "*.png"))
for img in img_paths:
    command = "python gennerate_f_image.py  --ckpt stylegan2-ffhq-config-f.pt --size 1024  {:s}".format(img)
    tem = os.popen(command)