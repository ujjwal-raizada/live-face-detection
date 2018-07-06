import os

import cv2
import face_recognition

import load_encoding
import face_capture
import face_encoding
import update_encoding
import live_recognition


os.system('cls' if os.name == 'nt' else 'clear')

intro = """

  WELCOME TO LIVE-FACE-RECOGNITION

  Select one of the following option:

  1) Capture Image (Create Data Set)
  2) Create encoding for new faces
  3) Update face encoding
  4) Start Live Recognition
  5) Quit

"""

while(True):
	print(intro)

	user_input = input("Enter Choice: ")

	if user_input == '1':
		face_capture.image_capture()

	elif user_input == '2':
		face_encoding.start_face_encoding()

	elif user_input == '3':
		update_encoding.start_update_encoding()

	elif user_input == '4':
		live_recognition.start_live()

	elif user_input == '5':
		break


