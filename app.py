import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

#load the pre-trained model
agemodel = load_model("./models/convnet_from_scratch_with_augmentation1.keras")
gendermodel = load_model("./models/convnet_from_scratch_with_augmentation2.keras")

#Define a function for predictions
def predict_age_gender(image):
    #Preprocess the image
    image = image.resize((200, 200)) #Resize to model's input size
    image_array = np.array(image) / 255.0 #Normalize
    image_array = np.expand_dims(image_array, axis=0) #Add batch dimension

    #Predict age and gender
    ageprediction = agemodel.predict(image_array)
    genderprediction = gendermodel.predict(image_array) 

    gender = "Male" if genderprediction[0][0] > 0.5 else "Female"
    age = int(ageprediction[0][0]) # Assuming regression for age
    return gender, age

# Streamlit App
st.title("Age and Gender Prediction")

# File uploader for image input
uploaded_file = st.file_uploader("Upload an image of a face", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    #Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Make predictions
    gender, age = predict_age_gender(image)
    st.write(f"**Predicted Gender:** {gender}")
    st.write(f"**Predicted Age:** {age}")
    st.write(f"**Predicted Gender:** {gender}")
    st.write(f"**Predicted Age:** {age}")