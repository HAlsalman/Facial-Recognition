#Facial Detection

Task 1
Two techniques used in the survey paper:
a)	Rigid Templates: Learned mainly by boosting based methods or by the application of deep neural networks. The main line of research in this direction is based on learning rigid templates using boosted cascades of classiﬁers. An example would be the Viola-Jones face detector, which also considered the root of the recent advances in face detection. Then, solutions to two key issues for boosting-based face detection: what features to extract, and which learning algorithm to apply.
b)	Deformable models: describes the face by its parts. It basically breaks the image into pieces based on color differentiations and facial features. Then looks for the location of the facial features and landmarks. This technique requires a high computation time and can become slow.
I have used HAAR cascade technique which creates rectangular features. The features are called the weights. Their intensity is the difference between 2- 4 rectangles. The value of the features are the difference of pixels values in the gray and white rectangles. 4 arrays are used to collect the values since the rectangle has 4 corners. 
My program would create the cascade file from 

cascPath = 'haarcascade_frontalface_default.xml'
This file was supplied from Github with the references provided at the end of this document.
Then create an array to import the frames provided in the project using the code
#create and array from the images
img_array = []
# Read the images provides with the project
for filename in glob.glob('./P2E_S5_C1.1/*.jpg'):
    image = cv2.imread(filename)
    height, width, layers = image.shape
    size = (width, height)

Run HAAR to detect faces, code was imported from GitHub
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)
Once a face is detected, draw a rectangle around it and print the number of faces detected.
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
then append the frame to the array. So later I create the output video from the frames in the array.


Task 2
Code files attached:
face_detect_cv3.py
haarcascade_frontalface_default.xml
project2results.avi
to run the software, the images must by stored in a folder named “P2E_S5_C1.1” and this folder must be in the same directory as the .py and .xml files.


References
S. Zafeiriou, C. Zhang, Z. Zhang, A Survey on Face Detection in the wild: past, present and future, Computer Vision and Image Understanding (2015), doi: http://dx.doi.org/10.1016/j.cviu.2015.03.015
A full guide to face detection, Mael Fabien https://maelfabien.github.io/tutorials/face-detection/#
Face Recognition with Python, in Under 25 Lines of Code https://realpython.com/face-recognition-with-python/
faceDetection https://github.com/maelfabien/Machine_Learning_Tutorials/tree/master/1_Computer%20Vision/FaceDetection
Image Processing http://angeljohnsy.blogspot.com/2012/02/how-to-get-frames-from-video.html
Convert Images(frames) to video https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481
Creating Videos from Images using OpenCV-Python https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/


---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://www.linkedin.com/in/halsalman2/" target="_blank">Hassan Alsalman</a>.
