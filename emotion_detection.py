""" 
This module is to determine emotion of text provided by user using 
Watson NLP libraries.
"""
import requests

def emotion_detector(text_to_analyse):
    """ 
    This function is used to determine emotion of user based on text input provided by user.
    Watson NLP libraries are used by this function to determine emotion
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=json)
    return response.text