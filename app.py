import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
from gtts import gTTS

app = Flask(__name__)
CORS(app)

# Load Google Gemini API key
genai.configure(api_key="AIzaSyBR5LsSVZdpiz74v44jXlJplKWnti0mp-4")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_story():
    data = request.json
    prompt = data.get("prompt", "")

    try:
        model = genai.GenerativeModel("gemini-2.0-flash-lite")
        response = model.generate_content(prompt)
        return jsonify({"story": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/text-to-speech", methods=["POST"])
def text_to_speech():
    data = request.json
    text = data.get("text", "").strip()
    voice = data.get("voice", "en")  # Default to English voice

    if not text:
        return jsonify({"error": "Text input is required"}), 400

    try:
        tts = gTTS(text, lang=voice)
        file_path = "static/story.mp3"
        tts.save(file_path)
        return jsonify({"audio_url": "/" + file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
