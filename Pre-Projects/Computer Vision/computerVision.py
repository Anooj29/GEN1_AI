import cv2

image = cv2.imread(r"C:\Users\Anooj Dilip Archana\Desktop\xyz.png")

if image is None:
    print("Error")
else: 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image', image)
    cv2.waitKey(0)