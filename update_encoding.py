import pickle
import os

import face_recognition

image_folders = [dI for dI in os.listdir('images') if os.path.isdir(os.path.join('images',dI))]
print(image_folders)


for folder in image_folders:
	files = [f for f in os.listdir(os.path.join('images', folder))]
	print(files)
	
	encoding = []
	for image in files:
		if image != "encoding.dat":
			image_file = "images/" + folder + "/" + image
			print(image_file)
			img = face_recognition.load_image_file(image_file)
			if face_recognition.face_encodings(img) != []:
				img_encode = face_recognition.face_encodings(img)[0]
				encoding.append(img_encode)
		
		

	encoding_file = "images/" + folder + "/" + "encoding.dat"
	with open(encoding_file, 'wb') as f:
		pickle.dump(encoding, f)
		print("Encoding created for: "+folder)





