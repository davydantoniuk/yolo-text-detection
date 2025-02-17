import streamlit as st
import torch
import numpy as np
import cv2
from PIL import Image
from ultralytics import YOLO
import logging
from io import BytesIO
import os

logging.getLogger(
    "streamlit.watcher.local_sources_watcher").setLevel(logging.ERROR)


@st.cache_resource
def load_model():
    model_path = "YOLOv8m.pt"
    model = YOLO(model_path)
    return model


model = load_model()

st.title("📖 Text Area Detection with YOLOv8")
st.write("Upload an image, and the model will detect text regions.")

uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Get original filename without extension
    original_filename = os.path.splitext(uploaded_file.name)[0]

    image = Image.open(uploaded_file)
    img_array = np.array(image)
    img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    results = model(img_cv)

    # Draw rectangles on detected text areas
    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box[:4])
            cv2.rectangle(img_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)

    output_img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    st.image(output_img, caption="Detected Text Areas",
             use_container_width=True)

    # Convert to PIL Image and save to bytes buffer
    output_pil = Image.fromarray(output_img)
    buf = BytesIO()
    output_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Construct new file name: original_name_detect.png
    processed_filename = f"{original_filename}_detect.png"

    # Update download button with new filename
    st.download_button(
        label="Download Processed Image",
        data=byte_im,
        file_name=processed_filename,
        mime="image/png"
    )
