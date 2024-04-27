import streamlit as st
from PIL import Image
import cv2, os
import numpy as np
from ultralytics import YOLO

st.set_page_config(page_title="YOLOv5 Detection", page_icon=":sparkles:", layout="wide")

# Load Assets
model = YOLO('yolov8n.pt')
yolo = Image.open("img/YOLO.png")
detect = []


# ---- HEADER SECTION ----
with st.container():
    st.subheader("A simple Image Detection program By Meutia Tri Mulyani")
    st.title("Welcome to my YOLO Detection System! :wave:")
    st.write(
        "Wanna Know More About Me? -> https://www.linkedin.com/in/meutia-tri-mulyani-1b79b6227/"
    )
    st.write("*Scroll down!*")


with st.container():
    st.write("---")
    st.header("YOLO Detection")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        # Upload file foto
        uploaded_file = st.file_uploader("Choose a image file", type="jpg")
        if uploaded_file is not None:
            # Convert foto dengan opencv
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, 1)
            opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
            detect.append(opencv_image)            
            # Menampilkan foto
            st.image(opencv_image, channels="RGB")

    with right_column:
        # menampilkan hasil prediksi
        st.write("##")
        Generate = st.button("PREDICT YOLO")
        if Generate:
            results = model(detect)
            for result in results:
                boxes = result.boxes  # Boxes object for bounding box outputs
                masks = result.masks  # Masks object for segmentation masks outputs
                keypoints = result.keypoints  # Keypoints object for pose outputs
                probs = result.probs  # Probs object for classification outputs
                result.save(filename='img/result.jpg')  # save to disk
                img_result = Image.open("img/result.jpg")
                st.image(img_result, channels="RGB")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About YOLO")
        st.write("##")
        st.write(
            """
            YOLO (You Only Look Once) is a popular object detection model known for its speed and accuracy. It was first introduced by Joseph Redmon et al. in 2016 and has since undergone several iterations, the latest being YOLO v7.
"""
        )
    with right_column:
        st.image(yolo, use_column_width='auto')
        st.subheader("Structure of YOLO")
        


    