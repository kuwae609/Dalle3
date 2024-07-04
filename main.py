from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ImageLinkRequest(BaseModel):
    url: str

# 画像リンクの取得エンドポイント
@app.post("/fetch-image-link/")
async def fetch_image_link(image_link_request: ImageLinkRequest):
    response = requests.get(image_link_request.url)
    if response.status_code == 200:
        with open("files/downloaded_image.jpg", "wb") as file:
            file.write(response.content)
        return {"info": "Image downloaded successfully"}
    return {"error": "Failed to fetch image"}