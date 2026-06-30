import base64, imghdr, os, re

html_path = 'D:/Projects/AI-Report/260627-AI宣讲-v4.html'
assets_dir = 'D:/Projects/AI-Report/assets'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all img src="assets/..." references
img_pattern = re.compile(r'<img[^>]+src="(assets/[^"]+)"[^>]*>')
matches = img_pattern.findall(html)

print(f"Found {len(matches)} image references")

converted = 0
skipped = 0
errors = []

for rel_path in set(matches):
    abs_path = os.path.join(assets_dir, os.path.basename(rel_path))
    if not os.path.exists(abs_path):
        # Try with the full relative path
        abs_path = os.path.join('D:/Projects/AI-Report', rel_path)
    if not os.path.exists(abs_path):
        errors.append(f"NOT FOUND: {rel_path}")
        continue

    with open(abs_path, 'rb') as f:
        img_data = f.read()

    # Determine mime type
    img_type = imghdr.what(None, img_data)
    if not img_type:
        # Try by extension
        ext = os.path.splitext(rel_path)[1].lower()
        mime_map = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
                    '.gif': 'image/gif', '.webp': 'image/webp', '.svg': 'image/svg+xml',
                    '.ico': 'image/x-icon'}
        mime = mime_map.get(ext, 'application/octet-stream')
    else:
        mime = f'image/{img_type}'

    b64 = base64.b64encode(img_data).decode('ascii')
    data_uri = f'data:{mime};base64,{b64}'

    # Replace all occurrences of this src
    old_src = f'src="{rel_path}"'
    new_src = f'src="{data_uri}"'

    # But we need to preserve the rest of the img tag - only replace the src attribute
    html = html.replace(old_src, new_src)
    converted += 1
    size_kb = len(img_data) / 1024
    print(f"  [{converted}] {rel_path} ({size_kb:.0f}KB) -> embedded")

print(f"\nDone: {converted} embedded, {skipped} skipped, {len(errors)} errors")
for e in errors:
    print(f"  ERROR: {e}")

# Save
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Report final size
final_size = os.path.getsize(html_path)
print(f"\nFinal HTML size: {final_size/1024:.0f}KB ({final_size/1024/1024:.1f}MB)")
