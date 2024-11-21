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
/* Background */
.stApp {
    background: url('https://e1.pxfuel.com/desktop-wallpaper/693/150/desktop-wallpaper-dog-paw-print-backgrounds-dog-bone-thumbnail.jpg');
    background-repeat: repeat; /* This repeats the background image */
    background-size: auto; /* Keeps the original size of the image */
    background-position: top center; /* Ensures the image stays centred at the top */
}
            
/* Container to center the logo */
.logo-container {
    text-align: center;                /* Centre align the content */
    margin-bottom: 20px;               /* Add some spacing below the image */
}

/* Logo image styling */
.logo-container img {
    width: 500px;                      /* Adjust the logo width */
    height: auto;                      /* Maintain aspect ratio */
}
 
/* Container for subheader display */
.subheader-container {
    border: 2px solid white; /* Thickness and colour of the container border */
    background: #f6eee3;  /* Solid background colour */
    padding: 12px;
    border-radius: 15px;
    text-align: center;
    max-width: 100%;  /* Wider container */
    margin: 0 auto;
    color: #996a56;  /* Text color */
}
            
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. Logo, subheader
# -------------------------

st.markdown("""
<div class='logo-container'>
    <img src="https://i.ibb.co/mc9sCFh/U-removebg-preview.png" alt="Pawsitivity" style="display: block; margin: 0 auto;">
    <div class='subheader-container'>
        <h2>🐶 Bringing you paws-itively fun dog facts - one tail-wag at a time! 🐶</h2>
    </div>
</div>
""", unsafe_allow_html=True)