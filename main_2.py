import imgsim
import cv2

img0 = cv2.imread("./samples/Steamboat-Willie.jpg")
img1 = cv2.imread("./files/downloaded_image.jpg")

vtr = imgsim.Vectorizer()
vec0 = vtr.vectorize(img0)
vec1 = vtr.vectorize(img1)

dist = imgsim.distance(vec0, vec1)

print("distance =", dist)
