#!/usr/bin/env python3
"""Generate vector-style neon green money icon with transparent background"""

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

# Generate vector-style neon green money icon with transparent background
money_prompt = """A simple, flat vector-style neon green dollar bill icon. ABSOLUTELY NO BACKGROUND - fully transparent/checkered background. 
Simple rectangular bright neon green (#00FF00) paper money shape with a bold dollar sign ($) symbol in the center. 
Flat design, no shadows, no gradients, clean vector-style illustration. The bill should be neon green with minimal detail.
Icon must be isolated on completely transparent background. PNG format with alpha channel transparency."""

generate_image(money_prompt, "money_icon_vector.png")
print("\n✅ Vector-style transparent money icon generated!")
