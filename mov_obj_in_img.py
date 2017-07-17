__author__ = 'awinash'
import cv2
img=cv2.imread("b.jpg")
cv2.namedWindow("window",cv2.WND_PROP_FULLSCREEN)
row,col,ch=img.shape
print row,col,ch

face=img[98:380,356:530]

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print x,y
# Create a black image, a window and bind the function to window


cv2.setMouseCallback('window',draw_circle)

while(1):

    img[98:380,0+360:174+360]=face

    cv2.imshow('window',img)


    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()