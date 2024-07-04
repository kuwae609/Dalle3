import openai 
import os
import requests
from PIL import Image
import json

url = "https://dsc-kore4.openai.azure.com/openai/deployments/Dalle3/images/generations?api-version=2024-02-01"

headers = {
    "Content-Type": "application/json",
    "api-key": "cb6deded95cf4f33a4bf4fa15f113639"
}

data = {
    "prompt": """
        テーマ/コンセプト: 直立二足歩行で舵取りするネズミ
        スタイル: 1920年代のトーキーアニメーション風
        色合い/ムード: モノクロ
        キャラクターの特徴:耳が大きくて丸い、帽子をかぶっている、ズボンをはいている、靴を履いている
        アクション/ポーズ: 舵取りをしながら口笛を吹いている
        場所: 船の上
        時間帯: 昼
        追加のディテール: アメリカの蒸気船にのっている
        """,
    "size": "1024x1024", 
    "n": 1,
    "quality": "hd", 
    "style": "vivid"
}

response = requests.post(url, headers=headers, json=data)

# ステータスコードとレスポンスの内容を確認
print(response.status_code)
print(response.text)

# # レスポンスをJSON形式に変換
# json_response = json.loads(result.model_dump_json())

# # 画像を保存するディレクトリを設定
# image_dir = os.path.join(os.curdir, 'images')

# # ディレクトリが存在しない場合、作成する
# if not os.path.isdir(image_dir):
#     os.mkdir(image_dir)

# # 画像の保存パスを初期化
# image_path = os.path.join(image_dir, 'headwaters.png')

# # 生成された画像を取得
# image_url = json_response["data"][0]["url"]  
# generated_image = requests.get(image_url).content  

# # 画像をファイルに書き込む
# with open(image_path, "wb") as image_file:
#     image_file.write(generated_image)