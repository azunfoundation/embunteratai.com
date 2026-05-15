import re
import glob

# Read index.html to extract the new header, mobile nav, and script templates
with open('c:/embunteratai.com/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

header_match = re.search(r'(<!-- HEADER -->.*?</header>)', index_content, re.DOTALL)
new_header = header_match.group(1) if header_match else ''

mobile_nav_match = re.search(r'(<!-- Mobile Drawer -->.*?<div class="mobile-nav-overlay" id="mobileNavOverlay"></div>)', index_content, re.DOTALL)
new_mobile_nav = mobile_nav_match.group(1) if mobile_nav_match else ''

script_match = re.search(r'(// Header scroll effect.*?mobileOverlay\.addEventListener\(\'click\', closeMobileNav\);)', index_content, re.DOTALL)
new_script_logic = script_match.group(1) if script_match else ''

files = [f for f in glob.glob('c:/embunteratai.com/*.html') if 'index.html' not in f.replace('\\', '/')]
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header
    content = re.sub(r'<!-- Header -->.*?</header>', new_header, content, flags=re.IGNORECASE | re.DOTALL)

    # Insert mobile nav if not present
    if '<!-- Mobile Drawer -->' not in content:
        content = content.replace('</header>', '</header>\n\n  ' + new_mobile_nav)

    # Make the right link active
    filename = file.replace('\\', '/').split('/')[-1]
    # Remove active class from Home
    content = content.replace('<a href="index.html" class="active">Home</a>', '<a href="index.html">Home</a>')
    # Add active class to current page
    content = content.replace(f'<a href="{filename}">', f'<a href="{filename}" class="active">')

    # Add script logic
    if '// Header scroll effect' not in content:
        if '<script>' in content:
            content = content.replace('</script>', '\n    ' + new_script_logic + '\n  </script>')
        else:
            content = content.replace('</body>', '\n  <script>\n    ' + new_script_logic + '\n  </script>\n</body>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print(f'Updated {len(files)} html files.')
