import streamlit as st

from pages.home import show_home
from pages.colorizer import show_colorizer
from pages.outfit import show_outfit

# -------- PAGE CONFIG --------

st.set_page_config(
    layout="wide",
    page_title="AI Image Colorizer"
)


# -------- SUNSET ORANGE BACKGROUND --------

st.markdown("""
<style>

/* Remove scroll */
html, body, [class*="css"]  {
    overflow: hidden;
}


/* Sunset Orange Background */

.stApp {
    background: linear-gradient(
        to top,
        #ff512f 0%,
        #ff7e5f 30%,
        #ff9966 60%,
        #ffd194 100%
    );
}


/* Optional: Remove padding */

.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}

</style>
""", unsafe_allow_html=True)



# -------- PAGE NAVIGATION --------

if "page" not in st.session_state:
    st.session_state.page = "home"



if st.session_state.page == "home":

    show_home()


elif st.session_state.page == "colorizer":

    show_colorizer()

elif st.session_state.page == "outfit":

    show_outfit()