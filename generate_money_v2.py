#!/usr/bin/env python3
"""Generate neon green money icon"""

import sys
import requests
from pathlib import Path

api_key = sys.argv[1] if len(sys.argv) > 1 else None
if not api_key:
    print("Error: API key required")
    exit(1)

assets_dir = Path(__file__).parent / "assets"
assets_dir.mkdir(exist_ok=True)

def generate_image(prompt, filename):
    """Generate image using DALL-E API"""
    print(f"Generating: {filename}")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024",
        "quality": "standard"
    }
    
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers=headers,
        json=payload
    )
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
        return False
    
    data = response.json()
    image_url = data['data'][0]['url']
    
    img_response = requests.get(image_url)
    output_path = assets_dir / filename
    
    with open(output_path, 'wb') as f:
        f.write(img_response.content)
    
    print(f"✓ Saved to: {output_path}")
    return True

# Generate neon green money icon
money_prompt = """A simple neon green paper money/dollar bill icon for a Roblox game UI. 
Flat design, bright neon green color (#00FF00 range), simple rectangular paper bill shape 
with a dollar sign ($) in the center. Clean, minimalist icon design, high contrast, 
vibrant and eye-catching. Should be easily readable at small sizes. Centered on transparent 
background, PNG format. Childish, game-style UI icon."""

generate_image(money_prompt, "money_icon_v2.png")
print("\n✅ New money icon generated!")
