#!/usr/bin/env python3
"""
Price Modal Translation Script
Translates all Czech text in price modals to English across all -en.html files
"""

from pathlib import Path

# Comprehensive modal translations
MODAL_TRANSLATIONS = {
    # Header artistic text
    'ZDRAVÍ': 'HEALTH',
    'RELAXACE': 'RELAXATION',
    'A PÉČE': 'AND BODY CARE',
    'O TĚLO': '',  # Already handled by "A PÉČE"
    'V HARMONII': 'IN HARMONY',
    
    # Basic pricing
    'Základní cena': 'Basic Price',
    '2 hod | Po–Čt': '2 hours | Mon–Thu',
    '2 hod | Pá–Ne': '2 hours | Fri–Sun',
    '(pro 1–2 osoby)': '(for 1–2 people)',
    'Prodloužení: + 2 000 Kč / každá další hodina': 'Extension: + 2 000 CZK / each additional hour',
    'Další osoba: + 500 Kč / osoba': 'Extra person: + 500 CZK / person',
    
    # Amenities
    'privátní rezervace celého prostoru': 'private reservation of the entire space',
    'finská sauna až 90 °C': 'Finnish sauna up to 90 °C',
    'ochlazovací bazén & sprchy': 'cooling pool & showers',
    'relax zóna': 'relaxation zone',
    'voda s esenciálními oleji dōTERRA': 'water with dōTERRA essential oils',
    'čajový ceremoniál': 'tea ceremony',
    'ručníky & prostěradla': 'towels & sheets',
    'kompletní servis a úklid': 'complete service and cleaning',
    'jednorázové pantofle': 'disposable slippers',
    'kosmetika (šampon a sp.gel)': 'cosmetics (shampoo & shower gel)',
    
    # Section headers
    'Rezervace masáží & procedur': 'Reservation of Massages & Treatments',
    'DOPLŇKOVÉ PROCEDURY': 'ADDITIONAL TREATMENTS',
    'SAUNOVÉ CEREMONIE & RITUÁLY': 'SAUNA CEREMONIES & RITUALS',
    '(CENA JE UVEDENA ZA 2 HODINY A PŘIČÍTÁ SE K ZÁKLADNÍ REZERVACI)': '(PRICE IS FOR 2 HOURS AND IS ADDED TO THE BASIC RESERVATION)',
    
    # Sauna ceremonies
    'AROMA CEREMONIE S DŌTERRA': 'AROMA CEREMONY WITH DŌTERRA',
    'ŘÍZENÝ SAUNOVÝ RITUÁL S INDIVIDUÁLNÍM VÝBĚREM ESENCIÁLNÍCH OLEJŮ, HLUBOKÁ RELAXACE A HARMONIZACE TĚLA I MYSLI': 'GUIDED SAUNA RITUAL WITH INDIVIDUAL SELECTION OF ESSENTIAL OILS, DEEP RELAXATION AND HARMONIZATION OF BODY AND MIND',
    'SAUNOVÝ RITUÁL – PAŘENÍ METLIČKAMI (2 HOD)': 'SAUNA RITUAL – WHISKING (VENIK) (2 HOURS)',
    'TRADIČNÍ PROHŘÍVÁNÍ, PRÁCE S PÁROU A METLIČKAMI, UVOLNĚNÍ SVALŮ A CELKOVÁ REGENERACE': 'TRADITIONAL HEATING, STEAM AND WHISK WORK, MUSCLE RELAXATION AND OVERALL REGENERATION',
    '/ OSOBA': '/ PERSON',
    '/ SKUPINA': '/ GROUP',
    
    # Massages
    'MASÁŽE': 'MASSAGES',
    'KLASICKÁ · RELAXAČNÍ · SPORTOVNÍ · LYMFATICKÁ · ANTICELULITIDNÍ · MEDOVÁ · BAŇKOVÁ': 'CLASSIC · RELAXING · SPORTS · LYMPHATIC · ANTI-CELLULITE · HONEY · CUPPING',
    'ODBORNÝ VÝBĚR S KONZULTACÍ': 'EXPERT SELECTION WITH CONSULTATION',
    'KAŽDÁ MASÁŽ JE INDIVIDUÁLNĚ ZVOLENA NA ZÁKLADĚ KONZULTACE S NAŠÍM CERTIFIKOVANÝM SPECIALISTOU...': 'EACH MASSAGE IS INDIVIDUALLY CHOSEN BASED ON CONSULTATION WITH OUR CERTIFIED SPECIALIST...',
    'PÁROVÁ MASÁŽ 60 / 90 MIN — CENA × 2': 'COUPLES MASSAGE 60 / 90 MIN — PRICE × 2',
    'MASÁŽ VE 4 RUCE 60 / 90 MIN — CENA × 2': '4-HAND MASSAGE 60 / 90 MIN — PRICE × 2',
    
    # Cosmetic treatments
    'KOSMETICKÉ PROCEDURY PRO TĚLO – COMFORT ZONE': 'COSMETIC BODY TREATMENTS – COMFORT ZONE',
    'PRACUJEME S PRÉMIOVOU ITALSKOU SPA KOSMETIKOU COMFORT ZONE. NAŠI TERAPEUTI JSOU AMBASADORY ZNAČKY...': 'WE WORK WITH PREMIUM ITALIAN SPA COSMETICS COMFORT ZONE. OUR THERAPISTS ARE BRAND AMBASSADORS...',
    'POUŽÍVANÉ ŘADY': 'USED RANGES',
    'TĚLOVÝ PEELING': 'BODY PEELING',
    'HYDRATAČNÍ TĚLOVÝ RITUÁL': 'HYDRATING BODY RITUAL',
    'DETOXIKAČNÍ RITUÁL': 'DETOX RITUAL',
    'REGENERAČNÍ RITUÁL PO SAUNĚ': 'REGENERATING RITUAL AFTER SAUNA',
    
    # Ladies ritual
    'SPECIÁLNÍ NABÍDKA PRO DÁMY – LADIES WELLNESS RITUAL': 'SPECIAL OFFER FOR LADIES – LADIES WELLNESS RITUAL',
    'PRIVÁTNÍ SPA, FINSKÁ SAUNA, AROMATERAPIE DŌTERRA A KOSMETICKÝ RITUÁL COMFORT ZONE PRO KAŽDOU DÁMU.': 'PRIVATE SPA, FINNISH SAUNA, DŌTERRA AROMATHERAPY AND COMFORT ZONE COSMETIC RITUAL FOR EVERY LADY.',
    '(POUZE PO–ČT | PRIVÁTNĚ)': '(MON–THU ONLY | PRIVATE)',
    'PROGRAM ZAHRNUJE': 'PROGRAM INCLUDES',
    'MINIMÁLNÍ POČET OSOB': 'MINIMUM NUMBER OF PERSONS',
    
    # Footer
    'V případě dotazů, konzultace nebo individuálních požadavků kontaktujte naše administrátory, kteří vám rádi pomohou s výběrem programu i samotnou rezervací.': 'In case of questions, consultation or individual requests, please contact our administrators who will be happy to help you choose a program and make a reservation.',
    'OKAMŽITÁ REZERVACE & DOTAZY': 'IMMEDIATE RESERVATION & INQUIRIES',
    
    # Booking info
    'Masáže a doplňkové procedury jsou poskytovány výhradně na základě předchozí rezervace. Pro zajištění dostupnosti terapeutů a přípravu prostoru je nutná předběžná objednávka před vaší návštěvou spa. Doporučujeme rezervovat masáže a procedury současně s rezervací privátního spa, aby bylo možné připravit služby přesně podle vašich požadavků.': 'Massages and additional treatments are provided exclusively based on prior reservation. To ensure therapist availability and space preparation, advance booking is required before your spa visit. We recommend reserving massages and treatments simultaneously with your private spa booking so services can be prepared exactly according to your requirements.',
}

def translate_file(file_path):
    """Apply all modal translations to a single file"""
    print(f"\nTranslating modal in {file_path.name}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Track changes
    changes = 0
    for czech, english in MODAL_TRANSLATIONS.items():
        if czech in content:
            content = content.replace(czech, english)
            changes += 1
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Applied {changes} translations to {file_path.name}")
    return changes

def main():
    base_dir = Path('/Users/viktorkamyshentsev/Desktop/gravity/spa-deluxe-site')
    english_files = [
        base_dir / 'index-en.html',
        base_dir / 'wellness-en.html',
        base_dir / 'sauna-en.html',
        base_dir / 'massage-en.html',
    ]
    
    print("=" * 60)
    print("PRICE MODAL TRANSLATION TO ENGLISH")
    print("=" * 60)
    
    total_changes = 0
    for file_path in english_files:
        if file_path.exists():
            changes = translate_file(file_path)
            total_changes += changes
        else:
            print(f"Warning: {file_path.name} not found")
    
    print("\n" + "=" * 60)
    print(f"✓ COMPLETE! Total translations applied: {total_changes}")
    print("=" * 60)

if __name__ == '__main__':
    main()
