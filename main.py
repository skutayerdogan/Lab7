import cv2

img = cv2.imread('C:\\Users\\MONSTER\\Desktop\\view.jpg')
cv2.imshow('Original_Image', img)

b,g,r = cv2.split(img)

cv2.imshow("Model Blue Image", b)
cv2.imshow("Model Green Image", g)
cv2.imshow("Model Red Image", r)

cv2.imshow("New Model Blue Image", b)
cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imshow("New Blue",b)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Model Blue Image",b)
merge = cv2.merge([b,g,r])
cv2.imshow("Merge",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()
b=img[: :25]
cv2.imshow("",b)

