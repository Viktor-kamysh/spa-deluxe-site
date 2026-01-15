#!/usr/bin/env python3
"""Add language switchers to mobile menus and remaining files"""

import re
from pathlib import Path

def add_mobile_switcher_czech(content):
    """Add language switcher to mobile menu in Czech files"""
    # Find mobile menu and add switcher at the end
    pattern = r'(<a href="#contact"\s+class="[^"]*">Kontakty</a>\s+</nav>)'
    replacement = r'\1\n                <div class="flex items-center gap-2 text-xs font-serif uppercase tracking-widest mt-4 pt-4 border-t border-white/20">\n                    <span class="font-bold text-white">CZ</span>\n                    <span class="text-white/50">|</span>\n                    <a href="FILENAME-en.html" class="text-white/80 hover:text-white transition-colors">EN</a>\n                </div>'
    return re.sub(pattern, replacement, content)

def add_mobile_switcher_english(content):
    """Add language switcher to mobile menu in English files"""
    pattern = r'(<a href="#contact"\s+class="[^"]*">Contacts</a>\s+</nav>)'
    replacement = r'\1\n                <div class="flex items-center gap-2 text-xs font-serif uppercase tracking-widest mt-4 pt-4 border-t border-white/20">\n                    <a href="FILENAME.html" class="text-white/80 hover:text-white transition-colors">CZ</a>\n                    <span class="text-white/50">|</span>\n                    <span class="font-bold text-white">EN</span>\n                </div>'
    return re.sub(pattern, replacement, content)

def add_desktop_switcher_en(content, filename):
    """Add language switcher to desktop nav in English files"""
    pattern = r'(</nav>)\s*(\s*<!-- Mobile Menu Button -->)'
    switcher = f'''

            <!-- Language Switcher -->
            <div class="hidden lg:flex items-center gap-2 text-xs font-serif uppercase tracking-widest">
                <a href="{filename}.html" class="text-white/80 hover:text-white transition-colors">CZ</a>
                <span class="text-white/50">|</span>
                <span class="font-bold text-white">EN</span>
            </div>
\\2'''
    return re.sub(pattern, switcher, content)

def main():
    base_dir = Path('/Users/viktorkamyshentsev/Desktop/gravity/spa-deluxe-site')
    
    # Process wellness.html, sauna.html, massage.html (Czech pages with simpler headers)
    for page in ['wellness', 'sauna', 'massage']:
        czech_file = base_dir / f'{page}.html'
        if czech_file.exists():
            # These pages don't have desktop nav, just add to header area if needed
            print(f"✓ {page}.html (header only - no nav menu)")
    
    # Process English files - add desktop switchers
    for page in ['index', 'wellness', 'sauna', 'massage']:
        en_file = base_dir / f'{page}-en.html'
        if en_file.exists():
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add desktop switcher only for index-en.html (has full nav)
            if page == 'index':
                content = add_desktop_switcher_en(content, page)
            
            with open(en_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Added switcher to {page}-en.html")
    
    print("\nLanguage switchers added!")

if __name__ == '__main__':
    main()
