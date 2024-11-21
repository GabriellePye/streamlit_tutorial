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
    background-repeat: repeat; /* This repeats the background image */
    background-size: auto; /* Keeps the original size of the image */
    background-position: top center; /* Ensures the image stays centered at the top */
}
            
/* Container to center the logo */
.logo-container {
    text-align: center;                /* Center align the content */
    margin-bottom: 20px;               /* Add some spacing below the image */
}

/* Logo image styling */
.logo-container img {
    width: 500px;                      /* Adjust the logo width as desired */
    height: auto;                      /* Maintain aspect ratio */
}
 
/* styling for subheader*/
.subheader-container {
    border: 2px solid white;
    background: #f6eee3;  /* Solid background color */
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
    <img src="https://i.ibb.co/s6bhCM8/U-removebg-preview.png" alt="Pawsitivity" style="display: block; margin: 0 auto;">
    <div class='subheader-container'>
        <h2>Bringing you paws-itively fun dog facts, one tail-wag at a time!</h2>
    </div>
</div>
""", unsafe_allow_html=True)