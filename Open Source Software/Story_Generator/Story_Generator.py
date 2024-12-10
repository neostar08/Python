import streamlit as st
import torch
from PIL import Image
import openai
from googletrans import Translator
import cv2
import numpy as np

# Configure OpenAI API
openai.api_key = "your_openai_api_key"

# Load YOLOv5 model
@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

model = load_model()

# Google Translator
translator = Translator()

# Function to detect objects
def detect_objects(image):
    results = model(image)
    detections = results.pandas().xyxy[0]
    return detections

# Function to generate a story using GPT
def generate_story(detections):
    objects = list(detections['name'])
    prompt = f"Create a creative story using the following objects: {', '.join(objects)}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

# Function to translate text
def translate_text(text, target_language):
    translated = translator.translate(text, dest=target_language)
    return translated.text
# Streamlit App with Enhanced Design
st.set_page_config(page_title="AI Story Generator", layout="wide")

# Add Enhanced Background
st.markdown(
    """
    <style>
        body {
            background-image: url('https://your-uploaded-image-url.com/updated_ai_background.jpg'); /* Update with your image URL */
            background-size: cover;
            background-attachment: fixed;
            color: #FFFFFF;
            font-family: 'Roboto', sans-serif;
        }
        .main-title {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            color: #00FFDD;
            margin-bottom: 20px;
            text-shadow: 2px 2px 8px rgba(0, 255, 221, 0.7);
        }
        .sub-title {
            font-size: 24px;
            text-align: center;
            color: #FFD700;
            margin-bottom: 40px;
            text-shadow: 1px 1px 6px rgba(255, 215, 0, 0.7);
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 255, 221, 0.4);
            margin-bottom: 20px;
        }
        .button {
            background: linear-gradient(90deg, #00FFDD, #007BFF);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            font-size: 18px;
            text-shadow: 1px 1px 6px rgba(255, 255, 255, 0.7);
        }
        .button:hover {
            background: linear-gradient(90deg, #007BFF, #00FFDD);
            box-shadow: 0px 4px 15px rgba(0, 255, 221, 0.7);
        }
        .sidebar {
            color: #FFFFFF;
        }
    </style>
    """,
    unsafe_allow_html=True
)
