import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check if text_to_analyze is blank or contains only whitespace
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
        response_json = response.json()
        if 'emotionPredictions' in response_json:
            emotion_predictions = response_json['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
            return {
                "anger": emotion_predictions.get('anger'),
                "disgust": emotion_predictions.get('disgust'),
                "fear": emotion_predictions.get('fear'),
                "joy": emotion_predictions.get('joy'),
                "sadness": emotion_predictions.get('sadness'),
                "dominant_emotion": dominant_emotion
            }
        else:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    else:
        response.raise_for_status()