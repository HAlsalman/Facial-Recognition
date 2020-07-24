import matplotlib.pyplot as plt
import cv2
import glob

font = cv2.FONT_HERSHEY_SIMPLEX

cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

# Load the image
img_array = [] #create array for the frames
for filename in glob.glob('./P2E_S5_C1.1/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)

    plt.figure(figsize=(12,8))
    plt.imshow(img, cmap='gray')
    plt.show()

    faces = faceCascade.detectMultiScale(
        img,
        scaleFactor=1.1,
        minNeighbors=5,
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # For each face
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)



    plt.figure(figsize=(12,8))
    plt.imshow(img, cmap='gray')
    plt.show()
    print("Found {0} faces!".format(len(faces)))
    img_array.append(img) #now add the image with the face to the array


out = cv2.VideoWriter('project2results.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()