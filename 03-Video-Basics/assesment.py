import cv2

# Create a function based on a CV2 Event (Left button click)

# mouse callback function
def draw_circle(event,x,y,flags,param):

    global center,clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if clicked:
            clicked = False
        else:
            center = (x,y)
            clicked = True   

        
# Haven't drawn anything yet!
center = (0,0)
clicked = False


# Capture Video

cap = cv2.VideoCapture(0)

# Create a named window for connections
cv2.namedWindow('Test')

# Bind draw_rectangle function to mouse cliks
cv2.setMouseCallback('Test', draw_circle) 


while True:
    # Capture frame-by-frame
    res,frame = cap.read()
    
    if clicked:
        cv2.circle(frame,center=center,radius=20,color=(0,255,255),thickness=10)
    
    cv2.imshow('Test', frame)

    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()