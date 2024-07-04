import openai
import os
import requests
from PIL import Image
import json

client = AzureOpenAI(
    api_version="2024-02-01",  
    api_key=os.environ["cb6deded95cf4f33a4bf4fa15f113639"],  
    azure_endpoint=os.environ['https://dsc-kore4.openai.azure.com/']
)

result = client.images.generate(
    model="Dalle3", # the name of your DALL-E 3 deployment
    prompt="青い雪だるまを描いてください。",
    n=1
)

json_response = json.loads(result.model_dump_json())

# Set the directory for the stored image
image_dir = os.path.join(os.curdir, 'images')

# If the directory doesn't exist, create it
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# Initialize the image path (note the filetype should be png)
image_path = os.path.join(image_dir, 'generated_image.png')

# Retrieve the generated image
image_url = json_response["data"][0]["url"]  # extract image URL from response
generated_image = requests.get(image_url).content  # download the image
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

# Display the image in the default image viewer
image = Image.open(image_path)
image.show()