# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:58:45 2022

@author: Hugh
"""

# Importing required packages
import tensorflow as tf
import tensorflow.keras.applications.xception as xception
import streamlit as st
import cv2
from PIL import Image, ImageOps
import numpy as np

# Importing the model
model = tf.keras.models.load_model('my_model.hdf5')

# Creating a header for user to upload their images
st.write("""
         # Garbage classification
         """
         )

st.write("This is a simple image classification web app to predict different categories of garbage")

file = st.file_uploader("Please upload an image file", type = ["jpg", "png"])

# Pre-process the image
def import_and_predict(image_data, model):
    
        size = (320,320)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(320, 320),    interpolation=cv2.INTER_CUBIC))/255
        
        img_reshape = img_resize[np.newaxis,...]
    
        prediction = model.predict(image)
        
        return prediction
    
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) == 0:
        st.write("It is a Paper!")
    elif np.argmax(prediction) == 1:
        st.write("It is a Cardboard!")
    elif np.argmax(prediction) == 2:
        st.write("It is a Plastic!")
    elif np.argmax(prediction) == 3:
        st.write("It is a Metal!")
    elif np.argmax(prediction) == 4:
        st.write("It is a Trash!")
    elif np.argmax(prediction) == 5:
        st.write("It is a Battery!")
    elif np.argmax(prediction) == 6:
        st.write("It is a Shoe!")
    elif np.argmax(prediction) == 7:
        st.write("It is Clothes!")
    elif np.argmax(prediction) == 8:
        st.write("It is a green-glass!")
    elif np.argmax(prediction) == 9:
        st.write("It is a brown-glass!")
    elif np.argmax(prediction) == 10:
        st.write("It is a white-glass!")
    else:
        st.write("It is a biological waste!")
    
    st.text("Probability (0: Paper, 1: Rock, 2: Scissor, 3: Metal, 4: Trash, 5: Battery, 6: Shoe, 7: Clothes, 8: Green Glass, 9: Brown Glass, 10 = White glass, 11: Biological")
    st.write(prediction)
    
