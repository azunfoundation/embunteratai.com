import os
import re
import shutil

base_dir = r'c:\embunteratai.com'
images_dir = os.path.join(base_dir, 'images')
assets_img_dir = os.path.join(base_dir, 'assets', 'images')

html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

# Pattern to find src="images/..."
pattern = re.compile(r'src="(images/[^"]+)"')

copied_files = set()

for html_file in html_files:
    file_path = os.path.join(base_dir, html_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    matches = pattern.findall(content)
    if matches:
        new_content = content
        for old_rel_path in matches:
            # Decode URL encoded characters if any (like spaces)
            import urllib.parse
            old_rel_path_dec = urllib.parse.unquote(old_rel_path)
            
            src_abs_path = os.path.join(base_dir, old_rel_path_dec.replace('/', '\\'))
            filename = os.path.basename(src_abs_path)
            # Create a safe new filename to avoid conflicts (just use the basename)
            new_rel_path = f'assets/images/{filename}'
            dest_abs_path = os.path.join(assets_img_dir, filename)

            # Copy file if it exists and hasn't been copied yet
            if os.path.exists(src_abs_path):
                if filename not in copied_files:
                    shutil.copy2(src_abs_path, dest_abs_path)
                    copied_files.add(filename)
                
                # Replace in HTML
                new_content = new_content.replace(f'src="{old_rel_path}"', f'src="{new_rel_path}"')
            else:
                print(f"File not found: {src_abs_path}")

        # Save updated HTML
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {html_file}")

print(f"Copied {len(copied_files)} images to assets/images/")
