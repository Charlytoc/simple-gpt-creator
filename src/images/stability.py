import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

STABILITY_KEY = os.environ.get('STABILITY_API_KEY')


class ImageGenerator:
    def __init__(self, title:str="ai_image", samples:int=1):
        
        self.title = title
        self.samples = samples

      
    def generate(self,description: str):
      url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

      body = {
        "width": 1024,
        "height": 1024,
        "steps": 40,
        "seed": 0,
        "cfg_scale": 7,
        "samples": self.samples,
        "style_preset": "enhance",
        "text_prompts": [
          {
            "text": description,
            "weight": 1
          }
        ],
      }

      headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {STABILITY_KEY}",
      }

      response = requests.post(
        url,
        headers=headers,
        json=body,
      )

      if response.status_code != 200:
          raise Exception("Non-200 response: " + str(response.text))

      data = response.json()

      if not os.path.exists('./out'):
          os.makedirs('./out')


      for i, image in enumerate(data["artifacts"]):
          with open(f"./out/{self.title}-{i}.png", "wb") as f:
              f.write(base64.b64decode(image["base64"]))