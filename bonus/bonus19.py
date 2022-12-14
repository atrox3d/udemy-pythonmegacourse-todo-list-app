import streamlit as st
from PIL import Image
import pathlib


def save_camera_image(camera_image):
    image_path = pathlib.Path("camera-photos", camera_image.name)
    image_path.parent.mkdir(exist_ok=True)
    with open(image_path, 'wb') as image_file:
        image_file.write(camera_image.getbuffer())
        print(f"file {image_path} saved")
        st.write(f"file {image_path} saved")


def save_grayscale_image(gray_img, name):
    image_path = pathlib.Path("camera-photos", name)
    image_path.parent.mkdir(exist_ok=True)
    image_path = pathlib.Path(
        image_path.parent,
        image_path.stem + "GRAY" + image_path.suffix
    )
    gray_img.save(image_path)
    print(image_path, "saved")
    st.write(image_path, "saved")


uploaded_image = st.file_uploader("Upload Image")

print("uploaded_image", uploaded_image)
st.write("uploaded_image", uploaded_image)

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

print("camera_image", camera_image)
st.write("camera_image", camera_image)

if camera_image:
    save_camera_image(camera_image)

    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)

    save_grayscale_image(gray_img, camera_image.name)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)

    save_grayscale_image(gray_img, uploaded_image.name)
