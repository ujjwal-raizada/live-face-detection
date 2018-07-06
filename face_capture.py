import cv2
import os

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def image_capture():

	name = input("Enter your name: ")

	dir_name = "images/" + name

	if not os.path.exists(dir_name):
		os.mkdir(dir_name)

	cam = cv2.VideoCapture(0)

	cv2.namedWindow("test")

	img_counter = 0

	while True:
		ret, frame = cam.read()


		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30),
		)

		# Draw a rectangle around the faces

		frame_copy = frame
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)



		cv2.imshow("Data Input ()", frame)
		if not ret:
			break
		k = cv2.waitKey(1)

		if k%256 == 27:
			# ESC pressed
			print("Escape hit, closing...")
			break
			
		elif k%256 == 32:
			# SPACE pressed
			img_name = "images/"+name+"/"+name+"_{}.jpg".format(img_counter)
			cv2.imwrite(img_name, frame_copy)
			print("{} written!".format(img_name))
			img_counter += 1

	cam.release()

	cv2.destroyAllWindows()

if __name__ == "__main__":
	image_capture()
