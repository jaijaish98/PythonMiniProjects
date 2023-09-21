import cv2
import os
import numpy as np
from sklearn import neighbors


# Function to load images and labels for training
def load_images_and_labels(data_path):
    images = []
    labels = []
    label = 0

    for person_folder in os.listdir(data_path):
        person_path = os.path.join(data_path, person_folder)
        print(person_folder, person_path)
        if os.path.isdir(person_path):
            for filename in os.listdir(person_path):
                img_path = os.path.join(person_path, filename)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                images.append(img)
                labels.append(label)
            label += 1
        print(images)

    return np.array(images), np.array(labels)


# Load images and labels for training
data_path = '/Users/jayendrans/jaijaish98/Work/Programming/Python/Python Mini Projects/FaceRecognition-Basic/Images'  # Update this with your data path
images, labels = load_images_and_labels(data_path)

# Train the k-NN model
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(images.reshape(len(images), -1), labels)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Load the face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face
        face = gray[y:y + h, x:x + w]

        # Resize the face to match the training data
        face_resized = cv2.resize(face, (100, 100))

        # Predict the label for the face
        label_predicted = knn.predict(face_resized.flatten().reshape(1, -1))

        # Display the name of the predicted person
        cv2.putText(frame, f'Person: {label_predicted[0]}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
