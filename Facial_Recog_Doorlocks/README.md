# SMART DOOR LOCKS WITH FACIAL RECOGNITION

This project aims to develop a smart door lock system that uses facial recognition technology to unlock doors. The system is built using a Raspberry Pi 4 kit, Python programming language, OpenCV library, and a pre-trained network model by Davis King on a dataset of approximately 3 million images, using the Labeled Faces in the Wild (LFW) dataset. The system is capable of detecting faces and switching between unlock modes, providing a convenient and secure way to unlock doors.

## Features
* Facial recognition-based door unlocking
* Manual password input for unlocking
* Touchscreen interface for switching between unlock modes
* Real-time camera feed display
* High accuracy face detection and identification
* Independent operation from a computer
## System Requirements
* Raspberry Pi 4 kit
* Python programming language
* OpenCV library
* Pre-trained network model
* Haar-Cascade for face detection
* Adaboost algorithms for facial recognition
* 3.5-inch LCD display
* Servo for door locking mechanism
* 5V power supply

## System Description
The smart door lock system consists of the following components:

* Input block: Camera
* Processing block: Raspberry Pi 4 kit
* Display block: 3.5-inch LCD screen
* Execution block: Servo
* Power block: 5V power supply

When the system is powered on, the central system initializes and displays the interface with the keypad and camera frame. The camera captures video frames, which are then processed by the Raspberry Pi 4 using facial detection and recognition algorithms. The system identifies faces and compares them with the trained data to determine whether to unlock the door. Additionally, users can enter a password on the touchscreen to unlock the door manually.

## How it works
1. Power up the smart door lock system.
2. The camera captures video frames and sends them to the processing block.
3. The Raspberry Pi 4 processes the video frames and detects faces using Haar-Cascade and Adaboost algorithms.
4. The identified faces are preprocessed to enhance image quality and input to the convolutional neural network model.
5. The model classifies the faces and compares them with the trained data.
6. If a match is found, the servo unlocks the door. If not, the system labels the face as "unknown" and keeps the door locked.
7. Users can also input a password on the touchscreen interface to unlock the door manually.

This project provides a comprehensive solution for smart door lock systems that integrate facial recognition technology, offering users a convenient and secure way to access their homes or offices.