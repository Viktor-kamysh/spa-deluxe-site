#!/usr/bin/env python3
"""
Complete Price Modal Replacement Script
Replaces entire modal HTML with fully translated English version
"""

from pathlib import Path
import re

# The complete English modal HTML
ENGLISH_MODAL = '''<div id="priceModal" class="fixed inset-0 z-[100] hidden" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-900/60 backdrop-blur-sm transition-opacity" onclick="closePriceModal()"></div>

    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">

            <div class="relative transform overflow-hidden rounded-[2rem] bg-[#e5e5e5] text-left shadow-2xl transition-all sm:my-8 sm:w-full sm:max-w-5xl border border-white/50">

                <button type="button" onclick="closePriceModal()" class="absolute top-6 right-6 z-20 text-gray-500 hover:text-gray-800 transition">
                    <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>

                <div class="p-8 md:p-16 brand-pattern">

                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 mb-16 items-start">

                        <div class="text-center lg:text-left flex flex-col justify-center h-full pt-8 space-y-10">
                            <div class="font-serif text-4xl text-[#5a7d8d] uppercase tracking-widest">HEALTH</div>
                            <div class="flex items-center justify-center lg:justify-start gap-4">
                                <span class="script text-7xl text-[#5a7d8d]">R</span>
                                <span class="font-serif text-4xl text-[#4a4a4a] uppercase tracking-widest">ELAXATION</span>
                            </div>
                            <div class="font-serif text-2xl text-[#5a7d8d] uppercase tracking-widest pl-12">AND BODY CARE</div>
                            <div class="font-serif text-4xl text-[#4a4a4a] uppercase tracking-widest">IN HARMONY</div>
                        </div>

                        <div class="bg-[#e9ecef]/80 rounded-3xl p-8 shadow-sm text-center text-[#5a7d8d]">
                            <p class="text-sm mb-6 leading-relaxed">
                                The 'Wellness Base' is a private program during which you have the entire spa space reserved exclusively for yourself. An ideal choice for couples, families, or small groups seeking peace, privacy, and quality relaxation.
                            </p>
                            <h3 class="font-bold text-lg uppercase tracking-wide mb-2">BASIC PRICE</h3>
                            <p class="font-bold text-[#4a6d7d] text-lg">2 hours | Mon–Thu — 2 500 CZK</p>
                            <p class="font-bold text-[#4a6d7d] text-lg mb-2">2 hours | Fri–Sun — 3 500 CZK</p>
                            <p class="text-xs mb-6">(for 1–2 people)</p>

                            <div class="text-sm space-y-1 mb-6">
                                <p>Extension: + 2 000 CZK / each additional hour</p>
                                <p>Extra person: + 500 CZK / person</p>
                            </div>

                            <div class="text-left text-xs grid grid-cols-2 gap-4 text-gray-600">
                                <ul class="list-disc list-inside space-y-1">
                                    <li>private reservation of the entire space</li>
                                    <li>Finnish sauna up to 90 °C</li>
                                    <li>cooling pool & showers</li>
                                    <li>relaxation zone</li>
                                    <li>water with dōTERRA essential oils</li>
                                </ul>
                                <ul class="list-disc list-inside space-y-1">
                                    <li>tea ceremony</li>
                                    <li>towels & sheets</li>
                                    <li>complete service and cleaning</li>
                                    <li>disposable slippers</li>
                                    <li>cosmetics (shampoo & shower gel)</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="w-full h-px bg-gray-300 mb-12"></div>

                    <div class="text-center mb-16 max-w-3xl mx-auto">
                        <h3 class="font-serif text-xl text-[#5a7d8d] uppercase mb-4">Reservation of Massages & Treatments</h3>
                        <p class="text-sm text-gray-600 leading-relaxed">
                            Massages and additional treatments are provided exclusively based on prior reservation. To ensure therapist availability and space preparation, advance booking is required before your spa visit. We recommend booking massages and treatments simultaneously with your private spa reservation to ensure services are prepared exactly according to your requests.
                        </p>
                    </div>

                    <div class="space-y-16 text-center text-[#5a7d8d]">

                        <div>
                            <h3 class="font-serif text-2xl uppercase tracking-widest mb-8 text-[#4a4a4a]">ADDITIONAL TREATMENTS</h3>

                            <div class="mb-8">
                                <h4 class="font-serif text-lg uppercase mb-1">SAUNA CEREMONIES & RITUALS</h4>
                                <p class="text-[10px] uppercase tracking-wider text-gray-500 mb-4">(PRICE IS FOR 2 HOURS AND IS ADDED TO THE BASIC RESERVATION)</p>

                                <div class="mb-6">
                                    <p class="font-medium uppercase">AROMA CEREMONY WITH DŌTERRA</p>
                                    <p class="font-bold text-lg text-[#4a6d7d]">1 500 CZK - 2 HOURS</p>
                                    <p class="text-xs text-gray-500 mt-1 uppercase">GUIDED SAUNA RITUAL WITH INDIVIDUAL SELECTION OF ESSENTIAL OILS, DEEP RELAXATION AND HARMONIZATION OF BODY AND MIND</p>
                                </div>

                                <div>
                                    <p class="font-medium uppercase">SAUNA RITUAL – WHISKING (VENIK) (2 HOURS)</p>
                                    <p class="text-xs text-gray-500 mb-1 uppercase">TRADITIONAL HEATING, STEAM AND WHISK WORK, MUSCLE RELAXATION AND OVERALL REGENERATION</p>
                                    <p class="font-bold text-lg text-[#4a6d7d]">1 500 CZK / PERSON</p>
                                    <p class="font-bold text-lg text-[#4a6d7d]">4 200 CZK / GROUP</p>
                                </div>
                            </div>
                        </div>

                        <div>
                            <h3 class="font-serif text-2xl uppercase tracking-widest mb-4 text-[#4a4a4a]">MASSAGES</h3>
                            <p class="text-xs uppercase tracking-wide text-gray-600 mb-2">CLASSIC · RELAXING · SPORTS · LYMPHATIC · ANTI-CELLULITE · HONEY · CUPPING</p>
                            <p class="text-[10px] uppercase text-gray-400 max-w-2xl mx-auto mb-6">
                                EXPERT SELECTION WITH CONSULTATION<br>
                                EACH MASSAGE IS INDIVIDUALLY CHOSEN BASED ON CONSULTATION WITH OUR CERTIFIED SPECIALIST...
                            </p>

                            <p class="font-bold text-xl text-[#4a6d7d] mb-2">60/90 min — 1 300 / 1 800 CZK</p>
                            <p class="font-medium text-lg mb-1">COUPLES MASSAGE 60 / 90 MIN — PRICE × 2</p>
                            <p class="font-medium text-lg">4-HAND MASSAGE 60 / 90 MIN — PRICE × 2</p>
                        </div>

                        <div>
                            <h3 class="font-serif text-2xl uppercase tracking-widest mb-4 text-[#4a4a4a]">COSMETIC BODY TREATMENTS – COMFORT ZONE</h3>
                            <p class="text-[10px] uppercase text-gray-500 max-w-3xl mx-auto mb-6">
                                WE WORK WITH PREMIUM ITALIAN SPA COSMETICS COMFORT ZONE. OUR THERAPISTS ARE BRAND AMBASSADORS...
                            </p>
                            <p class="font-medium uppercase mb-4">USED RANGES: TRANQUILLITY · BODY STRATEGIST · AROMASOUL · RENIGHT PROCEDURES</p>

                            <div class="space-y-2 font-medium">
                                <p>BODY PEELING — 900 CZK</p>
                                <p>HYDRATING BODY RITUAL — 1 400 CZK</p>
                                <p>DETOX RITUAL — 1 600 CZK</p>
                                <p>REGENERATING RITUAL AFTER SAUNA — 1 200 CZK</p>
                                <p>LUXURY BODY RITUAL — 1 900 CZK</p>
                            </div>
                        </div>

                        <div class="bg-white/50 rounded-2xl p-8 max-w-3xl mx-auto border border-white">
                            <h3 class="font-serif text-xl uppercase tracking-widest mb-2 text-[#4a4a4a]">SPECIAL OFFER FOR LADIES – LADIES WELLNESS RITUAL</h3>
                            <p class="text-xs uppercase text-gray-500 mb-4">PRIVATE SPA, FINNISH SAUNA, DŌTERRA AROMATHERAPY AND COMFORT ZONE COSMETIC RITUAL FOR EVERY LADY.</p>

                            <p class="font-bold text-2xl text-[#4a6d7d] mb-2">2 500 CZK / PERSON</p>
                            <p class="text-sm uppercase mb-4 text-gray-600">(MON–THU ONLY | PRIVATE)</p>

                            <div class="text-sm">
                                <p class="font-bold mb-1">PROGRAM INCLUDES</p>
                                <p class="mb-2">MINIMUM NUMBER OF PERSONS: 4</p>
                                <p class="font-bold">LADIES WELLNESS RITUAL – 2 500 CZK / PERSON</p>
                                <p class="text-xs mt-2 text-gray-500 max-w-md mx-auto">
                                    PRIVATE SPA, FINNISH SAUNA, DŌTERRA AROMATHERAPY AND COMFORT ZONE COSMETIC RITUAL FOR EVERY LADY.
                                </p>
                            </div>
                        </div>

                        <p class="text-xs text-gray-500 italic max-w-2xl mx-auto pt-8">
                            For our regular clients, we have also prepared membership subscriptions, allowing your spa visit to become a regular weekly tradition.
                            Detailed information about additional treatments can be found in the Additional Treatments section, and complete pricing in the Price List.
                        </p>
                        <p class="text-xs text-gray-500 italic max-w-2xl mx-auto pt-2">
                           In case of questions, consultation or individual requests, please contact our administrators, who will be happy to help you with program selection and the reservation itself.
                        </p>

                        <div class="mt-12 pt-8 border-t border-gray-300/50 text-center">
                            <p class="text-xs uppercase tracking-widest text-gray-500 mb-4">IMMEDIATE RESERVATION & INQUIRIES</p>
                            <a href="tel:+420703380013" class="font-serif text-3xl md:text-4xl text-[#5a7d8d] hover:text-[#4a6d7d] transition-transform hover:scale-105 inline-flex items-center gap-3">
                                <i class="fas fa-phone-alt text-2xl"></i>
                                +420 703 380 013
                            </a>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</div>'''

def replace_modal(file_path):
    """Replace entire price modal with English version"""
    print(f"\nProcessing {file_path.name}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the entire modal from opening to closing </div>
    # Find start and extract until the matching close
    pattern = r'<div id="priceModal"[^>]*>.*?(?=</div>\s*</div>\s*</div>\s*</div>\s*$)'
    
    # More robust approach: find the modal start and take everything until before </html>
    modal_start = content.find('<div id="priceModal"')
    if modal_start == -1:
        print(f"  ❌ Modal not found in {file_path.name}")
        return False
    
    # Find the closing tag - should be before </html>
    html_close = content.rfind('</html>')
    if html_close == -1:
        print(f"  ❌ Could not find </html> in {file_path.name}")
        return False
    
    # Extract content before modal and after modal
    before_modal = content[:modal_start]
    
    # Find the script closing tag that comes after the modal
    # The modal should end before the closing </html>
    # Look for the pattern that closes the modal (4 nested </div> tags)
    modal_end_pattern = '</div>\n    </div>\n</div>'
    modal_section = content[modal_start:html_close]
    modal_end_pos = modal_section.rfind(modal_end_pattern)
    
    if modal_end_pos == -1:
        print(f"  ❌ Could not find modal end in {file_path.name}")
        return False
    
    # Calculate absolute position
    absolute_modal_end = modal_start + modal_end_pos + len(modal_end_pattern)
    
    after_modal = content[absolute_modal_end:]
    
    # Reconstruct file
    new_content = before_modal + ENGLISH_MODAL + after_modal
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Successfully replaced modal in {file_path.name}")
    return True

def main():
    base_dir = Path('/Users/viktorkamyshentsev/Desktop/gravity/spa-deluxe-site')
    english_files = [
        base_dir / 'index-en.html',
        base_dir / 'wellness-en.html',
        base_dir / 'sauna-en.html',
        base_dir / 'massage-en.html',
    ]
    
    print("=" * 70)
    print("COMPLETE PRICE MODAL REPLACEMENT - ENGLISH VERSION")
    print("=" * 70)
    
    success_count = 0
    for file_path in english_files:
        if file_path.exists():
            if replace_modal(file_path):
                success_count += 1
        else:
            print(f"\n❌ File not found: {file_path.name}")
    
    print("\n" + "=" * 70)
    print(f"✓ COMPLETE! Successfully updated {success_count}/4 files")
    print("=" * 70)

if __name__ == '__main__':
    main()
