import streamlit as st
import os
from PIL import Image

def display_image_gallery(image_folder="images"):
    # Get list of image files
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        st.warning(f"No images found in the '{image_folder}/' folder. Please add images to display them here.")
    else:
        cols = st.columns(3)  # 3 images per row
        for index, image_file in enumerate(image_files):
            img_path = os.path.join(image_folder, image_file)
            image = Image.open(img_path)

            # Display image in the corresponding column without caption
            with cols[index % 3]:  
                st.image(image, use_container_width=True)
