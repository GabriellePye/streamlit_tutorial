# -- Pawsitivity Streamlit App -- #

# -------------------------
# Libraries & Functions
# -------------------------

import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("api_key")

# API endpoint for dog images
dog_img_ep = "https://api.thedogapi.com/v1/images/search"

# Function to fetch a random dog image
def get_dog_img():
    headers = {"x-api-key": api_key}  # Pass the API key in the headers
    response = requests.get(dog_img_ep, headers=headers)
    if response.status_code == 200: 
        # Parse JSON response
        data = response.json()
        return data[0]['url']  # Fetch the correct key for image URL
    else:
        return None  # Return None if the request fails

# -------------------------
# 1. Background CSS
# -------------------------

st.markdown("""
<style>
/* Background */
.stApp {
    background: url('https://e1.pxfuel.com/desktop-wallpaper/693/150/desktop-wallpaper-dog-paw-print-backgrounds-dog-bone-thumbnail.jpg');
    background-repeat: repeat;
    background-size: auto;
    background-position: top center;
}

/* Logo container */
.logo-container {
    text-align: center;
    margin-bottom: 20px;
}
.logo-container img {
    width: 500px;
    height: auto;
}

/* Subheader container */
.subheader-container {
    border: 2px solid white;
    background: #f6eee3;
    padding: 12px;
    border-radius: 15px;
    text-align: center;
    max-width: 100%;
    margin: 0 auto;
    color: #996a56;
}

/* Dog image container */
.dog-img-container {
    border: 2px solid white;
    background: #f6eee3;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    max-width: 80%;
    margin: 20px auto;
    color: #996a56;
}

/* Footer styling */
footer {
    width: 100%;
    background: #f6eee3;
    padding: 10px 0;
    margin-top: 20px;
}

footer p {
    text-align: center;
    color: #996a56;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. Logo and Subheader
# -------------------------

st.markdown("""
<div class='logo-container'>
    <img src="https://i.ibb.co/mc9sCFh/U-removebg-preview.png" alt="Pawsitivity">
    <div class='subheader-container'>
        <h2>🐶 Bringing you paws-itively fun dog images - one tail-wag at a time! 🐶</h2>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# 3. Dog Image Display
# -------------------------

# Persist the displayed image across interactions
if "dog_image" not in st.session_state:
    st.session_state.dog_image = None

if st.button("Get a New Dog Image 🐕"):
    st.session_state.dog_image = get_dog_img()

if st.session_state.dog_image:
    st.markdown("""
        <div class="dog-img-container">
            <h3>🐾 Random Dog Image 🐾</h3>
        </div>
    """, unsafe_allow_html=True)
    st.image(st.session_state.dog_image, use_column_width=True)
else:
    st.write("Click the button to fetch a dog image!")

# -------------------------
# 4. Footer
# -------------------------

st.markdown("""
<footer>
    <p>© 2024 Gabrielle Pye, Rockborne. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)

