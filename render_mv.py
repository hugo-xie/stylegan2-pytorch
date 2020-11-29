from glob import glob
import os

resize = 256

img_paths = glob(os.path.join("./sample", "*.png"))

for img in img_paths[:4]:
    print(img)
    flag = True
    command = "python gennerate_f_image.py  --ckpt stylegan2-ffhq-config-f.pt --size 1024  {:s}".format(img)
    tem = os.popen(command)
    while flag:
        file_name = os.path.splitext(os.path.basename(img))[0] + "-project.png"
        if os.path.exists(file_name):
            flag = False