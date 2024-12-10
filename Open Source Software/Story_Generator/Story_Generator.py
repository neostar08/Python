from flask import Flask, render_template, request
import torch
from PIL import Image
import openai
import cv2
import numpy as np
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Configure OpenAI API
openai.api_key = "your_openai_api_key"

# Load YOLOv5 model
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

model = load_model()

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

@app.route("/", methods=["GET", "POST"])
def home():
    story = None
    translated_story = None
    detections = None
    if request.method == "POST":
        # Get uploaded file
        file = request.files["file"]
        if file:
            image = Image.open(file.stream)
            image_array = np.array(image)

            # Detect objects
            detections = detect_objects(image_array)

            # Generate a story
            if not detections.empty:
                story = generate_story(detections)

                # Translate the story
                target_language = request.form.get("language")
                translated_story = translate_text(story, target_language)

    return render_template("index.html", story=story, translated_story=translated_story, detections=detections)

if __name__ == "__main__":
    app.run(debug=True)
