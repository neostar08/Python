from flask import Flask, render_template, request
import torch
from PIL import Image
import numpy as np
from transformers import pipeline
from googletrans import Translator

app = Flask(__name__)

# Initialize Translator
translator = Translator()

# Load YOLOv5 model
def load_yolo_model():
    print("Loading YOLO model...")
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

model = load_yolo_model()

# Class names for YOLOv5
CLASSES = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
    'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
    'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
    'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
    'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
    'hair drier', 'toothbrush'
]

# Detect objects in an image
def detect_objects(image):
    try:
        print("Detecting objects...")
        results = model(image)
        detections = results.pandas().xyxy[0]

        filtered_objects = [
            CLASSES[int(row['class'])]
            for _, row in detections.iterrows()
            if row['confidence'] > 0.5
        ]
        print(f"Filtered Objects: {filtered_objects}")  # Debugging
        return filtered_objects
    except Exception as e:
        print(f"Error in object detection: {e}")
        return []

# Generate a story using Hugging Face
def generate_story(objects):
    try:
        objects = list(set(objects))  # Ensure unique objects
        if not objects:
            return (
                "Once upon a time, a curious animal ventured into a magical forest. "
                "The forest was full of mysteries and challenges. "
                "What adventures awaited this brave creature?"
            )

        # Dynamic prompt based on detected objects
        if len(objects) == 1:
            prompt = (
                f"Once upon a time, there was a {objects[0]} in a magical world. "
                f"Write a creative story about its adventures, challenges, and discoveries."
            )
        else:
            prompt = (
                f"Once upon a time, there was a {', '.join(objects[:-1])}, and a {objects[-1]}. "
                f"Describe their exciting journey and how they overcame challenges together."
            )

        print(f"Prompt: {prompt}")  # Debugging
        generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
        story = generator(prompt, max_length=600, num_return_sequences=1)
        return story[0]['generated_text']
    except Exception as e:
        print(f"Error in story generation: {e}")
        return "An error occurred while generating the story."

# Translate story into the requested language
def translate_text(text, target_language):
    if not target_language or target_language.lower() == "en":
        return text  # No translation needed for English
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return "Translation failed. Please try again."

@app.route("/", methods=["GET", "POST"])
def home():
    story = None
    translated_story = None
    detections = None

    if request.method == "POST":
        # Reset data for the new request
        story = None
        translated_story = None
        detections = None

        file = request.files.get("file")
        target_language = request.form.get("language", "en").strip()

        if file:
            try:
                # Convert uploaded file to NumPy array for YOLO
                image = Image.open(file.stream).convert('RGB')
                image_array = np.array(image)

                # Detect objects and log results
                detections = detect_objects(image_array)
                print(f"Final Detected Objects: {detections}")

                # Generate a story and log prompt
                story = generate_story(detections)
                print(f"Generated Story: {story}")

                # Translate the story if a target language is provided
                if target_language:
                    translated_story = translate_text(story, target_language)
                    print(f"Translated Story: {translated_story}")
            except Exception as e:
                story = f"An error occurred: {str(e)}"

    return render_template("index.html", story=story, translated_story=translated_story, detections=detections)

if __name__ == "__main__":
    app.run(debug=True)
