# import google.generativeai as genai
# from PIL import Image

# # Configure API
# genai.configure(api_key="AIzaSyBSiJraERUhckpvc6_9YMlBeLBekY1a9pQ")

# # Load model
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Open image with PIL
# image_path = r"C:\Users\Anooj Dilip Archana\Desktop\pothole.jpg"
# img = Image.open(image_path)

# # Step 1: Get Description
# desc_response = model.generate_content(
#     [img, "Description:"]
# )
# description = desc_response.text.strip()
# print("Image Description:", description)

# # Step 2: Get Category
# cat_response = model.generate_content(
#     [img, f"Based on the description '{description}', categorize this image into one of the following civic issue categories: Garbage, Pothole, Streetlight, Water Leakage, Illegal Parking. Only return the category name."]
# )
# category = cat_response.text.strip()
# print("Predicted Category:", category)




import google.generativeai as genai
from PIL import Image
import json
import csv
import os

# Configure API
genai.configure(api_key="AIzaSyBSiJraERUhckpvc6_9YMlBeLBekY1a9pQ")

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Open image with PIL
image_path = r"C:\Users\Anooj Dilip Archana\Desktop\pothole.jpg"
img = Image.open(image_path)

# Step 1: Get Description
desc_response = model.generate_content(
    [img, "Provide a clear, concise one-sentence description of this image focusing on the civic issue visible."]
)
description = desc_response.text.strip()
print("Image Description:", description)

# Step 2: Get Category
cat_response = model.generate_content(
    [img, f"Only return the category name (Garbage, Pothole, Streetlight, Water Leakage, Illegal Parking) that best matches this description: '{description}'."]
)
category = cat_response.text.strip()
print("Predicted Category:", category)