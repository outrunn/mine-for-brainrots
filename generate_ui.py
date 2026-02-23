#!/usr/bin/env python3
"""Generate UI assets for Mine for Brainrots using DALL-E API"""

import os
import sys
import requests
from pathlib import Path

# Get API key from command line or environment
api_key = sys.argv[1] if len(sys.argv) > 1 else os.getenv('OPENAI_API_KEY')
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set")
    exit(1)

# Create assets directory
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
    
    # Download the image
    img_response = requests.get(image_url)
    output_path = assets_dir / filename
    
    with open(output_path, 'wb') as f:
        f.write(img_response.content)
    
    print(f"✓ Saved to: {output_path}")
    return True

# Generate money icon
money_prompt = """A tiny, bright, high saturation, childish money icon for a Roblox game UI. 
Style: cute cartoon gold coin with simple shapes, vibrant yellow/gold colors, slight 3D effect, 
clean edges, glossy finish. Should be easily readable at small sizes. Icon design, centered on 
transparent background, PNG format. Bright and cheerful, kid-friendly design."""

generate_image(money_prompt, "money_icon.png")

# Generate back to home button
button_prompt = """A UI button asset for a Roblox game. Green studded background (like LEGO studs texture). 
Text "BACK TO HOME" in Comic Sans font, white color with black outline (2-3px stroke). The button should be 
rectangular, bright green with a pattern of small circular studs/bumps. Clean, crisp text, high contrast. 
Game UI button design, PNG format."""

generate_image(button_prompt, "back_to_home_button.png")

print("\n✅ Generation complete!")
print(f"Assets saved to: {assets_dir}")
