########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'be1d5d7f8b8b4829b2ca539998f5cfb5',
}

params = urllib.parse.urlencode({
    # Request parameters
    'language': 'en',
    'gender-neutral-caption': 'False',
})

try:
    conn = http.client.HTTPSConnection('*.cognitiveservices.azure.com')
    conn.request("POST", "/computervision/imageanalysis:analyze?api-version=2023-02-01-preview&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################


# from azure.cognitiveservices.vision.computervision import ComputerVisionClient
# from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
# from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
# from msrest.authentication import CognitiveServicesCredentials
#
# from array import array
# import os
# from PIL import Image
# import sys
# import time
#
# '''
# Authenticate
# Authenticates your credentials and creates a client.
# '''
# subscription_key = os.environ["VISION_KEY"]
# endpoint = os.environ["VISION_ENDPOINT"]
# # print(subscription_key)
# # print(endpoint)
#
# computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
# '''
# END - Authenticate
# '''
#
# '''
# OCR: Read File using the Read API, extract text - remote
# This example will extract text in an image, then print results, line by line.
# This API call can also extract handwriting style text (not shown).
# '''
# print("===== Read File - remote =====")
# # Get an image with text
# read_image_url = "files/ocr-google-compressed-gas.json"
#
# # Call API with URL and raw response (allows you to get the operation location)
# read_response = computervision_client.read(read_image_url,  raw=True, model_version="2022-04-30")
#
# read_operation_location = read_response.headers["Operation-Location"]
# # Grab the ID from the URL
# operation_id = read_operation_location.split("/")[-1]
#
# # Call the "GET" API and wait for it to retrieve the results
# while True:
#     read_result = computervision_client.get_read_result(operation_id)
#     if read_result.status not in ['notStarted', 'running']:
#         break
#     time.sleep(1)
#
# # Print the detected text, line by line
# if read_result.status == OperationStatusCodes.succeeded:
#     for text_result in read_result.analyze_result.read_results:
#         for line in text_result.lines:
#             print(line.text)
#             print(line.bounding_box)
# print()
# '''
# END - Read File - remote
# '''
#
# print("End of Computer Vision quickstart.")