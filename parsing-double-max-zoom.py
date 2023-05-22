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



if __name__ == '__main__':

    orig_snellen = "EFPT0ZLPEDPECFDEDFCZPFELOPZDDEFPOTECLEFODPCT"

    max_zoom_google = "files/ocr-google-double-max-zoom.json"
    data_google = extract_data_google(max_zoom_google)

    max_zoom_azure = "files/ocr-msAzure-double-max-zoom.json"
    data_azure = extract_data_azure(max_zoom_azure)
    data_azure = "".join(list("".join(data_azure)))

    snellen_google = data_google[:44]
    logmar_google = data_google[44:]

    snellen_azure = data_azure[:44]
    logmar_azure = data_azure[44:]

    print(len(data_google))
    print("".join(snellen_google))
    print("".join(logmar_google))

    print(len(data_azure))
    print("".join(snellen_azure))
    print("".join(logmar_azure))
