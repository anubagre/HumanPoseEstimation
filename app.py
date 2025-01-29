import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

#Streamlit app title
st.title('Human Pose Estimation')

#File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

#If an image is uploaded
if uploaded_file is not None:
    #Open the image
    img = Image.open(uploaded_file)

    #Display the image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    #Optionally, show the image details
    st.write(f"Image Format: {img.format}")
    st.write(f"Image Size: {img.size}")


    mp_pose = mp.solutions.pose 
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5) 
    mp_drawing = mp.solutions.drawing_utils 

    #Load an image 
    image = np.array(img) 
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
    #Perform pose estimation 
    results = pose.process(image_rgb) 
    #Copy the image for annotation
    annotated_image = image.copy()

    #Draw landmarks
    if results.pose_landmarks: 
        st.write("Pose landmarks detected!") 
        for landmark in results.pose_landmarks.landmark:
            h,w,c= image.shape
            #Convert normalized coordinates to pixel coordinates
            cx, cy = int(landmark.x * w), int(landmark.y * h)
            #Draw keypoints
            cv2.circle(annotated_image, (cx, cy), 5, (0, 255, 0), -1)

        #Draw full landmarks on the image
        mp_drawing.draw_landmarks(
            annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
        )
    
    #Convert OpenCV BGR image back to RGB for Streamlit display
    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    
    #Display the output image 
    st.image(annotated_image, caption="Annotated Image", use_column_width=True)
    pose.close()