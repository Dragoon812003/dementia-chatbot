import cv2  
import os
import msvcrt
import sched, time
import requests
  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
  
cap = cv2.VideoCapture(0) 

img_format = ".jpg"
upload_url = "http://host:port/endpoint"
upload_interval = 30
last_img_upload_time = -upload_interval
  
def loop():  

    ret, img = cap.read()  

    global count, del_count, last_del, img_format
  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
  
    if len(faces) != 0:
        if time.time() - last_img_upload_time >= upload_interval:
            _, img_encoded = cv2.imencode(img_format, img)
            image_data = img_encoded.tostring()
            image = {'image': (f'image{img_format}', image_data, 'image/jpeg')}
            response = requests.post(upload_url, files=image)
            last_img_upload_time = time.time()
        
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