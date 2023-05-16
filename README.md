# Google Cloud Vision API and Azure Vision Studio text recognition through API

The goal of this assignment is to familiarize students with Application Programming Interface of different services, teach how to handle responses and parse data structures using Python programming language and json library.

## Part 1
Parse `ocr-google.json` that contains the result of OCR the file `double-max-zoom.jpg` processed by Google Vision AI service. and extract the data in the following format:
```python
content = {"symbol": confidence}
```
where `content` is a dictionary consisting of the recognized symbols and their confidence values.

## Part 2
Using Snellen chart and LogMAR chart from folder `files` define a confidence value that will give the most optimal result of OCR and justify your decision. What criteria you used for value estimation? How did you calculate it?

## Part 3
Create an Microsoft Azure account with free credit[^1] and use [Cognitive Services OCR](https://portal.vision.cognitive.azure.com/gallery/ocr) to recognize the symbols on the label in `compressed-gas.jpg' file.
Create a Google Cloud account[^2] with free credit and use [Google Vision AI](https://cloud.google.com/vision/)

Microsoft Computer Vision API documentation is available [here](https://centraluseuap.dev.cognitive.microsoft.com/docs/services/unified-vision-apis-public-preview-2023-02-01-preview/operations/61d65934cd35050c20f73ab6)

## Part 4
Compare the results of Google and Microsoft optical character recognition and compare them, explaining the comparison criteria and their relevance.

[^1]: You can apply for a [free student account](https://azure.microsoft.com/en-us/free/students/), but I am not sure it gives access to Cognitive Services
[^2]: You can apply for a [free education account](https://edu.google.com/programs/benefits/students/), but I am not sure it gives access to Vision AI

