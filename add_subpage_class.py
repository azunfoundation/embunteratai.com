import glob
import os

files = [f for f in glob.glob('c:/embunteratai.com/*.html') if 'index.html' not in f.replace('\\', '/')]
count = 0
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<body>' in content:
        content = content.replace('<body>', '<body class="subpage">')
        count += 1
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print(f'Added subpage class to {count} files.')
