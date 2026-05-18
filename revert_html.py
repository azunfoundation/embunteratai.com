import os

for path in [r'c:\embunteratai.com\pricing.html', r'c:\embunteratai.com\services.html']:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Revert to old structure
    html = html.replace('<div class="container" style="width: 100%;">\n      <div class="sv-hero-content">', '<div class="sv-hero-content">')
    html = html.replace('Ask Us Anything</a>\n        </div>\n      </div>\n    </div>', 'Ask Us Anything</a>\n      </div>\n    </div>')
    html = html.replace('View Packages</a>\n        </div>\n      </div>\n    </div>', 'View Packages</a>\n      </div>\n    </div>')

    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
