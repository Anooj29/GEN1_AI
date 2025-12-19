from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load an image from computer
image_path = r"C:\Users\Anooj Dilip Archana\Desktop\big-plastic-pollution-7937068.jpg"
image = Image.open(image_path)

# Preprocess and generate caption
inputs = processor(images=image, return_tensors="pt")
out = model.generate(**inputs)

# Print caption
print("Generated Caption:", processor.decode(out[0], skip_special_tokens=True))
