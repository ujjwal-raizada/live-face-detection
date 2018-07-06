import pickle
import os

import face_recognition

def load_encodings():
	image_folders = [dI for dI in os.listdir('images') if os.path.isdir(os.path.join('images',dI))]
	print(image_folders)
	encodings = {}

	for folder in image_folders:
		files = [f for f in os.listdir(os.path.join('images', folder))]
		print(files)
		if 'encoding.dat' in files:

			encoding_file = "images/" + folder + "/" + "encoding.dat"
			print(folder)
			with open(encoding_file, 'rb') as f:
				encoding = pickle.load(f)
				encodings[folder] = encoding


	for key, value in encodings.items():
		pass

	return encodings


if __name__ == '__main__':
	load_encodings()

