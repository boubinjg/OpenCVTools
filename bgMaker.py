#Creates the negative sample description file 
import argparse
from PIL import Image
import os
from os.path import isfile, join
parser = argparse.ArgumentParser()
parser.add_argument('dir', help='The directory of your negative samples')

args = parser.parse_args()

files = [f for f in os.listdir(args.dir) if isfile(join(args.dir, f))]
bg = open('bg.txt', 'w')
for f in sorted(files): 
	bg.write("%s/%s\n" % (args.dir, f));
