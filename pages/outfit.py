import streamlit as st
from PIL import Image
from outfit.outfit_model import change_outfit


def show_outfit():

    # ---------- SAME STYLE AS COLORIZER ----------

    st.markdown("""
    <style>

    .block-container
    {
        max-width: 1100px;
        padding-top: 0rem;
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



    # ---------- BACK BUTTON ----------

    if st.button("⬅ Back"):

        st.session_state.page = "home"
        st.rerun()



    # ---------- TITLE ----------

    st.title("👕 AI Outfit Changer")



    st.write("")
    st.write("")



    # ---------- FILE UPLOAD ----------

    uploaded = st.file_uploader(

        "Upload person image",

        type=["jpg", "png", "jpeg"]

    )



    st.write("")
    st.write("")



    # ---------- SELECT ----------

    option = st.selectbox(

        "Select Outfit",

        [

            "Traditional",
            "Western",
            "Formal",
            "School Uniform"

        ]

    )



    st.write("")
    st.write("")



    # ---------- RESULT ----------

    if uploaded:

        image = Image.open(uploaded).convert("RGB")


        col1, col2, col3 = st.columns([1,2,1])

        with col2:

            st.image(
                image,
                use_container_width=True
            )



        st.write("")



        if st.button("Generate Outfit"):


            with st.spinner("Generating Outfit..."):


                result = change_outfit(image, option)



            col1, col2, col3 = st.columns([1,2,1])


            with col2:

                st.image(
                    result,
                    use_container_width=True
                )