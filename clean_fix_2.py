import os
import glob
import re

print("Starting clean replacements...")

# Update CSS
css_path = r'c:\embunteratai.com\assets\css\style.css'
with open(css_path, 'r', encoding='utf-8', errors='replace') as f:
    css = f.read()

css = css.replace('background: rgba(10, 8, 5, 0.85);', 'background: rgba(61, 43, 31, 0.95);')
css = re.sub(r"(\.pillar-list li::before\{content:')[^']*(')", r"\g<1>\\2713\g<2>", css)

with open(css_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(css)

# Update HTML files
html_files = glob.glob(r'c:\embunteratai.com\*.html')
for html_path in html_files:
    with open(html_path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
    
    orig_html = html
    html = html.replace('Book a Consultation', 'Book Your Tour')
    html = html.replace('Book A Consultation', 'Book Your Tour')
    html = html.replace('Tangas basah', 'Herbal bath therapy')
    html = html.replace('tangas basah', 'herbal bath therapy')
    html = html.replace('Tunga basah', 'Herbal bath therapy')
    html = html.replace('tunga basah', 'herbal bath therapy')
    html = html.replace('Bertungku (tuam) &amp; Tangas basah', 'Bertungku (tuam) &amp; Herbal bath therapy')

    if 'index.html' in html_path:
        html = html.replace('<!-- TESTIMONIALS -->\n  <section class="section">', '<!-- TESTIMONIALS -->\n  <section class="section" style="display:none;">')

    if 'services.html' in html_path:
        html = html.replace('Exclusively<br><em>Tanamera</em>', 'Exclusively<br><em>Premium Herbal Oils</em>')
        html = re.sub(
            r'We are proud to exclusively use <strong>Tanamera</strong>[^<]*?for postpartum recovery\.',
            r'We are proud to exclusively use <strong>premium, certified herbal oils</strong> — cold-pressed, 100% natural, and specially formulated for postpartum recovery.',
            html
        )
        html = html.replace('alt="Tanamera premium postnatal herbal oil"', 'alt="Premium postnatal herbal oil"')
        html = re.sub(
            r'We exclusively partner with Tanamera[^<]*?for postpartum recovery\.',
            r'We exclusively use premium certified herbal products — natural and specially formulated for postpartum recovery.',
            html
        )

    if html != orig_html:
        with open(html_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
        print(f'Updated {os.path.basename(html_path)}')

print('Done!')
