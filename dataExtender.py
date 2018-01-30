#Creates the negative sample description file 
import argparse
from PIL import Image
import os
from os.path import isfile, join
import sys
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

def progress(count, total, status=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))
        percents = round(100.0 * count / float(total), 1)

        bar = '=' * filled_len + '-' * (bar_len-filled_len)
        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()

parser = argparse.ArgumentParser()
parser.add_argument('datadir', help='The directory of the dataset you want to extend')
parser.add_argument('savedir', help='The directory you want to save the extended dataset to')
parser.add_argument('numPerImg', help='The number of samples you want to create per original image')
args = parser.parse_args()

files = [f for f in os.listdir(args.datadir) if isfile(join(args.datadir, f))]
data = []
for f in sorted(files): 
	data.append(Image.open(args.datadir + "/" + f))
	
datagen = ImageDataGenerator(
	rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

counter = 0
datalen = len(data)
for img in data:
	x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
	x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

	# the .flow() command below generates batches of randomly transformed images
	# and saves the results to the `preview/` directory
	i = 0
	for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=args.savedir, save_prefix='img', save_format='jpeg'):
    		i += 1
    		if i > int(args.numPerImg):
        		break  # otherwise the generator would loop indefinitely
	counter += 1;
	progress(counter, datalen, 'preprocessing dataset')

print("\nComplete")
