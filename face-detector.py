import cv2  
import os
import msvcrt
import sched, time
  
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
  
def loop():  
  
    ret, img = cap.read()  

    global count, del_count, last_del, img_format
  
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
            return
        
scheduler = sched.scheduler(time.time, time.sleep)
def run_loop():
    scheduler.enter(0.5, 1, run_loop)
    loop()

run_loop()
scheduler.run()
        
cap.release() 
cv2.destroyAllWindows() 