import streamlit as st
import base64


def get_base64(file_path):
    """Safely converts local files to base64 for HTML usage."""
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""


def show_home():
    # 1. Prepare Base64 assets
    video_b64 = get_base64("assets/home.mp4")
    col_img_b64 = get_base64("assets/col.jpeg")
    fit_img_b64 = get_base64("assets/fit.jpg")

    # 2. Optimized CSS
    st.markdown("""
    <style>
    /* Remove default Streamlit lines and extra spacing */
    hr { display: none !important; }
    div[data-testid="stHorizontalBlock"] { border: none !important; }

    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }

    /* VIDEO STYLE - Positioned slightly down */
    .video-hero {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
        margin-top: 25px; /* Nudged down slightly from top */
    }
    .video-hero video {
        width: 900px; 
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
    }

    /* NAVIGATION CONTAINER */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-bottom: 10px;
    }

    /* ✅ SMALLER CARD STYLE */
    .nav-card {
        background: rgba(14, 17, 23, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 10px 20px; /* Reduced padding to save height */
        display: flex;
        align-items: center;
        gap: 15px; 
        transition: 0.3s;
        min-width: 240px; /* Narrower cards */
    }

    .nav-card:hover {
        background: rgba(30, 34, 45, 1);
        border-color: #00d2ff;
        transform: translateY(-3px);
    }

    .icon-box {
        width: 50px; /* Smaller icon */
        height: 50px;
        border-radius: 8px;
        object-fit: cover;
    }

    .card-label {
        color: white;
        font-size: 1.05rem; /* Slightly smaller text */
        font-weight: 600;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Button specific height fix */
    div.stButton > button {
        margin-top: 0px !important;
        padding-top: 5px !important;
        padding-bottom: 5px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # 3. Render Video
    st.markdown(f"""
        <div class="video-hero">
            <video autoplay loop muted playsinline>
                <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            </video>
        </div>
    """, unsafe_allow_html=True)

    # 4. Render Smaller Navigation Cards
    st.markdown(f"""
    <div class="nav-container">
        <div class="nav-card">
            <img src="data:image/jpeg;base64,{col_img_b64}" class="icon-box">
            <span class="card-label">Image Colorizer</span>
        </div>
        <div class="nav-card">
            <img src="data:image/jpeg;base64,{fit_img_b64}" class="icon-box">
            <span class="card-label">Outfit Changer</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 5. Logic Buttons - Compacted to fit screen
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("Use Colorizer", key="nav_col", use_container_width=True):
            st.session_state.page = "colorizer"
            st.rerun()
    with btn_col2:
        if st.button("Use Outfit Changer", key="nav_fit", use_container_width=True):
            st.session_state.page = "outfit"
            st.rerun()


if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    show_home()