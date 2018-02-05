import shutil
import os
from os.path import join


def jpg_file(filename):
    return not any(filename.endswith(extension) for extension in [".jpg"])

father_fold = os.getcwd()
lfw_fold = join(father_fold, "lfw")

new_fold = join(father_fold, "CelebA_/")

i=0

for name in os.listdir(lfw_fold):
    name_path = join(lfw_fold, name)
    for imag in os.listdir(name_path):
        imag_path = join(name_path,imag)
        print(imag_path)
        shutil.copyfile(imag_path, new_fold + str(i) + '.jpg')
        i += 1
        print(i)