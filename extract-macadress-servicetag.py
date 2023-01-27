import os
import re
import csv
from PIL import Image
import pytesseract

# directory where images are stored
img_dir = "c:/temp"

# list to store extracted data
data = []

# regular expression pattern for MAC address and service tag
#mac_pattern = re.compile(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})')
mac_pattern = re.compile(r'Adresse\sMAC\s:\s([0-9A-Z]{12})')
tag_pattern = re.compile(r'Service\sTag\s:\s([0-9A-Z]{7})')

# set OCR language to French
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_oem_psm_config = r'--oem 3 --psm 6'

# loop through images in directory
for filename in os.listdir(img_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filepath = os.path.join(img_dir, filename)
        # open image and extract text using OCR
        text = pytesseract.image_to_string(Image.open(filepath), config=custom_oem_psm_config)
        print (text)
        # search for MAC address and service tag in text
        mac = mac_pattern.search(text)
        tag = tag_pattern.search(text)
        if mac:
            mac = mac.group(1)
        if tag:
            tag = tag.group(1)
        # add data to list
        data.append([filename, mac, tag])

# write data to csv file
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "mac_address", "service_tag"])
    writer.writerows(data)