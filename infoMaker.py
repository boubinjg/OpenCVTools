#Creates the negative sample description file 
import argparse
from PIL import Image
import os
from os.path import isfile, join
import sys 

parser = argparse.ArgumentParser()
parser.add_argument('dir', help='The directory of your positive samples')
parser.add_argument('width', help='width of your new sample')
parser.add_argument('height', help='height of your new sample')

args = parser.parse_args()

def progress(count, total, status=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))
        percents = round(100.0 * count / float(total), 1)

        bar = '=' * filled_len + '-' * (bar_len-filled_len)
        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

size = int(args.width), int(args.height)
files = [f for f in os.listdir(args.dir) if isfile(join(args.dir, f))]
bg = open('info.dat', 'w')
counter = 0
for f in sorted(files): 
	im = Image.open(args.dir + '/' +f)
	img = im.resize(size, Image.ANTIALIAS)
	#im = im.resize(size, Image.ANTIALIAS)
	img.save(args.dir + '/' + f, "JPEG")
	bg.write("%s/%s 1 0 0 %s %s\n" % (args.dir, f, args.width, args.height));
	counter += 1
	progress(counter, len(files), "Writing and Resizing");
		
print("\nComplete")
