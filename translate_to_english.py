#!/usr/bin/env python3
"""
Comprehensive English Translation Script
Translates Czech content to English in all -en.html files
"""

import re
from pathlib import Path

# Comprehensive translation dictionary
TRANSLATIONS = {
    # Meta & HTML attributes
    'lang="cs"': 'lang="en"',
    'Luxusní soukromé spa v Praze': 'Luxury Private Spa in Prague',
    
    # Navigation
    'Prostor': 'Space',
    'Sauny a Ceremoniály': 'Sauna & Ceremonies',
    'Sauny\n                    a Ceremoniály': 'Sauna &\n                    Ceremonies',
    'Doplňkové Procedury': 'Additional Treatments',
    'Doplňkové\n                    Procedury': 'Additional\n                    Treatments',
    'Ceny': 'Prices',
    'O Nás': 'About Us',
    'O\n                    Nás': 'About\n                    Us',
    'Kontakty': 'Contacts',
    
    # Buttons & CTAs
    'Price': 'Price',
    'Booking': 'Booking',
    'CENÍK<br>REZERVACE': 'PRICE LIST<br>BOOKING',
    'CENÍK<br/>REZERVACE': 'PRICE LIST<br/>BOOKING',
    'More': 'More',
    
    # Section Headings
    'WELLNESS<br>PROSTOR': 'WELLNESS<br>SPACE',
    'WELLNESS PROSTOR': 'WELLNESS SPACE',
    'SAUNA CEREMONIÁLY': 'SAUNA CEREMONIES',
    'MASÁŽE': 'MASSAGES',
    'ZKUŠENOSTI & REFERENCE': 'EXPERIENCE & REFERENCES',
    'KONTAKT': 'CONTACT',
    'SPOLUPRÁCE': 'PARTNERSHIP',
    
    # Common phrases
    'Prostor je ideální': 'The space is ideal',
    'Každý detail je navržen': 'Every detail is designed',
    'Exkluzivní saunový zážitek': 'Exclusive sauna experience',
    'Saunové ceremoniály s': 'Sauna ceremonies with',
    'hluboká relaxace a regenerace': 'deep relaxation and regeneration',
    'Rezervace od 2 hodin': 'Bookings from 2 hours',
    
    # Wellness descriptions
    'Prostor je ideální pro páry, rodiny, mini skupiny i individuální návštěvy': 'The space is ideal for couples, families, small groups and individual visits',
    'Každý detail je navržen tak, aby vám umožnil zpomalit, vypnout a užít si čas bez rušení': 'Every detail is designed to allow you to slow down, disconnect and enjoy time without disturbance',
    
    # Sauna descriptions
    'Exkluzivní saunový zážitek v soukromém prostředí': 'Exclusive sauna experience in a private setting',
    'Saunové ceremoniály s pečlivě vybranými esenciálními oleji, hluboká relaxace a regenerace těla i mysli': 'Sauna ceremonies with carefully selected essential oils, deep relaxation and regeneration of body and mind',
    'Rezervace od 2 hodin pro páry i menší skupiny': 'Bookings from 2 hours for couples and small groups',
    
    # Massage descriptions  
    'V našem soukromém spa nabízíme profesionální masáže a doplňkové procedury, které podporují hlubokou relaxaci, regeneraci těla a celkovou rovnováhu': 'In our private spa we offer professional massages and additional treatments that support deep relaxation, body regeneration and overall balance',
    'Každá procedura probíhá v klidném, privátním prostředí a je přizpůsobena vašim potřebám': 'Each treatment takes place in a calm, private environment and is tailored to your needs',
    
    # Contact section
    'Rezervace': 'Booking',
    'Individuální programy & akce': 'Individual Programs & Events',
    'Spolupráce': 'Partnership',
    'Address': 'Address',
    'Social Media': 'Social Media',
    'Contact Us': 'Contact Us',
    
    # Footer
    'Rád vás přivítáme': 'We will be happy to welcome you',
    'Přijímáme také poptávky': 'We also accept inquiries',
    'Máte zájem o spolupráci': 'Are you interested in cooperation',
    'Vyplňte prosím kontaktní formulář': 'Please fill in the contact form',
    
    # Form
    'Kontaktní formulář': 'Contact Form',
    'Jméno a příjmení': 'Full Name',
    'E-mailová adresa': 'Email Address',
    'S čím Vám můžeme pomoci?': 'How can we help you?',
    'Telefonní číslo': 'Phone Number',
    'Datum': 'Date',
    'Informace o specifických potřebách (dieta) *': 'Information about specific needs (diet) *',
    'Souhlasím s Podmínkami zpracování osobních údajů': 'I agree to the Personal Data Processing Terms',
    'Odeslat poptávku': 'Submit Inquiry',
    
    # Reference section
    'NAPSAL I O NÁS': 'WRITTEN ABOUT US',
    'Reference': 'References',
    
    # Page titles (specific sections)
    'Finská Sauna &<br>Saunové Rituály': 'Finnish Sauna &<br>Sauna Rituals',
    'Sauna Ceremoniály': 'Sauna Ceremonies',
    
    # Wellness page specific
    'Wellness Base Program': 'Wellness Base Program',
}

def translate_file(file_path):
    """Translate Czech text to English in a single file"""
    print(f"\nTranslating {file_path.name}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply translations
    for czech, english in TRANSLATIONS.items():
        content = content.replace(czech, english)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Translated {file_path.name}")

def main():
    base_dir = Path('/Users/viktorkamyshentsev/Desktop/gravity/spa-deluxe-site')
    english_files = [
        base_dir / 'index-en.html',
        base_dir / 'wellness-en.html',
        base_dir / 'sauna-en.html',
        base_dir / 'massage-en.html',
    ]
    
    print("Starting English translation of all files...")
    
    for file_path in english_files:
        if file_path.exists():
            translate_file(file_path)
        else:
            print(f"Warning: {file_path.name} not found")
    
    print("\n✓ Translation complete!")
    print("Note: Manual review recommended for context-specific content.")

if __name__ == '__main__':
    main()
