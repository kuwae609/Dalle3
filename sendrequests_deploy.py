import requests

response = requests.post(
    url="https://dalle3-agz5.onrender.com/fetch-image-link",
    headers={"Content-Type": "application/json"},
    json={
        "url": "https://dalleproduse.blob.core.windows.net/private/images/54a081c8-71c0-4872-be36-113b050166a2/generated_00.png?se=2024-07-05T04%3A59%3A14Z&sig=H2Q18ILsFvddHxZmUh95Md8tlGjvJ0AjntVtxkGYgF4%3D&ske=2024-07-11T02%3A02%3A46Z&skoid=09ba021e-c417-441c-b203-c81e5dcd7b7f&sks=b&skt=2024-07-04T02%3A02%3A46Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02"
    },
)

print(response.status_code)
print(response.content)
