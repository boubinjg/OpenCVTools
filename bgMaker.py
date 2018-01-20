#Creates the negative sample description file 
import argparse
from PIL import Image
import os
from os.path import isfile, join
import sys

def progress(count, total, status=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))
        percents = round(100.0 * count / float(total), 1)

        bar = '=' * filled_len + '-' * (bar_len-filled_len)
        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

parser = argparse.ArgumentParser()
parser.add_argument('dir', help='The directory of your negative samples')

args = parser.parse_args()

files = [f for f in os.listdir(args.dir) if isfile(join(args.dir, f))]
bg = open('bg.txt', 'w')
counter = 0
for f in sorted(files): 
	bg.write("%s/%s\n" % (args.dir, f));
	counter += 1
	progress(counter, len(files), "Writing")
print("\nComplete")
