from django.shortcuts import render
import os
import yaml
from azure.storage.blob import ContainerClient
import uuid
from imageHandle.models import imageModel
from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse, HttpResponse

# Create your views here.
def loadConfig():
    dir_root = os.path.dirname(os.path.abspath(__file__))
    with open( dir_root + '/blob_config.yaml', "r") as yamlfile:
        return yaml.load(yamlfile,Loader=yaml.FullLoader)


def upload_blob(name):
    config = loadConfig()
    client = ContainerClient.from_connection_string(config["azure_storage_connectionstring"],config["image_container_name"])

    with open(r"C:\Users\choub\Desktop\imgbt\captionGen\imageHandle\passport_pic.jpg","rb") as data:
        curName = str(uuid.uuid4())
        blob_client = client.get_blob_client(curName+"test.jpeg")
        blob_client.upload_blob(data)
        print(blob_client.url)
        return blob_client.url

def getCaption(img):

    return str(uuid.uuid4())

@csrf_exempt 
def upload(request):
    img = request.FILES.get("image")
    imgUrl = upload_blob(img)
    imgCaption = getCaption(img)
    

    tags = imgCaption.split()
    for tag in tags:
        newEntry = imageModel(
        image = imgUrl,
        tag = tag
        )
        newEntry.save()
        print(imgUrl, tag)
    res = {"result" : "success"}
    return JsonResponse(res)