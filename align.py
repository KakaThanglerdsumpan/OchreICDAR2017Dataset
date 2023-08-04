import json

#======================to change before use===============================
rawDatasetDir = r"ICDAR2017_datasetPostOCR_v1.2/ICDAR2017_datasetPostOCR_Evaluation_2M_v1.2/eng_monograph/" # path to the raw dataset to preprocess
numOfFiles = 81 #number of files in dataset

alignDir = r"datasets/train/aligned/" #dir where you will be saving the output of aligned character json fiiles
#====================end of to change before use==========================

def string_to_char_list_in_json(input_string):
    char_list = list(input_string)
    json_data = json.dumps(char_list)
    return json_data

for i in range(1, numOfFiles+1):
    num = str(i + 666)
    fRawPath = rawDatasetDir + str(i) + ".txt"
    fRaw = open(fRawPath, "r")

    fRaw.readline() # ignored line (ocr_aligned)
    ocr = fRaw.readline() 
    gs = fRaw.readline()

    gsJson = string_to_char_list_in_json(gs[14:])

    ocrJson =string_to_char_list_in_json(ocr[14:])

    gsJson = gsJson.replace("@", "")
    gsJson = gsJson.replace("#", "")

    ocrJson = ocrJson.replace("@", "")
    ocrJson = ocrJson.replace("#", "")

    jsonString = ('{\n\t"ocr": ' +
        ocrJson + 
        ',\n\t"gs": ' + 
        gsJson +
        "\n}")
    fAlignName = alignDir + num + ".json"
    with open(fAlignName, "w") as outfile:
        outfile.write(jsonString)

    print(f"Aligned file saved to {fAlignName}")
    fRaw.close



