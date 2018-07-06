import face_recognition
import cv2

import load_encoding


def start_live():
	known_face_encodings = load_encoding.load_encodings()

	# Get a reference to webcam #0 (the default one)
	video_capture = cv2.VideoCapture(0)

	# Only process every other frame of video to save time
	process_this_frame = True

	while True:
		# Grab a single frame of video
		ret, frame = video_capture.read()

		# Resize frame of video to 1/4 size for faster face recognition processing
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

		# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
		rgb_small_frame = small_frame[:, :, ::-1]

		# Only process every other frame of video to save time
		if process_this_frame:
			# Find all the faces and face encodings in the current frame of video
			face_locations = face_recognition.face_locations(rgb_small_frame)
			face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

			face_names = []
			name = "Unknown"
			for face_encoding in face_encodings:

				for name, encodings in known_face_encodings.items():
					matches = face_recognition.compare_faces(encodings, face_encoding, tolerance=0.5)
					print(name + str(matches))
					if all(matches):
						face_names.append(name)
						break

		process_this_frame = not process_this_frame

		# Display the results
		for (top, right, bottom, left), name in zip(face_locations, face_names):
			# Scale back up face locations since the frame we detected in was scaled to 1/4 size
			top *= 4
			right *= 4
			bottom *= 4
			left *= 4

			# Draw a box around the face
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

			# Draw a label with a name below the face
			cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

		# Display the resulting image
		cv2.imshow('Video', frame)

		k = cv2.waitKey(1)
		# Hit 'ESC' on the keyboard to quit!
		if k%256 == 27:
			# ESC pressed
			print("Escape hit, closing...")
			break


	# Release handle to the webcam
	video_capture.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	start_live()
			



