Real-Time ASL Gesture Recognition
-
A deep learning-based system to recognize American Sign Language (ASL) gestures in real time using hand landmarks.


---

About the Project
-
This project was created as part of a final year major project with the goal of making communication more accessible. It uses real-time webcam input to detect and identify ASL gestures, converting them to text and speech.


Instead of working with image datasets, this system uses hand landmark data for a lightweight and accurate prediction model.


---
Features
-
1) Real-time ASL recognition via webcam

2) Trained on .npy landmark data, not images

3) Uses a custom deep learning model

4) Simple, clean output and fast performance

5) Easy to retrain or extend to new gestures



---

Tech Stack
-
>Python

>MediaPipe

>OpenCV

>TensorFlow / Keras

>NumPy

>Tkinter (for GUI)



---

Folder Structure
-
```
Real-Time-ASL-Gesture-Recognition/
├── data/               # Landmark training data (.npy)
├── models/             # Trained model (.h5), class names
├── src/                # All project scripts
├── demo/               # Screenshots
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```
---

## Preview

Here are some screenshots of the real-time ASL gesture recognition in action:

<h3>ASL Gesture Recognition - Screenshot</h3>

<img src="https://github.com/user-attachments/assets/5582e240-6585-4032-9ffd-f960d2aef9af" alt="ASL Output Screenshot" width="500">

<img src="https://github.com/user-attachments/assets/c3397ff7-38fc-4db2-9a2f-f3f5fa60931d" alt="ASL Demo Screenshot" width="300">

---

Getting Started
-
1. Clone the repo



    >git clone https://github.com/kaushiks-info/Real-Time-ASL-Gesture-Recognition.git
cd Real-Time-ASL-Gesture-Recognition

2. Install dependencies



   ```pip install -r requirements.txt```

3. Run the gesture recognizer



   ```python src/asl_recognition.py```

4. (Optional) Collect your own data and train:



   ```python src/data_collection.py```
   
   ```python src/train_model.py```


---

How It Works
-
1) MediaPipe detects 21 hand landmarks from webcam input

2) These are passed as numerical data into a trained model

3) The model predicts the corresponding ASL gesture

4) The prediction is displayed in real time



---

License
-
>This project is licensed under the MIT License.


---
