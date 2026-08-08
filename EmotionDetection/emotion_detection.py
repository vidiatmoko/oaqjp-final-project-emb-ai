import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Mengubah string JSON dari respon API menjadi kamus (dictionary) Python
    formatted_response = json.loads(response.text)
    
    # Mengambil objek emosi dari struktur respons Watson API
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Mengambil nilai skor masing-masing emosi
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Logika untuk mencari emosi dominan (skor tertinggi)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Mengembalikan format kamus yang diminta
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }