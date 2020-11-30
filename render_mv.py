from glob import glob
import os

resize = 256

img_paths = glob(os.path.join("/home/xieyu/project/aligned", "*.png"))

for img in img_paths[:4]:
    file_name = "/home/xieyu/project/stylegan2-pytorch/video/"+os.path.splitext(os.path.basename(img))[0] + "-project.png"
    print(file_name)
    flag = True
    command = "python gennerate_f_image.py  --ckpt stylegan2-ffhq-config-f.pt --size 1024  {:s}".format(img)
    tem = os.popen(command)
    while flag:
        if os.path.exists(file_name):
            flag = False