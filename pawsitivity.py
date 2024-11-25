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
dog_api_key = os.getenv("dog_api_key")
# cat_api_key = os.getenv("cat_api_key")

# API endpoint for dog images
dog_img_ep = "https://api.thedogapi.com/v1/images/search"
# cat_img_ep = "https://api.thecatapi.com/v1/images/search"

# Function to fetch a random dog image
def get_dog_img():
    headers = {"x-api-key": dog_api_key}  # Pass the API key in the headers
    response = requests.get(dog_img_ep, headers=headers)
    if response.status_code == 200: 
        # Parse JSON response and return the image URL
        data = response.json()
        return data[0]['url']
    else:
        return None  # Return None if the request fails
    
# Function to fetch a random cat image
# def get_cat_img():
    # headers = {"x-api-key": cat_api_key}  # Pass the API key in the headers
    # response = requests.get(cat_img_ep, headers=headers)
    # if response.status_code == 200: 
        # Parse JSON response and return the image URL
      #  data = response.json()
      #  return data[0]['url']
    # else:
        # return None  # Return None if the request fails

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

/* Dog Image Display Container */
.dog-img-container {
    border: 2px solid white;
    background: #f6eee3;
    padding: 12px;
    border-radius: 15px;
    text-align: center;
    max-width: 100%;
    margin: 20px auto;
    color: #996a56;
}

/* Empty State Message Container */
.empty-state-container {
    border: 2px solid white;
    background: #f6eee3;
    padding: 12px;
    border-radius: 15px;
    text-align: center;
    max-width: 100%;
    margin: 20px auto;
    color: #996a56;
}

/* Footer styling */
footer {
    width: 100%;
    background: #f6eee3;
    border: 2px solid white; /* Match other container borders */
    border-radius: 15px; /* Rounded corners */
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
        <h2>🐶 Bringing you paws-itively fun animal images - one tail-wag at a time! 🐶</h2>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# 3. Layout with Columns and Button
# -------------------------

# Create columns to center the button
col1, col2, col3 = st.columns(3)

# Place the button in the middle column (col2)#

with col1:
    pass
with col2:
    dog_button = st.button('Get a New Dog Image 🐕')  # Center the button
with col3:
    pass
   # center_button = st.button('Get a New Cat Image 🐈')  # Center the button

# -------------------------
# 4. Dog Image Display Logic
# -------------------------

# Persist the displayed image across interactions
if "dog_image" not in st.session_state:
    st.session_state.dog_image = None

# Fetch a new dog image when the button is clicked
if dog_button:
    st.session_state.dog_image = get_dog_img()

# -------------------------
# 5. Display Dog Image or Empty State
# -------------------------

# Check if a dog image has been fetched, else show the empty state message
if st.session_state.dog_image:
    # Show the dog image in a container
    st.markdown("""
        <div class="dog-img-container">
            <h3>🐾 Random Dog Image 🐾</h3>
        </div>
    """, unsafe_allow_html=True)
    st.image(st.session_state.dog_image, use_column_width=True)
else:
    # Show the empty state message when no image is fetched
    st.markdown("""
        <div class="empty-state-container">
            <h3>🐾 Welcome to Pawsitivity! 🐾</h3>
            <p>Click the button above to fetch your first animal image!</p>
        </div>
    """, unsafe_allow_html=True)

# -------------------------
# 6. Footer
# -------------------------

st.markdown("""
<footer>
    <p>© 2024 Gabrielle Pye, Rockborne. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)
