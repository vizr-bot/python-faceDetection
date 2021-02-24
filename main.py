import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640) #lebar kamera
cam.set(4, 480) #tinggi kamera

faceDetector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    retV, frame = cam.read() #Membaca frame
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 4)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame',frame)

    #bikin tombol exit
    ex = cv2.waitKey(1) & 0xff
    if ex == 27:
        break

cam.release()
cv2.destroyAllWindows()