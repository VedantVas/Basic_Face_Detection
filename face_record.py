import cv2 # Imports the OpenCV library.

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Loads a pre-trained Haar Cascade classifier to detect frontal human faces.
webcam = cv2.VideoCapture(0) # Starts video capture using your webcam, here 0 represents default camera.
while True: # Begins an infinite loop to keep reading webcam frames continuously.
    _,img = webcam.read() # Reads a single frame from the webcam, img contains the image/frame.
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Converts the color frame to grayscale. Haar cascade works better on grayscale images as it reduces computational complexity
    
    faces = face_cascade.detectMultiScale(gray,1.6,4)
    #detects faces in the grayscale image using a scale factor of 1.6 and requires at least 4 nearby rectangles to confirm a face
    
    for(x,y,w,h) in faces:#Iterates through each detected face and retrieve
    # x, y: top-left corner of face rectangle    
    # w, h: width and height of the face    
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) # Draws a green rectangle on the original image around the face.
        # (0, 255, 0): Green color in BGR format.
        # 3: Thickness of the rectangle border
    
    cv2.imshow("Face Detection",img) # Displays the image in a window titled "Face Detection"
    
    key = cv2.waitKey(10) #Waits for 10 milliseconds for a keyboard key press, it returns ASCII value of that key
    
    if key == 27: # Checks if the Esc key (27) is pressed.
        break # If yes break the loop and webcam gets closed
        
webcam.release() # Releases the webcam so it can be used by other programs.

cv2.destroyAllWindows() # Closes all OpenCV-created windows.  
