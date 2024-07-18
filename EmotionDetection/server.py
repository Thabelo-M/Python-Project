"""
Flask server for Emotion Detection Application.

This module provides a Flask server to analyze emotions from text input.
"""

from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def analyze_emotion():
    """
    Analyzes the emotion from text input provided in the POST request.

    Returns a JSON response with emotion scores and dominant emotion.
    If text input is blank, returns an error message.
    """
    data = request.json
    text_to_analyze = data.get('text', '')

    if not text_to_analyze:
        return jsonify({"error": "Empty input! Please provide text to analyze."}), 400

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)