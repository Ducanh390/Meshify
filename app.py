import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces[0] # Get all 468 landmarks position over face
        for i in face:
            cv2.circle(img,i,2,(0,255,0),cv2.FILLED) # Drawing custom circle over landmark
    cv2.imshow("Camera Feed",img)
    cv2.waitKey(1)