from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import cv2
import numpy as np
from imgsim import Vectorizer, distance
from io import BytesIO

app = FastAPI()


class ImageLinkRequest(BaseModel):
    url: str


def load_image_from_url(url):
    try:
        # URLから画像をダウンロード
        response = requests.get(url)
        img_np = np.array(bytearray(response.content), dtype=np.uint8)

        # OpenCVで画像を読み込む
        img = cv2.imdecode(img_np, -1)

        return img
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error loading image from url: {e}"
        )


@app.post("/fetch-image-link/")
async def fetch_image_link(image_link_request: ImageLinkRequest):
    try:
        img_url = image_link_request.url
        img0 = load_image_from_url(img_url)
        img1_url = "https://www.udiscovermusic.jp/wp-content/uploads/2020/05/Mickey-Mouse-Steamboat-Willie-web-optimised-1000.jpg"
        img1 = load_image_from_url(img1_url)

        vtr = Vectorizer()
        vec0 = vtr.vectorize(img0)
        vec1 = vtr.vectorize(img1)

        dist = distance(vec0, vec1)

        return {"distance": f"{dist}"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing images: {e}")
