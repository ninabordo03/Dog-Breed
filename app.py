import streamlit as st
import cv2
import numpy as np
from keras.models import load_model

st.title('Dog Breed App')
st.markdown('Upload an image of a dog')
classes = ['Scottish Deerhound', 'Maltese', 'Afghan Hound']
model = load_model('dog_breed.h5')
img = st.file_uploader('Choose an image', type=['png', 'jpg', 'jpeg', 'webp'])
submit = st.button('Predict')

if submit:
    if img is not None:
        #convert the file into an opencv image
        file_bytes = np.asarray(bytearray(img.read()), dtype = np.uint8)
        opencv_img = cv2.imdecode(file_bytes, 1)
        st.image(opencv_img, channels= 'BGR')
        opencv_img = cv2.resize(opencv_img, (224, 224))
        opencv_img.shape = (1, 224, 224, 3)
        y_pred = model.predict(opencv_img)
        st.title(f'The dog breed is {classes[np.argmax(y_pred)]}')