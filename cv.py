import cv2
import numpy as np
from tensorflow.keras.models import load_model


model = load_model("digit_model.h5")
img = cv2.imread("download.png", cv2.IMREAD_GRAYSCALE)  
if img is None:
    raise ValueError("Image not found. Check the filename and path.")

img = cv2.resize(img, (28, 28))
img = 255 - img
img = img / 255.0
img = img.reshape(1, 28, 28, 1)
prediction = model.predict(img)
predicted_digit = np.argmax(prediction)

print(f"Predicted digit: {predicted_digit}")
