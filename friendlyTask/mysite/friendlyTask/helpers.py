import requests
import json
from pathlib import Path
import urllib.request
import cloudscraper
from PIL import Image
from os.path import abspath, dirname, join
import os
from colorthief import ColorThief

def get_dict_from_api(body):
    URL = "https://jsonplaceholder.typicode.com/photos"
    PARAMS = {'albumId': body['albumId'], 'title': body['title']}
    r = requests.get(url = URL, params = PARAMS)
    if len(r.json()) > 0:
        return r.json()[0]

def photo_to_file(photoId, json_response):
    scraper = cloudscraper.create_scraper(browser={
        'browser': 'firefox',
        'platform': 'windows',
        'desktop': True
    })
    img_data = scraper.get(json_response['url']).content
    path = create_photo_path(photoId)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as handler:
        handler.write(img_data)

def create_photo_path(photoId):
    filename = str(photoId) + '.jpg'
    photo_path = join('friendlyTask/static/photos/', filename)
    absolute_path = abspath(photo_path)
    return absolute_path

def set_photo_attributes(photo):
    path = create_photo_path(photo.id)
    img = Image.open(path)
    photo.width = img.width
    photo.height = img.height
    photo.url = path
    photo.color = get_dominant_color(path)

def get_dominant_color(img_path):
    color_thief = ColorThief(img_path)
    dominant_color = color_thief.get_color(quality=1)
    color_hex = '#%02x%02x%02x' % dominant_color
    return color_hex

def find_dict_in_file(file, body):
    list_of_dictionaries = json.loads(file.read())
    for photo_dict in list_of_dictionaries:
        if (photo_dict['albumId'] == body['albumId']) and (photo_dict['title'] == body['title']):
            return photo_dict
