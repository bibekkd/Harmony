import streamlit as st

st.title("Welcome to Harmony !")
st.write(" ")
st.image("bgimg2.png")

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Define the CSS styles
css = """
<style>
body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f9;
    color: #333;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

.app-description {
    max-width: 1000px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 70px;
    box-shadow: 0 0 100px rgba(0, 0, 0, 0.2);
}

.app-description h2 {
    font-size: 2.5em;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 20px;
}

.app-description p {
    font-size: 1.2em;
    margin-bottom: 20px;
    font-weight: bold;
    text-align: center;
    
}

.app-description ul {
    list-style-type: disc;
    padding-left: 20px;
}

.app-description ul li {
    font-size: 1.1em;
    margin-bottom: 10px;
}

.app-description ul li::marker {
    color: #3498db;
}

.app-description p:last-of-type {
    font-weight: bold;
    text-align: center;
}
</style>
"""

# Define the HTML content
html = """
<div class="app-description">
    <h2>About This App</h2>
    <p>Student Goal Visualization and Meditation App</p>
    <ul>
        <li>Enter your goals and get a visual representation to help you stay motivated and focused.</li>
        <li>Describe your traumatic experiences and receive a personalized meditation script to help you re-imagine and cope with them.</li>
        <li>Securely save your goals and meditation scripts to Azure Cosmos DB for future reference.</li>
    </ul>
    <p>We hope this app helps you achieve your goals and find peace through guided meditation. We hope you find this app useful and easy to use!</p>
</div>
"""

# Render the CSS and HTML in Streamlit
st.markdown(css, unsafe_allow_html=True)
st.markdown(html, unsafe_allow_html=True)

