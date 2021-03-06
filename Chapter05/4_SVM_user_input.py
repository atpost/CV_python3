from sklearn import datasets, metrics, svm


from skimage import io, color, feature, transform

mnist = datasets.load_digits()



images = mnist.images

data_size = len(images)

#Preprocessing images
images = images.reshape(len(images), -1)
labels = mnist.target

#Initialize Logistic Regression
SVM_classifier = svm.SVC(gamma=0.001)

#Training the data on only 75% of the dataset. Rest of the 25% will be used in testing the Logistic Regression
SVM_classifier.fit(images[:int((data_size / 4) * 3)], labels[:int((data_size / 4) * 3)])

#Load a custom image 
digit_img = io.imread('./Chapter05/images/digit.png')

#Convert image to grayscale
digit_img = color.rgb2gray(digit_img)

#Resize the image to 28x28
digit_img = transform.resize(digit_img, (8, 8), mode="wrap")

#Run edge detection on the image 
digit_edge = feature.canny(digit_img, sigma=5) 

io.imshow(digit_img)
io.show()

digit_edge = digit_edge.flatten().reshape(1, -1)

#Testing the data
predictions = SVM_classifier.predict(digit_edge)

print(predictions)
'''
[1]
'''
