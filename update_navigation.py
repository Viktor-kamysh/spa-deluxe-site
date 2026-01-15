#!/usr/bin/env python3
"""
Bilingual Website Navigation Updater
Updates navigation links in English files and prepares translation map
"""

import re
from pathlib import Path

# Navigation link mappings
LINK_MAPPINGS = {
    'href="wellness.html"': 'href="wellness-en.html"',
    'href="sauna.html"': 'href="sauna-en.html"',
    'href="massage.html"': 'href="massage-en.html"',
    'href="index.html"': 'href="index-en.html"',
    'href="index.html#o-nas"': 'href="index-en.html#o-nas"',
}

# Translation dictionary
TRANSLATIONS = {
    # Navigation
    'Prostor': 'Space',
    'Sauny a Ceremoniály': 'Sauna & Ceremonies',
    'Sauny\n                    a Ceremonálý': 'Sauna &\n                    Ceremonies',
    'Doplňkové Procedury': 'Additional Treatments',
    'Doplňkové\n                    Procedury': 'Additional\n                    Treatments',
    'Ceny': 'Prices',
    'O Nás': 'About Us',
    'O\n                    Nás': 'About\n                    Us',
    'Kontakty': 'Contacts',
    'Rezervace': 'Booking',
    
    # Buttons & CTAs
    'Price': 'Price',
    'Booking': 'Booking',
    'CENÍK<br>REZERVACE': 'PRICE LIST<br>BOOKING',
    'More': 'More',
    
    # Common phrases
    'WELLNESS PROSTOR': 'WELLNESS SPACE',
    'SAUNA CEREMONIÁLY': 'SAUNA CEREMONIES',
    'MASÁŽE': 'MASSAGES',
    
    # Meta
    'lang="cs"': 'lang="en"',
    'Luxusní soukromé spa v Praze': 'Luxury Private Spa in Prague',
}

def update_navigation_links(file_path):
    """Update navigation links in English files"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_link, new_link in LINK_MAPPINGS.items():
        content = content.replace(old_link, new_link)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated navigation links in {file_path.name}")

def main():
    base_dir = Path('/Users/viktorkamyshentsev/Desktop/gravity/spa-deluxe-site')
    english_files = [
        base_dir / 'index-en.html',
        base_dir / 'wellness-en.html',
        base_dir / 'sauna-en.html',
        base_dir / 'massage-en.html',
    ]
    
    print("Updating navigation links in English files...")
    for file_path in english_files:
        if file_path.exists():
            update_navigation_links(file_path)
        else:
            print(f"Warning: {file_path.name} not found")
    
    print("\nNavigation links updated successfully!")

if __name__ == '__main__':
    main()
