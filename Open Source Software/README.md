# 🌟 AI-Powered Story Generator

Welcome to the **AI-Powered Story Generator** repository! This project combines advanced AI technologies, natural language processing, and object detection to create engaging, personalized stories based on input images. Built with a professional, user-friendly design, it offers a fun and creative way to experience the potential of AI.

---

## ✨ Features

- **🔍 Object Detection**: Uses **YOLOv5** for high-accuracy object detection in uploaded images. Automatically identifies objects and lists them with confidence scores.
- **✍️ Story Generation**: Leverages a **fine-tuned GPT model** to create engaging and imaginative stories based on detected objects.
- **🌍 Multi-Language Translation**: Translates stories into multiple languages, including English, Spanish, French, German, Chinese, Korean, and Hindi.
- **🎨 Anime-Inspired Design**: A vibrant UI with anime-style visuals and a magical storytelling atmosphere.
- **⚡ Optimized Performance**: Supports GPU acceleration for faster processing.
- **💾 Pre-Trained Model Ready**: Fine-tuned model included for seamless use without additional training.

---

## 🛠️ Technology Stack

| **Category**      | **Technology**                 |
|-------------------|--------------------------------|
| **Backend**       | Flask, PyTorch, Transformers  |
| **Frontend**      | HTML, CSS, Anime-Inspired UI  |
| **Object Detection** | YOLOv5, OpenCV               |
| **Language Model**| Fine-Tuned GPT (e.g., GPT-2)  |
| **Translation**   | Googletrans                   |

---

## 🚀 Installation

### Prerequisites

- Python 3.9 or above.
- A valid OpenAI API key or use the provided fine-tuned GPT model.

### Clone the Repository
```bash
git clone https://github.com/neostar08/AI-Story-Generator.git
cd AI-Story-Generator
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📖 Usage

### Run the Application
1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

### Application Workflow
1. **Upload an Image**:
   - Drag and drop an image or select one using the upload button.
2. **Generate Story**:
   - The app detects objects in the image and generates a creative story based on them.
3. **Translate the Story**:
   - Choose your preferred language for translation from the sidebar.
4. **Save or Share**:
   - Copy the story or take a screenshot for sharing.

---

## 📂 Project Structure

```
AI-Story-Generator/
├── app.py                 # Main Flask application
├── train_model.py         # Fine-tuning script for the language model
├── templates/             # HTML templates
│   └── index.html         # Main user interface
├── static/                # Static files (CSS, images)
│   ├── styles.css         # Custom CSS for the UI
│   └── background.webp    # Background image
├── fine_tuned_model/      # Directory containing fine-tuned model files
├── requirements.txt       # Python dependencies
├── LICENSE                # License file
└── README.md              # Project documentation
```

---

## 🤝 Contributing

We welcome contributions! Here’s how you can get started:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push your changes:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

---

## 📌 License

This project is licensed under the **MIT License**. To use the code, you need to follow the terms outlined in the [LICENSE](LICENSE) file.

---

## 🗓 Future Roadmap

- [ ] Add video tutorials for better onboarding.
- [ ] Integrate additional object detection models.
- [ ] Expand multi-language support with audio output.
- [ ] Deploy as a Progressive Web App (PWA) for offline usage.
- [ ] Improve model fine-tuning with diverse datasets.

---

Thank you for exploring the **AI-Powered Story Generator**! We hope you enjoy the magic of storytelling with AI. 🌟

