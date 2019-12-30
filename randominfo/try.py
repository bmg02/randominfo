from os.path import abspath, isdir
from os import getcwd
import glob
from random import choice
print(choice(glob.glob(getcwd() + "\\images\\people\\*.jpg")))