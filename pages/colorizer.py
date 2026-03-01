import streamlit as st
from PIL import Image
import cv2

from utils.model import load_model, colorize_image


# Load model
net = load_model()


def show_colorizer():

    # ---------- STYLE ----------
    st.markdown("""
    <style>

    .block-container
    {
        max-width: 1100px;
        padding-top: 30px;
        padding-bottom: 30px;
        margin: auto;
    }

    .stApp
    {
        background: linear-gradient(
            135deg,
            #0f2027,
            #203a43,
            #2c5364
        );
        color: white;
    }

    h1
    {
        font-size: 42px !important;
        font-weight: 700 !important;
    }

    </style>
    """, unsafe_allow_html=True)



    # ---------- TITLE ----------
    st.title("🎨 Welcome To AI Image Colorizer")



    # ---------- BACK BUTTON ----------
    if st.button("⬅ Back"):

        st.session_state.page = "home"
        st.rerun()



    st.write("")
    st.write("")



    # ---------- UPLOAD ----------
    uploaded = st.file_uploader(
        "Upload Black & White Image",
        type=["jpg", "png", "jpeg"]
    )



    st.write("")
    st.write("")



    # ---------- COLORIZE ----------
    if uploaded:

        image = Image.open(uploaded).convert("RGB")


        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st.image(image, use_container_width=True)



        st.write("")


        if st.button("Colorize Image"):

            result = colorize_image(net, image)


            col1, col2, col3 = st.columns([1,2,1])

            with col2:

                st.image(result, use_container_width=True)


                file = cv2.imencode(".jpg", result)[1].tobytes()


                st.download_button(
                    "Download Image",
                    file,
                    "colorized.jpg"
                )



    # ---------- SPACE ----------
    st.write("")
    st.write("")
    st.write("")



    # ---------- FIRST IMAGE ----------
    col1, col2, col3 = st.columns([1,5,1])

    with col2:

        example1 = Image.open("assets/babyy.jpg")

        st.image(
            example1,
            use_container_width=True
        )



    # ---------- SPACE ----------
    st.write("")
    st.write("")
    st.write("")



    # ---------- SECOND IMAGE ----------
    col1, col2, col3 = st.columns([1,5,1])

    with col2:

        example2 = Image.open("assets/family.jpg")

        st.image(
            example2,
            use_container_width=True
        )



    st.write("")
    st.write("")