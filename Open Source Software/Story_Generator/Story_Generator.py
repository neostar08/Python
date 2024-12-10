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
