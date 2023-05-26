import os
import json
# Imports the Google Cloud client library
from google.cloud import vision



def run_quickstart():

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath("files/compressed-gas.jpg")

    # Loads the image into memory
    with open(file_name, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    text = json.loads(type(response).to_json(response))
    # text = MessageToJson(data)
    print(text["textAnnotations"][0]["description"])


if __name__ == "__main__":
    run_quickstart()
