from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .models import Photo
from .serializers import PhotoSerializer
import requests
import urllib.request
from PIL import Image
from os.path import abspath, dirname, join
import os
from colorthief import ColorThief
from friendlyTask.helpers import get_dict_from_api, photo_to_file, set_photo_attributes, get_dominant_color, find_dict_in_file


@api_view(['GET'])
def getData(request):
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPhoto(request):
    body = request.data
    photo_dict = get_dict_from_api(body)

    serializer = PhotoSerializer(data=photo_dict) 
    if serializer.is_valid():
        if Photo.objects.filter(albumId=body['albumId'], title=body['title']).exists():
            return Response("This photo already exists.")
        serializer.save()
    else:
        return Response('invalid serializer', status=status.HTTP_400_BAD_REQUEST)

    photo = Photo.objects.get(albumId=body['albumId'], title=body['title'])
    photo_to_file(photo.id, photo_dict)
    set_photo_attributes(photo)
    photo.save()
    return Response(PhotoSerializer(photo).data)

@api_view(['PUT'])
def updatePhoto(request, id):
    if Photo.objects.filter(id=id).exists():
        body = request.data
        photo = Photo.objects.get(id=id)
        photo.update(body['title'], body['albumId'])
        photo.save()
        serializer = PhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
        content = {"This photo doesn't exist"}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deletePhoto(request, id):
    if Photo.objects.filter(id=id).exists():
        Photo.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        content = "This photo doesn't exist"
        return Response(content, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addPhotoFromFile(request):
    body = request.data
    try:
        with open("friendlyTask/static/json/photos.json", "r") as file:
            photo_dict = find_dict_in_file(file, body)
            if photo_dict:
                serializer = PhotoSerializer(data=photo_dict)
                if serializer.is_valid():
                    if Photo.objects.filter(albumId=body['albumId'], title=body['title']).exists():
                        return Response("This photo already exists.")
                    serializer.save()
                else:
                    return Response('Invalid serializer', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("This photo doesn't exist", status=status.HTTP_400_BAD_REQUEST)
    except EnvironmentError:
        return Response('You must first import the json file to use this route', status=status.HTTP_400_BAD_REQUEST)

    photo = Photo.objects.get(albumId=body['albumId'], title=body['title'])
    photo_to_file(photo.id, photo_dict)
    set_photo_attributes(photo)
    photo.save()
    return Response(PhotoSerializer(photo).data)

