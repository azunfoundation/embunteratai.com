content = open(r'c:\embunteratai.com\pricing.html', 'r', encoding='utf-8').read()

replacements = [
    ('modal-ayu', 'Ayu'),
    ('modal-suri', 'Suri'),
    ('modal-anggun', 'Anggun'),
    ('modal-teratai', 'Teratai'),
]

for modal_id, pkg in replacements:
    old = f'<button class="btn btn-outline" onclick="closeModal(\'{modal_id}\')">Close</button>'
    new = '<a href="contact.html" class="btn btn-outline modal-btn">Schedule a Visit &rarr;</a>'
    content = content.replace(old, new)

open(r'c:\embunteratai.com\pricing.html', 'w', encoding='utf-8').write(content)
print('Done - all 4 close buttons replaced with Schedule a Visit')
