# Importing necessary libraries
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using an external API and returns
    a dictionary of emotion scores including the dominant emotion.
    
    Args:
        text_to_analyze (str): The input text for emotion detection.

    Returns:
        dict: A dictionary with emotion scores and the dominant emotion.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 400:
            # Blank input or bad request
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
        response.raise_for_status()
        response_data = response.json()
        emotions = response_data["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
        emotions["dominant_emotion"] = dominant_emotion
        return emotions
    except (requests.RequestException, KeyError, IndexError, json.JSONDecodeError) as error:
        return {"error": str(error)}









    # anger_score = new_response["emotionPredictions"]["emotion"]["anger"]
    # disgust_score = new_response["emotionPredictions"]["emotion"]["disgust"]
    # fear_score = new_response["emotionPredictions"]["emotion"]["fear"]
    # joy_score = new_response["emotionPredictions"]["emotion"]["joy"]
    # sadness_score = new_response["emotionPredictions"]["emotion"]["sadness"]


    # match (max(anger_score,disgust_score,fear_score,joy_score,sadness_score)):
    #     case anger_score:
    #         dominant_emotion = "anger"
    #     case disgust_score:
    #         dominant_emotion = "disgust"
    #     case fear_score:
    #         dominant_emotion = "fear"
    #     case joy_score:
    #         dominant_emotion = "joy"
    #     case sadness_score:
    #         dominant_emotion = "sadness"
    