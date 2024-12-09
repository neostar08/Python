# 🌟 AI-Powered Story Generator

Welcome to the **AI-Powered Story Generator** repository! This project showcases the combination of advanced AI technologies, natural language processing, and object detection to create engaging, personalized stories based on input images. Built with a professional, user-friendly design, it offers a fun and creative way to experience the potential of AI.

---

## ✨ Features

- **🔍 Object Detection**: Uses **YOLOv5** for high-accuracy object detection in uploaded images. Automatically identifies objects and lists them with confidence scores.
- **✍️ Story Generation**: Leverages **OpenAI's GPT** to create engaging and imaginative stories based on detected objects.
- **🌍 Multi-Language Translation**: Integrates **Google Translate** to support languages like English, Spanish, French, German, Chinese, Korean, and Hindi.
- **🎨 Anime-Inspired Design**: Aesthetic UI with vibrant, anime-style visuals and a magical storytelling atmosphere. Fully responsive for desktop and mobile screens.

---

## 🛠️ Technology Stack

| **Category**   | **Technology**                 |
|----------------|--------------------------------|
| **Backend**    | Flask, PyTorch, OpenAI GPT     |
| **Frontend**   | Bootstrap 5, Custom CSS       |
| **Translation**| Googletrans                   |

---

## 🚀 Installation

### Prerequisites
- Python 3.9 or above.
- A valid OpenAI API key. Get one [here](https://platform.openai.com/account/api-keys).

### Install Dependencies
```bash
pip install flask flask-bootstrap torch torchvision pillow openai googletrans==4.0.0-rc1 opencv-python
```

### Clone the Repository
```bash
git clone https://github.com/neostar08/AI-Story-Generator.git
cd AI-Story-Generator
```

### Project Structure
```
AI-Story-Generator/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   └── index.html         # Main user interface
├── static/                # Static files (CSS, images)
│   └── background.webp    # Background image
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

### Run the Application
1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
http://127.0.0.1:5000```  

---

## 📖 Usage

1. **Upload an Image**: Drag and drop an image or select one using the upload button.
2. **Choose Language**: Select your preferred language for the generated story.
3. **Generate Story**: Click the "Generate Story" button to see the magic of AI.
4. **View Results**: Explore the generated story and optionally translate it.

---

## 🤝 Contributing

We welcome contributions! To get started:

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

## 📬 Contact

- **GitHub**: [neostar08](https://github.com/neostar08)
- **Email**: [sher.4.95@mail.ru](mailto:sher.4.95@mail.ru)

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📅 Future Roadmap

- [ ] Add video tutorials for better onboarding.
- [ ] Integrate additional object detection models.
- [ ] Expand multi-language support with audio output.
- [ ] Transition to a Progressive Web App (PWA) for offline usage.

---

Thank you for exploring the **AI-Powered Story Generator**! We hope you enjoy the magic of storytelling with AI. 🌟
