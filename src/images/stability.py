import base64
import requests


import os

class ImageGenerator:
    def generate(self, description: str):
      url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v0-9/text-to-image"

      body = {
        "width": 1024,
        "height": 1024,
        "steps": 50,
        "seed": 0,
        "cfg_scale": 7,
        "samples": 1,
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
        "Authorization": "Bearer sk-fewmPTk2ZdxnBQvZm2ymWwXMKhqsmUQ1aUcgDhMIiXMG6pFI",
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
          with open(f"./out/txt2img_{image['seed']}.png", "wb") as f:
              f.write(base64.b64decode(image["base64"]))