import openai
import os
from getpass import getpass
import requests
import json
import base64

# # AzureのエンドポイントとAPIキーを環境変数に設定
# os.environ["AZURE_OPENAI_ENDPOINT"] = getpass('Azure OpenAI Endpoint:')
# os.environ["AZURE_OPENAI_API_KEY"] = getpass('Azure OpenAI API Key:')

# AzureのエンドポイントとAPIキーを取得
azure_openai_endpoint = "https://dsc-kore4.openai.azure.com/"
azure_openai_api_key = "cb6deded95cf4f33a4bf4fa15f113639"

# リクエストヘッダー
headers = {
    "Content-Type": "application/json",
    "api-key": azure_openai_api_key
}

# リクエストボディ
data = {
    "model": "dall-e-3",  # モデル
    "prompt": "青い雪だるまを描いてください",  # プロンプト
    "n": 1,  # 生成数
    "size": "1024x1024",  # 解像度 dall-e-3では1024x1024、1792x1024、1024x1792
    "response_format": "b64_json",  # レスポンスフォーマット url or b64_json
    "quality": "hd",  # 品質 standard or hd
    "style": "vivid"  # スタイル vivid or natural
}

# APIリクエスト送信
response = requests.post(
    f"{azure_openai_endpoint}/openai/images/generate",
    headers=headers,
    data=json.dumps(data)
)

# レスポンスをJSON形式で取得
response_data = response.json()

# base64エンコードされた画像データを取得
image_data = response_data['data'][0]['b64_json']
image_bytes = base64.b64decode(image_data)

# 画像を保存
with open("generated_image.png", "wb") as f:
    f.write(image_bytes)

print("Image saved as 'generated_image.png'")
