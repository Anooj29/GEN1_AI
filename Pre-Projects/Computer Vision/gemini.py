import google.generativeai as genai
from PIL import Image

# Configure API
genai.configure(api_key="AIzaSyBSiJraERUhckpvc6_9YMlBeLBekY1a9pQ")

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Open image with PIL
image_path = r"C:\Users\Anooj Dilip Archana\Desktop\pothole.jpg"
img = Image.open(image_path)

# Ask Gemini
response = model.generate_content(
    [img, "Categorize this image into one of the following civic issue categories: Garbage, Pothole, Streetlight, Water Leakage, Illegal Parking."]
)

print("Predicted Category:", response.text)
