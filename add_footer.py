import glob, os, re

html_files = glob.glob(r'c:\embunteratai.com\*.html')

for html_path in html_files:
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    orig = html

    # Match the footer-bottom block, allowing for mangled copyright symbols
    html = re.sub(
        r'<div class="footer-bottom">\s*<p>.*?2026 Embun Teratai.*?</p>\s*<p>Empire Damansara.*?</p>\s*</div>',
        '''<div class="footer-bottom">
        <p>&copy; 2026 Embun Teratai. All rights reserved. | Empire Damansara, Petaling Jaya</p>
        <p>Designed and developed by <a href="https://creativals.com" target="_blank" rel="noopener" style="color: var(--gold-light); text-decoration: none; transition: 0.3s opacity;" onmouseover="this.style.opacity=0.7" onmouseout="this.style.opacity=1">Creativals</a></p>
      </div>''',
        html,
        flags=re.DOTALL
    )

    if html != orig:
        with open(html_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
        print(f'Updated footer in {os.path.basename(html_path)}')

print('Done!')
