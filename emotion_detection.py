# Importing necessary libraries
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using an external API.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    json_obj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=json_obj, headers=headers)

    return response.text





