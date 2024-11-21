#-- Pawsitivity Streamlit App --#

# -------------------------
# Libraries & Functions
# -------------------------

import streamlit as st
import pandas as pd
import numpy as np

# API 

# -------------------------
# 1. Background CSS
# -------------------------

st.markdown("""
<style>
/* background */
.stApp {
    background: url('https://i.ibb.co/2kgHSWf/Screenshot-21-11-2024-113536-www-pinterest-com.jpg');
    background-size: cover; 
    background-position: top;
}
            
/* Container to center the image */
.logo-container {
    text-align: center;                /* Center align the content */
    margin-bottom: 20px;               /* Add some spacing below the image */
}

/* Logo image styling */
.logo-container img {
    width: 400px;                      /* Adjust the logo width as desired */
    height: auto;                      /* Maintain aspect ratio */
}
 
/* styling for subheader + other text elements */
.subheader-container {
    border: 2px solid white;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    max-width: 80%;  /* Adjusted for centering */
    margin: 0 auto;
}
            
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. Logo
# -------------------------

st.markdown("""
<div class='logo-container'>
    <img src="https://i.ibb.co/DMz3K4H/U.png" alt="Pawsitivity" style="display: block; margin: 0 auto;">
    <div class='subheader-container'>
        <h2>Bringing you paws-itively fun dog facts, one tail-wag at a time!</h2>
    </div>
</div>
""", unsafe_allow_html=True)