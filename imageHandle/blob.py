import os
import yaml
from azure.storage.blob import ContainerClient
import uuid

from PIL import Image

def loadConfig():
    dir_root = os.path.dirname(os.path.abspath(__file__))
    with open( dir_root + '/blob_config.yaml', "r") as yamlfile:
        return yaml.load(yamlfile,Loader=yaml.FullLoader)

config = loadConfig()
print(config)
client = ContainerClient.from_connection_string(config["azure_storage_connectionstring"],config["image_container_name"])

with open(r"C:\Users\choub\Desktop\imgbt\captionGen\imageHandle\passport_pic.jpg","rb") as data:
    curName = str(uuid.uuid4())
    blob_client = client.get_blob_client(curName+"test.jpeg")
    blob_client.upload_blob(data)
    print(blob_client.url)
    