import requests
import random
import ast
import os
import openai

import urllib.request
from PIL import Image

from dotenv import load_dotenv

def configure():
    load_dotenv()

def get_prompt(category, topic):
    if(category == 'bucket_list'):
        prompt = "Create a long form Instagram post in the tone of an influencer who just completed the following activity.\n\nActivity: {}".format(topic)
    elif(category == 'history'):
        prompt = "Create a long form Instagram post in the tone of an influencer who witnessed the following event.\n\nEvent: {}".format(topic)
    elif(category == 'hobbies'):
        prompt = "Create a long form Instagram post in the tone of an influencer who is describing what she did today.\n\nTopic: {}".format(topic)
    else:
        print("Incorrect category provided")
        return
    return prompt

def get_caption(prompt):
    openai.api_key = os.getenv('api_key')

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.82,
        max_tokens=3354,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_text = response['choices'][0]['text']
    return response_text

# Image generation
def get_image_url(topic):
    prompt_img = "T. Rex {}, digital art".format(topic)
    openai.api_key = os.getenv('api_key')

    response_img = openai.Image.create(
        prompt=prompt_img,
        n=1,
        size="1024x1024"
    )

    image_url = response_img['data'][0]['url']
    return image_url

# Save image
def save_img(img_url):
    urllib.request.urlretrieve(img_url, "img.jpg")