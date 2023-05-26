import os
import json
# Imports the Google Cloud client library
from google.cloud import vision
from google.protobuf.json_format import MessageToDict



def run_quickstart() -> vision.EntityAnnotation:
    """Provides a quick start example for Cloud Vision."""

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
    # data = response.text_annotations
    # text = json.loads(MessageToJson(data))

    response = MessageToDict(response, preserving_proto_field_name = True)
    desired_res = response["label_annotation"]
    print(desired_res)
    # for k in text:
    #     print(k)


if __name__ == "__main__":
    run_quickstart()
