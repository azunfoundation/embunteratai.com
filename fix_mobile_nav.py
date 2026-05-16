import os, re

pages = ['about.html','booking.html','contact.html','pricing.html','rooms-baby.html','rooms-mother.html','services.html']
base = r'c:\embunteratai.com'

correct_script = """    // Mobile nav drawer
    const mobileNav = document.getElementById('mobileNav');
    const mobileOverlay = document.getElementById('mobileNavOverlay');
    const openBtn = document.getElementById('navToggle');
    const closeBtn = document.getElementById('mobileNavClose');
    function openMobileNav() {
      mobileNav.classList.add('active');
      mobileOverlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
    function closeMobileNav() {
      mobileNav.classList.remove('active');
      mobileOverlay.classList.remove('active');
      document.body.style.overflow = '';
    }
    openBtn.addEventListener('click', openMobileNav);
    closeBtn.addEventListener('click', closeMobileNav);
    mobileOverlay.addEventListener('click', closeMobileNav);"""

# Match the old broken one-liner (single line version)
old_pattern = re.compile(
    r"document\.getElementById\('navToggle'\)\.addEventListener\('click',\s*\(\)\s*=>\s*\{[^}]+\}\s*\);",
    re.DOTALL
)

for page in pages:
    path = os.path.join(base, page)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = old_pattern.sub(correct_script, content)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed: {page}')
    else:
        print(f'No match / already correct: {page}')
