from fastapi import FastAPI
from pydantic import BaseModel
import requests
import imgsim
import cv2
import requests
import numpy as np
from io import BytesIO


def load_image_from_url(url):
    try:
        # URLから画像をダウンロード
        response = requests.get(url)
        img_np = np.array(bytearray(response.content), dtype=np.uint8)

        # OpenCVで画像を読み込む
        img = cv2.imdecode(img_np, -1)

        return img
    except Exception as e:
        print(f"Error loading image from url: {e}")
        return None


app = FastAPI()


class ImageLinkRequest(BaseModel):
    url: str


# 画像リンクの取得エンドポイント
@app.post("/fetch-image-link/")  # 生成画像のリンク
async def fetch_image_link(image_link_request: ImageLinkRequest):
    response = requests.get(image_link_request.url)  # 生成画像のダウンロード
    img0 = load_image_from_url(image_link_request.url)
    img1 = load_image_from_url(
        "https://www.udiscovermusic.jp/wp-content/uploads/2020/05/Mickey-Mouse-Steamboat-Willie-web-optimised-1000.jpg"
    )
    vtr = imgsim.Vectorizer()
    vec0 = vtr.vectorize(img0)
    vec1 = vtr.vectorize(img1)

    dist = imgsim.distance(vec0, vec1)
    #
    if response.status_code == 200:
        return {"distance": f"{dist}"}
    return {"error": "Failed to fetch image"}
