import requests
from requests.exceptions import ConnectionError
import argparse
from io import BytesIO 
from PIL import Image
import time
from tqdm import tqdm
import sys

def progress(count, total, status=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))
	percents = round(100.0 * count / float(total), 1)
	
	bar = '=' * filled_len + '-' * (bar_len-filled_len)
	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
	sys.stdout.flush()

parser = argparse.ArgumentParser()
parser.add_argument('file', help='the text file with urls to downloadable images as your second argument')
parser.add_argument('dir', help='the directory for your downloaded images')
parser.add_argument('fname', help='the name you wish to give your downloaded files')
args = parser.parse_args()

numLines = sum(1 for line in open(args.file))
with open(args.file) as f:
	counter = 0
	for line in f:
		try:
			response = requests.get(line)
			img = Image.open(BytesIO(response.content))	
			img.save(args.dir + "/"+args.fname + str(counter)+".jpg")
		except (ConnectionError, IOError) as e:
			pass
		counter += 1
		progress(counter, numLines, "Downloading");
print("\nComplete")
