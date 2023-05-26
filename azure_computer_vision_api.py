import json
import http.client, urllib.request, urllib.parse, urllib.error, base64

credentials = json.load(open("files/credentials.json"))
VISION_KEY = credentials["VISION_KEY"]
ENDPOINT = credentials["VISION_ENDPOINT"]

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': VISION_KEY,
}

params = urllib.parse.urlencode({
    # Request parameters
    'features': 'read',
    'gender-neutral-caption': 'False',
})

body = json.dumps({"url": "https://raw.githubusercontent.com/ICA0011/optical-character-recognition-with-api-RSylla/"
                          "1fc0d920696fd8212ac93b686ae76eef61d9eb5c/files/compressed-gas.jpg"})

try:
    conn = http.client.HTTPSConnection(ENDPOINT)
    conn.request("POST", f"/computervision/imageanalysis:analyze?api-version=2023-02-01-preview&{params}",
                 body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
