import requests
import json

def emotion_detector(text_to_analyse):
    # Check if the text is empty or just whitespace
    if not text_to_analyse.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # API call to Watson for emotion prediction
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json=myobj, headers=header)  # Send a POST request to the API with the text and headers

    formatted_response = json.loads(response.text)

    # Ensure emotionPredictions is a list and extract the first element
    emotion_predictions = formatted_response.get('emotionPredictions', [])
    if not emotion_predictions:
        return {"error": "No emotion predictions found"}

    emotions = emotion_predictions[0].get('emotion', {})  # Access the first element and its 'emotion' key
    if not emotions:
        return {"error": "No emotion data available"}

    # Extract individual emotions
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)

    # Find dominant emotion
    dominant_emotion_name = max(emotions, key=emotions.get, default="None")
    dominant_emotion = emotions.get(dominant_emotion_name, 0)

    # Return dictionary with emotion scores and dominant emotion
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion_name,
        'dominant_emotion_score': dominant_emotion
    }
