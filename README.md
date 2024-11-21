# 💻 Streamlit App Tutorial 💻

**Welcome!**
This tutorial is designed for Python enthusiasts who want to dive into building interactive web applications with Streamlit. Whether you're new to Streamlit or looking to explore advanced features like custom CSS styling and API integration, this guide has something for you.

---

## Objective

This tutorial guides you through creating a Streamlit app using custom CSS and HTML coding. We will also integrate API's and explore various Streamlit features to build an interactive and visually appealing application. 

---

## What is Streamlit?

Streamlit is a powerful Python library that simplifies the process of building user-friendly, interactive web applications. It is a widely appreciated for its: 
- **Ease of Use:** Write apps entirely in Python - no need for JavaScript knowledge.
- **Focus on Functionality:** Developers can prioritise features while Streamlit handles component rendering.
- **Versatility:** Perfect for quickly prototyping data dashboards, machine learning apps, and more.

---

## By the End of This Tutorial, You Will: 

- **Set Up and Build Basic Streamlit Apps**
- **Use Markdown and CSS for Customisation**
- **Explore Layout Features**
- **Add Interactivity with Widgets**
- **Combine Python, HTML, and CSS**

---

## Installation Instructions
**Prerequisites:**
- Python 3.7 or above
- VSCode
- GitHub Account
- Streamlit Cloud Account

**To Install Streamlit:**
Open your app.py file and in the terminal on VSCode, type:
```bash
pip install streamlit
```

**Other Dependencies:**
```bash
pip install openai
pip install requests
```


**How to Run the App:**
```bash
streamlit run app.py
```

### What to Expect When Running the App
- The command automatically launches the app in the user's default web browser.
- If it doesn’t open, users can copy and paste the URL from the terminal (e.g., http://localhost:8501) into their browser.

## Project Structure 

├── app.py                  # Main Streamlit app  
├── resources/              # Contains assets like images or logos  
│   ├── logo.png  
│   ├── style.css           # Custom CSS file  
├── README.md               # This file  
├── requirements.txt        # Python dependencies  

### Features Overview 

- **Customizable Themes:** How to style apps with CSS.
- **Interactive Widgets:** Examples of user-input features.
- **API Integration:** Using OpenAI or similar APIs to add functionality.

### Examples 

### FAQ

**1. How do I install Streamlit?**
Use the following command 
```bash
pip install streamlit
```

**2. WHat do I do if the app doesn't open in browser?**
Check terminal output for local URL eg. http://localhost:8501 and paste into your browser 

**3. How do I fix 'ModuleNotFoundError?'**
Ensure all dependencies are installed using 
```bash
pip install -r requirements.txt
```

**4. Can I deploy this app online?** 
Yes, you can! Streamlit apps can be deployed for free using <a href='https://streamlit.io/'>Streamlit Community Cloud</a> 😄

**5. Why do I see a 'Permission Denied' error?**
This often happens when you run Streamlit without the proper permissions. Try:
```bash
sudo streamlit run app.py
```
Or adjust file permissions.

### Credit's & Attributions 

### Links & Other Resources ⭐
