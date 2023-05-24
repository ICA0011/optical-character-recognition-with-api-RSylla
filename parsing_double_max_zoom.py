import json

def extract_data_google(path):
    """Extract confidence and text data from json,
    return it as dictionary"""
    with open(path, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    pages_list = json_data["fullTextAnnotation"]["pages"]
    dicty = {"snellen": [],
             "logmar": []}
    for a in pages_list:
        block = 1
        for b in a["blocks"]:
            for c in b["paragraphs"]:
                for d in c["words"]:
                    for e in d["symbols"]:
                        if e["confidence"] > 0.1:
                            if block == 1:
                                dicty["snellen"].append({"text": e["text"],
                                               "confidence": e["confidence"]})
                            else:
                                dicty["logmar"].append({"text": e["text"],
                                               "confidence": e["confidence"]})
            block += 1
    return dicty

def extract_data_azure(path):
    """Extract confidence and text data from json,
    return it as list"""
    with open(path, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    lines = json_data[0]["lines"]
    list_of_letters = []
    for a in lines:
        for b in a["words"]:
            if b["confidence"] > 0.1:
                list_of_letters.append(b["text"])
    return list_of_letters

def analyze_confidece_for_ocr(orig_arr, google_arr, human_arr):
    """Compare the results char by char with original array of characters.
    In comparison we use original array (logmar, snellen), google vision AI
    composed array of same characters from an image and same array read by
    human from same image. Image was medimum to poor quality and a bit blurry.
    Counters count for any false letters on current position on either side.
    """
    false_google_chars = 0
    false_human_chars = 0

    for i in range(len(google_arr)):
        if google_arr[i]["confidence"] < 0.49 and orig_arr[i] != google_arr[i]["text"]:
            false_google_chars += 1
        if orig_arr[i] != human_arr[i]:
            false_human_chars += 1

    print(f"False chars for google: {false_google_chars}\n"
          f"False chars for human: {false_human_chars}")

if __name__ == '__main__':

    max_zoom_google = "files/ocr-google-double-max-zoom.json"
    google_snellen = extract_data_google(max_zoom_google)["snellen"]
    google_logmar = extract_data_google(max_zoom_google)["logmar"]

    orig_snellen = "EFPTOZLPEDPECFDEDFCZPFELOPZDDEFPOTECLEFODPCT"
    orig_logmar = "ONVSRKDNROZKCSVDVOHCOHVCKHZCKONCKHDZHCSR"

    human_snellen = "EFPTOZLPEDPECFDEDFCZPFELOPZDDEFPOTEOLEFGDPCT"
    human_logmar = "ONVSRKDNROZKCSVDVOHCOHVCKHZCKONCKMDZHCSR"

    print("As for confidence of Google vision AI,\nwe should consider it to be "
          "49% or greater.\nAt this percentile average error size is about the same as for humans.")
    print("Logmar:")
    analyze_confidece_for_ocr(orig_logmar, google_logmar, human_logmar)
    print("--------------------\nSnellen:")

    analyze_confidece_for_ocr(orig_snellen, google_snellen, human_snellen)

