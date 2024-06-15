import streamlit as st
from pymongo import MongoClient
import openai
import uuid

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Azure OpenAI API configuration
OPENAI_API_KEY = "your_openai_api_key"
openai.api_key = OPENAI_API_KEY

# Azure Cosmos DB for MongoDB configuration
MONGO_URI = "your_mongo_uri"
DATABASE_NAME = "your_database_name"
COLLECTION_NAME = "your_collection_name"

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]


# Meditation for Re-imagining Traumatic Experiences
st.header("Meditation for Re-imagining Traumatic Experiences")
trauma = st.text_area("Describe your traumatic experience:")
if st.button("Start Meditation"):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Provide a meditation script to help re-imagine the following traumatic experience: {trauma}",
        max_tokens=150
    )
    meditation_script = response.choices[0].text
    st.write(meditation_script)

# Save Data to Cosmos DB
if st.button("Save Data"):
    item = {
        "id": str(uuid.uuid4()),
        "goal": goal,
        "trauma": trauma,
        "visualization": visualization,
        "meditation_script": meditation_script
    }
    collection.insert_one(item)
    st.success("Data saved successfully!")

