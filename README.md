# Live Face Detection

Live face detection software, with encoding handler.
it save encoding of every person separately so that it can be used later.

## Setup

First install dependencies:

```
install -r requirements.txt
```

then run main.py

```
python3 main.py
```

it will display you the following menu:

```
  WELCOME TO LIVE-FACE-RECOGNITION

  Select one of the following option:

  1) Capture Image (Create Data Set)
  2) Create encoding for new faces
  3) Update face encoding
  4) Start Live Recognition
  5) Quit
```

breakdown:

1) To create image library of a new person. Press 'Space' to take pictures in different angles. and ESC to close.

2) Create encoding of newly added faces.

3) Update encoding of the all the faces

4) Start live detection, opens a OpenCV window with webcam support.

5) Quit