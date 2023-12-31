import cv2  
import os
import msvcrt
  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
  
cap = cv2.VideoCapture(0) 
count = 0
del_count = 0
last_del = 0
img_format = ".jpg"

dir_path = "images/"
for file_name in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file_name)):
        os.remove(os.path.join(dir_path, file_name))
  
while True:  
  
    ret, img = cap.read()  
  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
  
    if len(faces) != 0:
        cv2.imwrite(f"images/faces{count}{img_format}", img)
        count += 1

        if count - last_del > 100:
            for i in range(last_del, count - 10):
                file_path = f"images/faces{i}{img_format}"
                os.remove(file_path)

            last_del = count - 10

            if count > 64000:
                for file_name in os.listdir(dir_path):
                    if os.path.isfile(os.path.join(dir_path, file_name)):
                        os.remove(os.path.join(dir_path, file_name))

                count = 0
                last_del = 0
        
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'q':
            break
        
cap.release() 
cv2.destroyAllWindows() 