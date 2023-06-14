import requests
import random
import ast
import os
import openai

from dotenv import load_dotenv

def get_category():
    return random.choice(['bucket_list', 'history', 'hobbies'])

def get_topic(category):
    if(category == 'bucket_list'):
        return get_bucket_list_topic()
    elif(category == 'history'):
        return get_historical_event_topic('snow')
    elif(category == 'hobbies'):
        return get_hobbies_topic()
    else:
        print("Incorrect category provided")
        return

# Bucket List API
def get_bucket_list_topic():
    api_url = 'https://api.api-ninjas.com/v1/bucketlist'
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv('ninja_api_key')})
    if response.status_code == requests.codes['ok']:
        return ast.literal_eval(response.text)["item"]
    else:
        print("Error:", response.status_code, response.text)

# Historical Events API
def get_historical_event_topic(text):
    api_url = 'https://api.api-ninjas.com/v1/historicalevents?text={}'.format(text)
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv('ninja_api_key')})
    if response.status_code == requests.codes['ok']:
        event = random.choice(ast.literal_eval(response.text))
        # date = event['day'] + '/' + event['month'] + '/' + event['year']
        return event['event']
    else:
        print("Error:", response.status_code, response.text)

# Hobbies API
def get_hobbies_topic():
    categories = ['general', 'sports_and_outdoors', 'collection', 'competition', 'observation']
    category = random.choice(categories)
    api_url = 'https://api.api-ninjas.com/v1/hobbies?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv('ninja_api_key')})
    if response.status_code == requests.codes['ok']:
        return ast.literal_eval(response.text)["hobby"]
    else:
        print("Error:", response.status_code, response.text)