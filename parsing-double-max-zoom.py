import json

def extract_data_google(path):

    with open(path, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    pages_list = json_data["fullTextAnnotation"]["pages"]
    list_of_letters = []
    for a in pages_list:
        for b in a["blocks"]:
            for c in b["paragraphs"]:
                for d in c["words"]:
                    for e in d["symbols"]:
                        if e["confidence"] > 0.28:
                            list_of_letters.append(e["text"])
    return list_of_letters

def extract_data_azure(path):
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
    false_google_chars = 0
    false_human_chars = 0
    for i in range(len(google_arr)):
        if orig_arr[i] != google_arr[i]:
            false_google_chars += 1
        elif orig_arr[i] != human_arr[i]:
            false_human_chars += 1
    print(f"False chars for google: {false_google_chars}\n"
          f"False chars for human: {false_human_chars}")

if __name__ == '__main__':

    max_zoom_google = "files/ocr-google-double-max-zoom.json"
    data_google = extract_data_google(max_zoom_google)

    orig_snellen = "EFPTOZLPEDPECFDEDFCZPFELOPZDDEFPOTECLEFODPCT"
    orig_logmar = "ONVSRKDNROZKCSVDVOHCOHVCKHZCKONCKHDZHCSR"

    human_snellen = "EFPTOZLPEDPECFDEDFCZPFELOPZDDEFPOTEOLEFGDPCT"
    human_logmar = "ONVSRKDNROZKCSVDVOHCOHVCKHZCKONCKMDZHCSR"

    google_snellen = "".join(data_google[:44])
    google_logmar = "".join(data_google[44:])
    print(f"len logmar: {len(google_logmar)}, len snellen: {len(google_snellen)}")
    print("Logmar:")
    analyze_confidece_for_ocr(orig_logmar, google_logmar, human_logmar)
    print("--------------------\n"
          "Snellen:")
    analyze_confidece_for_ocr(orig_snellen, google_snellen, human_snellen)

