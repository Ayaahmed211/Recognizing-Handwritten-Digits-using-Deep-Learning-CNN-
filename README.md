
# 🧠 Handwritten Digit Recognition using Deep Learning (CNN)

This project demonstrates how to build and use a Convolutional Neural Network (CNN) to recognize handwritten digits (0–9) using the MNIST dataset. It includes a model training script and a prediction script using OpenCV to test your own digit images.

> ✅ Built with TensorFlow, Keras, NumPy, and OpenCV  
> 📂 Designed for learning deep learning and computer vision  
> 🎯 Goal: Train a CNN and use it to predict digits from images

## 🧠 How It Works

### ✅ Training the Model (`nums.py`)
- Loads and preprocesses the MNIST dataset (grayscale 28x28 images)
- Uses a CNN with:
  - Conv2D layers
  - MaxPooling
  - Dropout for regularization
  - Dense layers for classification
- Trains the model and saves it as `digit_model.h5`

### ✅ Predicting Digits (`cv.py`)
- Loads a custom image using OpenCV
- Converts the image to grayscale
- Resizes it to 28×28
- Normalizes and reshapes it for model input
- Uses the trained model to predict the digit

---

## 🧩 Requirements

- Python 3.7 or later
- TensorFlow
- NumPy
- OpenCV
