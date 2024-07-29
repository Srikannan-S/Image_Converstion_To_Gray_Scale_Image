import cv2

# Read the image
img=cv2.imread("flower.png")

# Convert the image into grey scale
Gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Save the gray image
cv2.imwrite("grey.png",Gray_img)

# Display both image
# The names Original and Gray as optional it will display in Result
cv2.imshow('Original',img)  
cv2.imshow('Gray',Gray_img)


cv2.waitKey(5000)
cv2.destroyAllWindows()
