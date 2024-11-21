#-- Pawsitivity Streamlit App --#

# -------------------------
# Libraries & Functions
# -------------------------

import streamlit as st
import pandas as pd
import numpy as np
import requests
from dotenv import load_dotenv
import os

#-- API --#

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("api_key")

# API endpoint
dog_img_ep = "https://api.thedogapi.com/v1/images/search"

# Function to fetch a random dog fact
def get_dog_img():
    headers = {"x-api-key": api_key}  # Pass the API key in the headers
    response = requests.get(dog_img_ep, headers=headers)
    if response.status_code == 200: 
        # Parse JSON response
        data = response.json()
        return data[0]['url'] # Fetch the image url
    else:
        return "Sorry, couldn't fetch a dog image at the moment."

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
    color: #996a56;  /* Text colour */
}

/* Container for the dog fact display */
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

/* Footer */
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
# 2. Logo, subheader
# -------------------------

st.markdown("""
<div class='logo-container'>
    <img src="https://i.ibb.co/mc9sCFh/U-removebg-preview.png" alt="Pawsitivity" style="display: block; margin: 0 auto;">
    <div class='subheader-container'>
        <h2>🐶 Bringing you paws-itively fun dog images - one tail-wag at a time! 🐶</h2>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# 3. Dog images, widgets, and display
# -------------------------

if st.button("Get a New Dog Image 🐕"): # Create button for interactivity
    img = get_dog_img()
    
    # Custom HTML display for dog image
    st.markdown(f"""
        <div class="dog-img-container">
            <h3>🐾 Random Dog Image 🐾</h3>
            <p>{img}</p>
        </div>
    """, unsafe_allow_html=True)

# ----
# 4.Footer
# ----

st.markdown("""
    <footer>
        <p>© 2024 Gabrielle Pye, Rockborne. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)



