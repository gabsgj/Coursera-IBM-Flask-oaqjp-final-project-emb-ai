"""
Flask web application for detecting emotions from text using an external API.

Routes:
- / : Renders the index HTML page.
- /emotionDetector : Returns the detected emotions and dominant emotion for a given text input.
"""

# import necessary packages
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_deployment():
    """
    API endpoint that returns emotion detection results for a given text.
    Expects a GET parameter 'textToAnalyze'.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    function_response = emotion_detector(text_to_analyze)

    if "error" in function_response:
        return f"Error: {function_response['error']}", 500

    # Handle None emotion case (blank input or bad request)
    if function_response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {function_response['anger']}, "
        f"'disgust': {function_response['disgust']}, "
        f"'fear': {function_response['fear']}, "
        f"'joy': {function_response['joy']} and "
        f"'sadness': {function_response['sadness']}. "
        f"The dominant emotion is {function_response['dominant_emotion']}."
    )

    return response_text

@app.route("/")
def render_index_page():
    """
    Renders the main index page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
