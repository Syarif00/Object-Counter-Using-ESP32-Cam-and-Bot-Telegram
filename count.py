import cv2
import urllib.request
import numpy as np
import requests
from collections import Counter

 
url='http://YOUR_IP_ADDRESS/'
lst=[]
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / z '''
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
 
while True:
    img_resp=urllib.request.urlopen(url+'cam-lo.jpg')
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)
    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(cv2.GaussianBlur(gray,(11,11),0),30,150,3)
    dilated=cv2.dilate(canny,(1,1),iterations=2)
    (Cnt,_)=cv2.findContours(dilated.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    k=img
    
    cv2.drawContours(k,Cnt,-1,(0,255,0),2)
 
    cv2.imshow("mit contour",canny)

    cv2.imshow("live transmission",img)
    key=cv2.waitKey(5)
    
    if key==ord('q'):
        break
 
    elif key==ord('a'):
        cow=len(Cnt)
        lst.append(cow)
        print(cow)

cv2.destroyAllWindows()

TOKEN = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"
x=Counter(lst)
y=max(x,key=x.get)
message = 'Jumlah Object Terdeteksi: '+str(y)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())