import cv2
import os

face_cascade = cv2.CascadeClassifier(
  os.path.realpath("haarcascade_frontalface_default.xml"))
video = cv2.VideoCapture(0)
a = 1
while True:
  a += 1
  check, frame = video.read()
  print(check)
  print(frame)
  gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05,
                                        minNeighbors=5)
  for x, y, w, h in faces:
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
  cv2.imshow("Capture", frame)
  key = cv2.waitKey(1)
  if key == ord('q'):
    break

print(a)
video.release()
cv2.destroyAllWindows()
